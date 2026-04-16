# The Five Kubernetes Cost Questions Nobody on Your Platform Team Can Answer

*By Anushka B*

---

Here's a situation that plays out in engineering retrospectives across India every quarter.

A senior platform engineer pulls up the AWS or GCP bill. The number has climbed — again. ₹18 lakh last month, ₹22 lakh this month. Leadership wants a breakdown. The platform team goes quiet. Not because they don't care, but because the honest answer is: *we don't know where it went.*

You have observability for everything. Grafana dashboards. Datadog traces. PagerDuty alerts at 2 AM. You know exactly when your p99 latency spikes. You can tell which pod restarted and why. But ask your platform team what it cost to serve Tenant A last week versus Tenant B, and they'll stare at their laptops like the answer might crawl out of the terminal if they wait long enough.

This is the Kubernetes cost visibility gap — and it's not a niche problem. It's endemic to any team running 100+ pods across shared clusters without proper cost attribution tooling. You've built excellent operational intelligence. You've built almost zero financial intelligence.

The consequences compound quietly. Engineering leaders can't make resource trade-offs on data. Product teams can't price features accurately. FinOps reviews turn into guesswork sessions with spreadsheets. And the cloud bill keeps climbing because no one can point to *exactly* what changed and *exactly* what it cost.

Let's go through the five questions your platform team almost certainly cannot answer right now — and the commands and queries that start changing that.

---

## Question 1: What Does One Tenant Cost to Serve?

This is the foundational question for any SaaS platform on Kubernetes. If you're multi-tenant with namespaces or labels per tenant, you should be able to say: "Serving Tenant Acme Corp cost us ₹47,000 last month." Almost nobody can.

Without tenant-level cost attribution, you cannot have cost-based pricing conversations. You cannot identify your most expensive customers. You cannot tell whether that enterprise discount you gave is actually margin-positive.

**With OpenCost:**

```bash
# Query cost allocation by tenant label over the last 30 days
curl -G http://opencost.kube-system.svc:9003/allocation \
  --data-urlencode 'window=30d' \
  --data-urlencode 'aggregate=label:tenant' \
  --data-urlencode 'accumulate=true' | jq '.data[] | {name: .name, totalCost: .totalCost}'
```

This requires your pods to carry a `tenant` label — which they should if you're multi-tenant. If they don't, that's your first infrastructure debt to address.

What you'll get back: per-tenant CPU cost, memory cost, GPU cost (if applicable), network, and PV storage — all denominated in dollars by default, which you convert at the prevailing USD/INR rate. A tenant consuming ₹2.4 lakh/month on a shared ₹15 lakh cluster is information that changes pricing conversations immediately.

---

## Question 2: Which Namespace Is Most Expensive?

This sounds trivial. It is not. Namespace-level cost visibility is where most teams think they have coverage, and most teams are wrong.

`kubectl top pods -n payments` gives you current resource *usage*. It tells you nothing about cost. Your actual spend depends on resource *requests* (what Kubernetes reserves for scheduling), usage (what the pod actually consumes), and the blended compute cost of the nodes those pods land on.

**With kubectl and metrics-server (usage only):**

```bash
# Aggregate CPU and memory requests by namespace
kubectl get pods --all-namespaces -o json | \
  jq -r '.items[] | [.metadata.namespace, 
    (.spec.containers[].resources.requests.cpu // "0"), 
    (.spec.containers[].resources.requests.memory // "0")] | @tsv' | \
  sort | awk '{ns[$1]+=$2; mem[$1]+=$3} END {for (n in ns) print n, ns[n], mem[n]}'
```

**With OpenCost (actual cost attribution):**

```bash
curl -G http://opencost.kube-system.svc:9003/allocation \
  --data-urlencode 'window=7d' \
  --data-urlencode 'aggregate=namespace' \
  --data-urlencode 'accumulate=true' | \
  jq '.data[] | {namespace: .name, totalCost: .totalCost, cpuCost: .cpuCost, memoryCost: .memoryCost}' | \
  sort -t: -k2 -rn
```

In teams we've worked with, the answer is almost always surprising. The `data-pipeline` namespace running batch jobs nobody monitors is frequently the most expensive. Not the customer-facing APIs everyone obsesses over.

At ₹18 lakh/month cluster spend, knowing that one namespace accounts for ₹6.2 lakh — and that it could be optimised with smarter job scheduling — is actionable intelligence.

---

## Question 3: What Percentage of Cluster Capacity Is Idle Overnight?

Indian SaaS companies predominantly serve Indian customers. Traffic drops sharply between midnight and 7 AM. But most Kubernetes clusters run at their daytime provisioning levels 24/7.

If your cluster is sized for peak daytime load and you're not scaling down overnight, you're paying full price for empty capacity — potentially 30–40% of your monthly bill.

**Check actual node utilisation right now:**

```bash
# Node-level CPU and memory utilisation
kubectl top nodes

# Requested vs allocatable capacity per node
kubectl describe nodes | grep -A 5 "Allocated resources"
```

**Get a cleaner picture of request-to-allocatable ratio:**

```bash
kubectl get nodes -o json | jq -r '.items[] | 
  .metadata.name + " " + 
  .status.allocatable.cpu + " " + 
  .status.allocatable.memory'
```

