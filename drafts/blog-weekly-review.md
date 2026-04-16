# The 15-Minute Weekly Cloud Cost Review Every Indian Mid-Market CTO Should Run

*By Anushka B | AICloudStrategist*

---

## Most CTOs Are Already Three Weeks Behind

Here's the pattern I see constantly in mid-market companies running ₹8–20L/month on cloud — AWS in ap-south-1, maybe Azure Central India for the compliance workloads, GCP for the data team that went rogue two years ago.

The CTO reviews cloud costs monthly. Sometimes quarterly. The CFO asks a question in the board deck and someone pulls a report. Everyone nods. The bill was ₹14.2L last month. It was ₹13.8L the month before. "Looks roughly flat," someone says.

What nobody sees: the ₹2.1L that silently crept in between reviews. The dev environment a departing engineer spun up in Mumbai and forgot to tag. The Lambda function that started running every 30 seconds instead of every 5 minutes — because someone changed a cron expression and pushed it on a Thursday. The RDS read replica that never got decommissioned after the feature was rolled back.

Monthly reviews catch the damage after the fact. Quarterly reviews are a post-mortem.

A 15-minute weekly structured look, run consistently, catches drift in the window where it costs ₹40K — not ₹4L. That is the entire argument. Let me show you how to run it.

---

## The 15-Minute Weekly Ritual — Exact Paths

Set a recurring 30-minute block on a Tuesday (Monday spend data is always incomplete). Here's what you click and what you're looking for:

**AWS — Cost Explorer (ap-south-1)**

`AWS Console → Cost Management → Cost Explorer → Explore Costs`

- Set **Granularity: Weekly**, **Group by: Service**, **Filter: Region = ap-south-1**
- Compare current week vs. prior week. You want this view in 45 seconds, not 15 minutes — save it as a Cost Explorer report and bookmark it.
- Then switch **Group by: Tag → environment** to isolate prod vs. dev vs. staging. Dev/staging should be flat or trending down Monday–Friday and dead on weekends. If they're not, something's running that shouldn't be.

Prefer the CLI? This gets you the last two weeks broken by service in ap-south-1:

```bash
aws ce get-cost-and-usage \
  --time-period Start=$(date -d '14 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity WEEKLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE \
  --filter '{"Dimensions":{"Key":"REGION","Values":["ap-south-1"]}}' \
  --output table
```

**Azure — Cost Analysis (Central India)**

`Azure Portal → Cost Management + Billing → Cost Analysis → Accumulated cost`

- Switch to **Weekly** view. Group by **Service name**, then pivot to **Resource group**. Look for resource groups that have no owner tag — those are the orphans.

**GCP — FinOps Hub or BigQuery Billing Export**

If your team exports billing to BigQuery (and they should):

```sql
SELECT service.description, SUM(cost) AS weekly_cost
FROM `your-project.billing_dataset.gcp_billing_export_v1_*`
WHERE DATE(_PARTITIONTIME) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
  AND location.region = 'asia-south1'
GROUP BY service.description
ORDER BY weekly_cost DESC
LIMIT 10;
```

Total clock time for all three: 12–15 minutes with saved views and a bookmark folder. Do not improvise navigation every week — that's where the 15 minutes becomes 45.

---

## Anomaly Detection — What a 15% Week-over-Week Bump Actually Means

A 15% week-over-week increase in ap-south-1 spend is not normal variance. At ₹10L/month baseline, that's ₹1.5L of unplanned spend arriving in 7 days. Here's what's almost always behind it:

**Runaway script or misconfigured automation.** The most common culprit. A Lambda, a GitHub Actions workflow, a Glue job — something that started executing far more frequently than intended. Look at AWS Lambda invocation counts or EC2 CPU credit usage spiking on an instance that's supposedly idle.

```bash
aws ce get-anomalies \
  --date-interval StartDate=$(date -d '7 days ago' +%Y-%m-%d),EndDate=$(date +%Y-%m-%d) \
  --query 'Anomalies[*].{Service:RootCauses[0].Service,Impact:Impact.TotalImpact}' \
  --output table
```

