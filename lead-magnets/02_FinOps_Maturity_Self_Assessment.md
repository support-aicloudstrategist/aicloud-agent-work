# FinOps Maturity Self-Assessment

A 10-question diagnostic to map where your cloud cost practice stands today — and what it would take to get to the next level. Based on the FinOps Foundation's Crawl / Walk / Run framework, adapted for Indian SMBs and mid-market teams.

> Built and maintained by [AICloudStrategist](https://aicloudstrategist.com) · Founder-led. Enterprise-reviewed. · support@aicloudstrategist.com

---

## How it works

10 questions. Pick one answer per question. Add up your score. Read your maturity band at the end. Each band has a one-page action plan.

Should take you 5 minutes.

---

## The 10 questions

### 1. Who owns cloud cost in your org?
- (0) No one explicitly. Finance gets the bill.
- (1) Finance owns the bill, engineering owns the build, no one bridges them.
- (2) DevOps/SRE keeps an eye on it informally.
- (3) Designated FinOps lead or cost-owner with a calendar slot.

### 2. How is cost data shared?
- (0) Monthly bill from AWS/Azure/GCP, finance stares at it.
- (1) Quarterly cost review presentation, leadership audience.
- (2) Weekly dashboard accessible to engineering.
- (3) Real-time cost-per-service or cost-per-team visible in Slack/Teams or in a dashboard everyone bookmarks.

### 3. Tagging coverage
- (0) Untagged or inconsistent.
- (1) Some resources tagged, some not.
- (2) Mandatory tags for new resources but legacy is messy.
- (3) >90% of resources tagged with `env`, `owner`, `service`, `cost_center`. Untagged → flagged automatically.

### 4. Anomaly detection
- (0) We notice when the bill comes in.
- (1) We notice when finance escalates.
- (2) We have AWS/Azure native anomaly alerts going to a channel no one watches.
- (3) Anomaly alerts route to the team that owns the affected service, with SLA to triage.

### 5. Reserved Instance / Savings Plan strategy
- (0) None. All on-demand.
- (1) Bought RIs once, haven't reviewed since.
- (2) Annual review of RI/SP coverage tied to a baseline.
- (3) Continuous coverage management; coverage rate tracked as KPI.

### 6. Right-sizing cadence
- (0) Never.
- (1) Once after migration, never since.
- (2) Quarterly review.
- (3) Continuous: Compute Optimizer / OpenCost recommendations actioned monthly.

### 7. Engineering accountability
- (0) Engineers don't know what their workloads cost.
- (1) Costs surfaced in retros sometimes.
- (2) Each team has a monthly cost budget.
- (3) Cost-per-feature or cost-per-tenant is a tracked product KPI.

### 8. Showback / chargeback
- (0) None.
- (1) Informal showback at all-hands.
- (2) Formal showback report by team / product / customer.
- (3) Real chargeback to business unit budgets.

### 9. Forecast accuracy (last 3 months)
- (0) We don't forecast.
- (1) Forecasts are off by >25%.
- (2) Forecasts within 10–25%.
- (3) Forecasts within 5–10%, variances explained.

### 10. Tooling
- (0) Nothing beyond the cloud provider's billing console.
- (1) Native tools (AWS Cost Explorer, Azure Cost Mgmt) used regularly.
- (2) Open-source tools deployed (OpenCost, Infracost) but not universally used.
- (3) Mature stack: OpenCost + Infracost in CI + FOCUS-conformant exports + custom dashboards. Or paid tooling fully adopted.

---

## Score yourself

Add up your score (0–30).

### 0–8 — **Crawl**
You're in good company — most Indian SMBs are here. Cloud is treated as an infrastructure cost, not a managed product. Quick wins available everywhere. The next 60 days could deliver 20–30% savings with no architectural changes.

**What to do first (in this order):**
1. Pick one person as the cost owner (even part-time).
2. Tag everything. Mandate tags for new resources via SCP/policy.
3. Turn on AWS Cost Anomaly Detection (free) or Azure equivalent. Route alerts to a channel.
4. Pull a 30-day spend report. Find the top 5 waste items. Fix them.
5. After fixing, look at RI/SP coverage. Don't commit until baseline is stable.

### 9–17 — **Walk**
You have visibility but the muscle isn't built yet. Costs are tracked but not driving behavior. Engineers know costs exist but don't own them. This is where most teams plateau.

**What to do first:**
1. Move from monthly cost reviews to weekly cost dashboards engineers actually look at.
2. Set per-team or per-product cost budgets. Make finance owner of the conversation, engineering owner of the lever.
3. Get RI/SP coverage to a measured KPI (e.g. "70% Compute SP coverage on prod").
4. Adopt OpenCost (CNCF) for Kubernetes if applicable. Free.
5. Run quarterly architectural reviews focused on cost — not "review my Terraform" but "what would this cost if we 10×'d traffic."

### 18–24 — **Run**
You have a real practice. Cost is part of how engineering thinks. Forecasts are reliable. The opportunity now is sharpening: cost-per-tenant, cost-per-customer, or cost-as-a-product-KPI.

**What to do first:**
1. Build cost-per-feature or cost-per-tenant attribution. Hard but transformative.
2. Move forecasts under 10% variance.
3. Engage product management — make pricing and packaging decisions with cost as input.
4. Consider FinOps Foundation membership for community + benchmarking.
5. Train a second person in FinOps so it's not a single point of failure.

### 25–30 — **Lead**
Rare for Indian SMBs. You're operating ahead of most enterprises. The remaining ground is around AI/ML cost (rapidly growing), sustainability/carbon, and possibly multi-cloud cost normalization (FOCUS spec).

**What to do first:**
1. Adopt FOCUS-conformant exports across clouds. Normalize for analysis.
2. Build AI/ML-specific FinOps practice (GPU utilization, model serving cost-per-request).
3. Consider sharing your story externally — case studies, conference talks. It pays back in hiring.
4. Mentor adjacent teams; don't let the practice be a single hero.

---

## What if I want help getting to the next level?

This self-assessment was honest if you scored honestly. The next 60 days of improvement are usually cheap and high-impact for anyone scoring under 20. After that, structural change matters more than tooling.

**Free 30-min Cloud Cost Health Check:**
Bring your assessment score and a recent CUR sample. We'll spend 30 minutes on the highest-ROI moves you could make this quarter. You leave with a written summary, even if we never work together.

**[Book your call →](https://aicloudstrategist.com/book.html)**

— Anushka B, Founder · AICloudStrategist
[support@aicloudstrategist.com](mailto:support@aicloudstrategist.com)
