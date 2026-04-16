# Next blog draft — Savings Plans vs Reserved Instances

**Slug:** `savings-plans-vs-ris`
**Target publish date:** 2026-07-01 (Tue)
**Estimated word count:** 1,400
**Read time:** ~7 min

**Source markdown for publish-blog.sh:** `/docker/task-queue/data/drafts/blog-savings-plans-vs-ris.md` (when ready to publish)

---

## Article body

# Savings Plans vs Reserved Instances — When to Use Which, And Why Most Teams Get This Wrong

Every Indian mid-market team I audit has Reserved Instances AND Savings Plans. Almost none of them can explain why they have both, which one covers what, or what would happen if they just used one. The two commitment vehicles look interchangeable from a distance. Up close they are not, and the choice between them is worth ₹3-15 lakh per month on a typical account.

Here is the decision tree I use, INR-first, Indian-mid-market-specific, and the scenarios where the wrong choice quietly bleeds money.

## The Short Version

Use a decision tree:

1. **Is this workload stable for 12+ months on the same instance family?** → Reserved Instance
2. **Is this workload stable on AWS compute but family/size might change?** → Compute Savings Plan
3. **Is this workload on Fargate, Lambda, or SageMaker?** → Compute Savings Plan (RIs don't apply)
4. **Is this workload variable, scaling up and down unpredictably?** → No commitment yet — optimise the fleet first, commit second

That is 80 percent of the decision. The remaining 20 percent is where ₹5-10 lakh/month gets lost.

## The Full Comparison

### Reserved Instances

**What they cover:** Specific EC2 instance family, operating system, region, tenancy, and (for EC2) size. RDS, ElastiCache, Redshift, and OpenSearch also have their own RIs.

**Discount rate:** Up to 72% off On-Demand for 3-year All Upfront. More typically 30-55% for 1-year partial or no upfront, which is what most Indian teams choose to preserve cash.

**Flexibility:** Low. You are locked into the family and region. You CAN exchange Standard RIs for equal-or-greater-value ones (the Modify-RI path), but this is a mechanical exchange, not an automatic one.

**Best for:**
- Stable baseline workloads on specific instance families (m5, c5, r6i for example)
- Single-region, single-AZ-tier architectures
- Workloads where you have 12+ months of utilisation data and the variance is under ±15%

**Worst for:**
- Teams planning a Graviton migration — your x86 RIs won't transfer
- Multi-region workloads where traffic patterns shift between regions quarterly
- Any team that cannot confidently predict instance family composition 12 months out

### Savings Plans (specifically Compute Savings Plans)

**What they cover:** Any EC2 compute in any region, any family, any OS, any tenancy. Also covers Fargate and Lambda. The commitment is measured in dollars-per-hour of compute spend, not instances.

**Discount rate:** Up to 66% off On-Demand for 3-year All Upfront. Typically 20-35% for 1-year no-upfront Compute Savings Plans — slightly less aggressive than equivalent RIs because of the flexibility.

**Flexibility:** High. You can shift between x86 and Graviton, between m5 and r7i, between us-east-1 and ap-south-1, and the savings plan keeps applying. This is the single biggest structural advantage.

**Best for:**
- Multi-service, multi-region architectures
- Teams actively migrating to Graviton or newer instance families
- Anyone running Fargate, Lambda, or SageMaker (RIs literally do not cover these)
- Workloads with unpredictable family composition

**Worst for:**
- Pure steady-state workloads where you know the family/region won't change for 2+ years and maximum discount matters (RIs beat SPs here by 6-15% on equivalent term/payment)

### EC2 Instance Savings Plans (the third option, usually wrong choice)

EC2 Instance Savings Plans are a narrower version of Compute Savings Plans — they require you to commit to a specific instance family in a specific region, similar to an RI but with some size-flexibility benefits.

**Our take:** 90% of the time this is the worst of both worlds. You lose the multi-region/family flexibility of Compute SPs without gaining the deepest discount of RIs. Use Compute Savings Plans OR Reserved Instances, almost never EC2 Instance Savings Plans.

## The Crossover Point

On a typical Indian mid-market AWS account at ₹8 lakh/month of compute:

- **Baseline stable workload (60% of compute):** Cover with RIs (3-year partial upfront). Gets you ~55% discount on that portion.
- **Medium-stability workload (25% of compute):** Cover with Compute Savings Plans (1-year no upfront). Gets you ~25% discount but preserves flexibility.
- **Variable workload (15% of compute):** Leave On-Demand or cover with Spot. No commitment.

This blended approach typically recovers ₹3-5 lakh/month on an ₹8 lakh compute bill — 37-62% savings depending on how aggressive you go on the RI portion.

## The Three Common Mistakes

**Mistake 1: Buying Savings Plans for everything.** Feels safe. Discount is meaningfully lower than equivalent RIs. On a ₹10 lakh/month account where 60% is genuinely stable, buying SPs instead of RIs costs an extra ₹60,000-₹80,000/month compared to proper mixed coverage.

**Mistake 2: Buying Reserved Instances without a Graviton plan.** AWS will push m5 in ap-south-1 because that is what most teams currently run. But if your 2026 roadmap includes Graviton migration (m6g, c7g, r7g), the x86 RI becomes a trap. Convert via Modify-RI or avoid the commitment.

**Mistake 3: The auto-renewal trap.** AWS does not auto-renew RIs or SPs, but your team's internal "we have reservations" memory does. Every 11 months, check every expiring commitment. The biggest RI coverage gaps I see come from accounts where reservations expired in month N and nobody ran a rebalance until month N+8.

## A Practical Monthly Check (15 minutes)

Put this on your SRE lead's calendar on the 5th of each month:

1. Open AWS Cost Explorer → Savings Plans → Utilization report. Anything under 95% utilisation is waste — you are paying for commitment you are not using.
2. Cost Explorer → Reservations → Utilization and Coverage reports. Target: Coverage above 70% on stable workloads, Utilization above 95%.
3. List all commitments expiring in the next 90 days. For each, decide: renew, modify, let-expire. Document the reasoning (even a one-line note).
4. If fleet composition has shifted (new services, new instance families, new regions), model a rebalance.

Fifteen minutes per month. That's the whole FinOps governance layer for commitments. Most teams skip it because it feels too simple to be valuable.

## When to Bring In Help

If any of these sound true, we should talk:

- Your coverage is below 40% on stable workloads
- You have RIs from 2022 or 2023 that nobody has modified since
- You are starting a Graviton migration and don't have a plan for existing x86 commitments
- Your monthly cloud bill has doubled in the last 12 months and Savings Plans "didn't help"

The first diagnosis is free — book a 30-minute Cloud Cost Health Check at aicloudstrategist.com/book.html. We will tell you honestly whether your account has the ₹3-5 lakh/month of addressable commitment gap we typically see, or whether you are already in the good 20% of teams who run this well.

---

*Written by Anushka B, Founder of AICloudStrategist — a founder-led cloud cost consultancy for Indian mid-market companies. Read more at aicloudstrategist.com/blog.html.*

---

## Publish workflow

```bash
# Upload to VPS
scp blog-savings-plans-vs-ris.md root@vps:/docker/task-queue/data/drafts/

# Publish
ssh vps "/docker/task-queue/bin/publish-blog.sh savings-plans-vs-ris 2026-07-01"

# Verify
curl -sI https://aicloudstrategist.com/blog/savings-plans-vs-ris.html
```

publish-blog.sh will:
1. Convert markdown to styled HTML
2. Deploy to /var/www
3. Regenerate RSS feed and sitemap
4. Inject JSON-LD BlogPosting schema (via add-schema.py)
5. Ping Telegram group