AWS Cost Anomaly Detection surfaces this for you — but it has to be enabled and subscribed. If you haven't done that yet, that's your first action item after reading this.

**Forgotten dev environment.** Someone built a proof of concept, ran it in ap-south-1, left the EC2 on over the weekend. A t3.xlarge running 24/7 costs roughly ₹13,000/month. Three of those forgotten across a 60-person engineering team? ₹39,000/month of pure avoidable spend. The fix is a scheduled Lambda that stops untagged or non-production instances after hours — not a process change, an automated one.

**New service that scaled unexpectedly.** A new microservice got deployed, traffic hit it harder than load tests suggested, and ECS or EKS autoscaled to accommodate. This isn't necessarily bad — but it's invisible until you look. Week-over-week service-level grouping makes it obvious immediately. ₹80K of unexpected ECS spend in ap-south-1 week-one of a launch is a conversation your team should have had before the CFO saw it.

Not from bad intentions — from forgotten infra, misconfigured schedules, and absent structured review.

---

## Who Should Actually Run This (Not You)

Let me be direct: the CTO should not be clicking through Cost Explorer every Tuesday.

The person who runs this review is your **platform engineer** or your **DevOps lead** — whoever owns the infrastructure lifecycle. They know what was deployed last week. They can look at an EC2 spike in ap-south-1 and immediately say "that's the new Kafka cluster the data team stood up on Wednesday."

What the CTO owns is two things: (1) confirming the review happened, and (2) ensuring it gets escalated when it needs to. Set up a lightweight internal ritual — a Slack message or a Jira ticket — where the platform engineer posts a one-line cost signal every Tuesday by 11am. Green: within 5% week-over-week. Yellow: 5–15% increase, investigation underway. Red: >15% or unidentified anomaly, escalation needed.

This takes the cognitive overhead off the CTO's plate while keeping cloud cost visible at the right altitude. The structured review runs every week. Decisions escalate only when the numbers demand it.

---

## What to Report Up — 3-Line Weekly Email to the CFO

Your CFO does not want a cost dashboard link. They want a signal. Here's the template:

---

**Subject: Cloud Cost Signal — Week of [Date]**

This week: ₹[X]L across AWS/Azure/GCP (ap-south-1 primary). Week-over-week change: [+/-X%].  
Anomaly noted: [One line — e.g., "₹38K overage in ECS traced to autoscaling event on 14 Apr, remediated."] OR "No anomalies detected."  
Next action: [One line — e.g., "Rightsizing review for 3 over-provisioned RDS instances scheduled for Friday."] OR "On track, no action required."

---

That's it. Three lines. Sent every Tuesday. Over 12 months, that's 52 data points your CFO can see trending. It builds trust. It surfaces problems before they become board-level surprises. And it demonstrates that your engineering org has financial discipline — which matters when you're asking for headcount approval or pitching a platform modernisation to the leadership team.

---

## This Is What Managed FinOps Actually Looks Like

Seven years of working with mid-market engineering teams across Bengaluru, NCR, and Pune has shown me one consistent truth: the companies that don't overspend on cloud aren't the ones with the biggest budgets. They're the ones with the most consistent review cadence.

If you don't yet have a platform engineer who owns this, or your team is too stretched to run a structured weekly review alongside everything else — that's exactly where a **Managed FinOps Retainer** changes the equation. We come in, instrument your tagging and anomaly detection, set up your saved Cost Explorer views and alert thresholds, run the weekly review on your behalf, and deliver that 3-line CFO signal every Tuesday morning.

No re-architecture required. Open source tooling your team owns when we're done. Founder-level responsiveness on anomalies.

The first step is a free 30-minute Cloud Cost Health Check — we'll pull up your ap-south-1 spend, show you what's drifting and what's not, and give you a structured review playbook whether you engage us or not.

No sales process. No deck. Just the numbers.

[Book the Health Check → aicloudstrategist.com]

---

*Founder-led. Enterprise-reviewed.*

— Anushka B  
Founder · AICloudStrategist