Cross-reference this with your actual `kubectl top nodes` output at 2 AM. The delta is your idle capacity tax. For a team on a 20-node cluster at ₹4,500/node/month (typical GKE n2-standard-4 equivalent in Mumbai region), 8 hours of idle overnight across 8 nodes is roughly ₹14,400/month in pure waste. Across a year: ₹1.7 lakh, just for leaving the lights on.

Horizontal Pod Autoscaler and Cluster Autoscaler with appropriate `--scale-down-delay` settings fix this. But you can't prioritise what you can't see.

---

## Question 4: Which Services Are Over-Requested vs Actual Usage?

This is where most Kubernetes cost waste hides — not in dramatically over-provisioned nodes, but in the quiet accumulation of conservative resource requests that developers set once and never revisit.

A service that requests 2 CPUs and 4Gi memory but consistently uses 0.3 CPUs and 600Mi memory is holding 1.7 CPUs and 3.4Gi memory hostage from the scheduler. Multiply this across 40 microservices and you're paying for a cluster that's 2–3x larger than it needs to be.

**Find the worst offenders:**

```bash
# Compare requests vs actual usage per pod
kubectl top pods --all-namespaces --sort-by=cpu | head -40

# For a specific namespace, get request vs limit ratio
kubectl get pods -n production -o json | jq -r '
  .items[] | .metadata.name as $name |
  .spec.containers[] | 
  [$name, .name, 
   (.resources.requests.cpu // "none"), 
   (.resources.limits.cpu // "none")] | @tsv'
```

**With OpenCost efficiency metrics:**

```bash
curl -G http://opencost.kube-system.svc:9003/allocation \
  --data-urlencode 'window=7d' \
  --data-urlencode 'aggregate=pod' \
  --data-urlencode 'accumulate=true' | \
  jq '.data[] | select(.cpuEfficiency < 0.3) | 
    {pod: .name, cpuEfficiency: .cpuEfficiency, 
     memorEfficiency: .ramEfficiency, waste: .totalEfficiency}'
```

Anything with `cpuEfficiency` below 0.3 is using less than 30% of what it requested. These are your VPA (Vertical Pod Autoscaler) candidates. For teams with 50+ services and a ₹20 lakh monthly bill, rightsizing the bottom 20% of efficiency is typically a ₹3–5 lakh monthly saving — without touching a single line of application code.

---

## Question 5: What Does One CI/CD Pipeline Run Cost?

This question makes platform engineers uncomfortable because the answer exists — it's just that nobody has ever calculated it.

Your CI/CD pipelines run on your cluster (or consume cluster-adjacent compute). Every `helm upgrade`, every `kubectl apply`, every integration test suite has a cost. If your pipelines run 200 times a day across 15 teams, and each run consumes meaningful CPU and memory for 4–8 minutes, that's a non-trivial monthly line item hiding inside your "general compute" bucket.

**Instrument pipeline jobs with cost labels:**

```yaml
# In your pipeline pod spec or job template
metadata:
  labels:
    cost-center: ci-cd
    team: payments
    pipeline: release-deploy
```

**Then query:**

```bash
curl -G http://opencost.kube-system.svc:9003/allocation \
  --data-urlencode 'window=30d' \
  --data-urlencode 'aggregate=label:pipeline' \
  --data-urlencode 'accumulate=true' | \
  jq '.data[] | {pipeline: .name, totalCost: .totalCost}'
```

**Quick approximation without OpenCost:**

```bash
# Find CI namespace pod resource consumption
kubectl top pods -n ci-cd --sort-by=cpu

# Get average run duration from your CI tool logs, multiply by:
# (CPU cores requested × node $/hour) + (memory GiB × memory $/hour)
```

If each pipeline run costs ₹12 and you're running 6,000 runs/month, that's ₹72,000/month on CI alone. Teams that see this number start making different decisions: caching aggressively, parallelising smarter, killing redundant test stages. The ones who don't see it keep clicking "re-run pipeline" without consequence.

---

## The Common Thread

Every one of these questions is answerable. The tools exist: OpenCost (open-source, CNCF sandbox), Kubecost, native cloud cost allocation tags, VPA recommendations. The kubectl commands exist. The Prometheus metrics exist.

What doesn't exist on most platform teams is the 2–3 week investment to set up the attribution framework, label consistently, configure the tooling, and build the dashboards that turn raw cost data into actionable team-level visibility.

That's not a criticism — platform teams are stretched. But the cost of *not* building this visibility isn't abstract. It's ₹3–8 lakh per month in avoidable waste for a mid-size cluster, compounding every month you don't look.

---

## Want This Built for Your Cluster?

We run cost attribution engagements for platform and DevOps teams: OpenCost or Kubecost setup, namespace and tenant labelling strategy, Grafana cost dashboards, and a rightsizing report that identifies your top 10 waste sources with specific fixes.

Teams typically see 20–35% cluster cost reduction within 60 days. The engagement pays for itself before the second invoice.

**[Talk to us about our DevOps & Platform Engineering service →]**

If you're running ₹10 lakh+/month on Kubernetes and can't answer these five questions, that's not an observability gap. It's a revenue leak.

---

*Anushka B writes about platform engineering, FinOps, and the infrastructure decisions Indian SaaS teams avoid until they can't. If this resonated, share it with your platform lead.*
