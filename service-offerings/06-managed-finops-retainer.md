# Managed FinOps Retainer

**Service 6 of 9 — AICloudStrategist**
**Monthly Retainer | Ongoing after QuickStart or Implementation Sprint**

---

## Overview

The Managed FinOps Retainer is our ongoing cloud cost governance service — the operating layer that keeps the savings realised in a QuickStart or Implementation Sprint from eroding back into the bill over time.

Cloud cost is not a project. Reserved Instances expire. Workloads scale. Engineers provision services without tagging. Commitment portfolios drift out of alignment. Without continuous oversight, most organisations return to within 80% of their pre-engagement spend within six months of a one-time optimisation effort.

The retainer replaces the expensive cycle of periodic engagements with a structured, month-to-month operating rhythm: weekly anomaly triage, monthly executive-grade reporting, and a quarterly strategic deep-dive. we act as the client's embedded FinOps function — the role most Indian mid-market companies cannot justify hiring full-time at ₹40–80L per year.

> **Positioning:** This is not a dashboard subscription or a monitoring tool hand-off. Anushka B (7+ years in cloud/DevOps/automation) and a senior architect with 22+ years of Fortune 500 cloud economics experience remain active partners — reading anomalies, adjusting commitment portfolios, enforcing tagging governance, and preparing board-ready cost reports every month.

---

## Ideal Client Profile

| Signal | Typical Pattern |
|--------|-----------------|
| **Prior engagement** | Completed an AICloudStrategist QuickStart or Implementation Sprint in the last 90 days |
| **Monthly cloud spend** | INR 8 lakh – 80 lakh across AWS, Azure, or GCP |
| **Spend trajectory** | Growing 20%+ YoY; cost governance needed to keep pace with product growth |
| **Internal FinOps capacity** | No dedicated FinOps engineer; cost review is a part-time responsibility of a DevOps lead or finance analyst |
| **Commitment portfolio** | Active Reserved Instances or Savings Plans that require ongoing portfolio management |
| **Board visibility** | CXO or board receives a cloud cost line item and wants a named owner for it |
| **Compliance/showback** | Internal chargeback or showback requirements across BUs, products, or cost centres |

**Who this is not for:** Organisations with monthly spend below INR 5 lakh (retainer economics don't work at this scale — a QuickStart is the right entry point), companies mid-migration with a rapidly changing footprint (wait for stabilisation), or organisations with an internal FinOps team of 2+ people (we can augment rather than replace — scope a custom engagement).

---

## Monthly Cadence and Deliverables

### Weekly Cost Review (Every Monday)

Delivered asynchronously via Slack or email by 10:00 AM IST.

- **Anomaly digest:** Automated FOCUS-conformant billing export analysis; any day-over-day spike >15% or service-level anomaly flagged with root-cause hypothesis and recommended action
- **Commitment coverage pulse:** Current RI/SP coverage rate vs. target; expiring commitments in the next 30 days; any drift from the agreed portfolio allocation
- **Untagged resource delta:** Net new untagged spend since prior week; responsible team or service identified where attributable
- **Action item tracker:** Open items from prior weeks, owner, and due date

Typical review time for the client engineering contact: 10 minutes.

### Monthly Executive Summary (Delivered by the 5th of each month)

A structured, board-ready report covering the prior calendar month.

**Section 1 — Cost Performance**
- Total spend vs. prior month (absolute and %) with variance commentary
- Spend vs. agreed budget or forecast; deviation explanation
- Top 5 spend drivers ranked by INR delta (growing and shrinking)
- Effective RI/SP coverage rate vs. target; portfolio efficiency score
- Waste-and-idle inventory: current INR/month of identified but un-actioned waste

**Section 2 — Optimisation Activity**
- Actions taken this month: instance right-sizings, commitment purchases, lifecycle policy changes, tagging enforcement runs
- Verified savings realised vs. prior month baseline (forms the gain-share measurement basis)
- New savings opportunities identified: ranked backlog items surfaced during the month

**Section 3 — Governance Health**
- Tagging coverage rate vs. target (per-service, per-region breakdown)
- Budget alert status: any breaches or forecast-to-breach within 30 days
- New services or regions added outside the standard approved list

**Section 4 — Next Month Outlook**
- Forecast for the coming month by service and business unit
- Planned commitment purchases or modifications
- Engineering team actions requested (with effort estimates)

### Quarterly Strategic Deep-Dive (Q1/Q2/Q3/Q4)

A 90-minute working session — not a readout, a decision meeting.

- Full FinOps maturity assessment against the FinOps Foundation Crawl/Walk/Run model: which capabilities have progressed, which have regressed, and why
- Commitment portfolio rebalancing: review the 12-month consumption trend, model the next purchase tranche, assess whether to extend, modify, or let commitments expire
- Architecture cost pattern review: one service or workload selected for detailed cost-efficiency analysis each quarter (e.g., Q1: data transfer and NAT Gateway patterns; Q2: Kubernetes resource efficiency; Q3: database tier right-sizing; Q4: storage lifecycle gaps)
- FinOps roadmap update: revise the 90-day action backlog based on changed business priorities, new services, or headcount shifts
- Tooling review: assess whether OpenCost, Infracost, and dashboard configurations remain aligned to the current environment

---

## Pricing — Three Tiers (INR, excl. GST)

| Tier | Monthly Retainer | Best For | Cloud Spend Range |
|------|-----------------|----------|-------------------|
| **Starter** | ₹45,000 / month | Single cloud, single account, stable workload | INR 5L – 15L/month |
| **Growth** | ₹85,000 / month | Multi-account or multi-cloud, active engineering team | INR 15L – 40L/month |
| **Enterprise** | ₹1,50,000 / month | AWS Organisations / Azure Management Groups, multi-BU showback, board-level reporting | INR 40L+/month |

**Gain-Share Supplement (all tiers):** 20% of verified net-new monthly savings above the agreed baseline, for the first 12 months. Baseline is the spend documented at engagement start (or QuickStart report). Invoiced monthly, capped at 1× the retainer fee, drops to zero after month 12. After that, savings are entirely the client's to keep.

**Pricing rationale:** At Starter, a client spending INR 10L/month achieving a conservative 20% reduction recovers the retainer fee in 22 days of savings. The gain-share aligns incentives — AICloudStrategist only earns more when the client spends less.

**Contract terms:** Month-to-month, 60-day written notice. No minimum term. Clients from a prior QuickStart or Implementation Sprint receive a 10% discount on months 1–3.

**Payment terms:** Monthly in advance by the 1st. GST invoice issued same date.

---

## Step-by-Step Onboarding Guide

### Phase 1 — Baseline Capture (Week 1)

1. **Access confirmation:** Validate that read-only IAM/service principal/service account from the prior engagement remains active; re-provision if expired
2. **FOCUS export activation:** Enable FOCUS 1.0-conformant billing exports — AWS CUR 2.0 to S3, Azure Cost Management FOCUS export to storage account, GCP Billing export to BigQuery — if not already configured from a prior sprint
3. **Dashboard provisioning:** Deploy the AICloudStrategist baseline BigQuery (GCP) or Athena (AWS) dashboard set; connect to client's existing BI tool (Looker, Grafana, or Power BI) or provide standalone Metabase instance
4. **OpenCost continuity check:** Confirm OpenCost is running and reporting correctly post-implementation; update Helm chart to current stable release; validate namespace-level cost allocation accuracy
5. **Baseline spend snapshot:** Pull 90-day trailing spend by service, region, and account; document as the formal engagement baseline for gain-share measurement

### Phase 2 — KPI Agreement (Week 1–2)

6. **Define target metrics:** Agree on 4–6 KPIs that will govern the engagement — typical set includes: RI/SP coverage rate target (e.g., ≥70%), tagging coverage target (e.g., ≥90% by cost centre tag), monthly waste-as-a-percentage-of-bill ceiling (e.g., <5%), and a 6-month forecast accuracy target (e.g., within ±10%)
7. **Set budget alerts:** Configure AWS Budgets / Azure Budgets / GCP Budget Alerts at 80%, 90%, and 100% of agreed monthly targets; connect to the client's Slack or PagerDuty for alerting
8. **Stakeholder mapping:** Identify the weekly engineering contact (receives Monday digest), the monthly finance contact (receives executive summary), and the quarterly executive sponsor (attends deep-dive)
9. **Communication channel setup:** Establish a dedicated Slack channel (`#finops-aics`) or WhatsApp group for async communication; agree on response SLA (see Service-Level Expectations below)

### Phase 3 — Tagging Enforcement (Week 2–4)

10. **Tagging policy codification:** Formalise the tagging taxonomy from the QuickStart or agreed from scratch: mandatory tags (cost-centre, team, environment, product), optional tags (project, owner)
11. **Policy-as-code deployment:** Deploy AWS Config rules or Azure Policy / GCP Organisation Policy to enforce mandatory tags on resource creation; configure deny-new-untagged resource creation for agreed service classes (EC2, RDS, storage)
12. **Remediation sprint:** Run a one-time tag remediation pass on existing untagged resources; provide the client engineering team with a prioritised list of resources requiring manual tagging where automation cannot infer the correct value
13. **Tagging coverage baseline:** Record the pre-enforcement tagging coverage rate as the governance baseline; this becomes a tracked KPI from month 1

### Phase 4 — Commitment Portfolio Setup (Week 2–4)

14. **Portfolio inventory:** Document all active Reserved Instances and Savings Plans: term, payment option, expiry date, current utilisation rate, and covered instance family
15. **Coverage gap model:** Identify stable on-demand workloads that have 90+ days of consistent utilisation — immediate candidates for commitment conversion
16. **Purchase plan:** Prepare a phased commitment purchase recommendation using 1-year No-Upfront as the default (preserves flexibility) with 3-year options modelled for the most stable, highest-spend workloads; present to client for approval before any purchase
17. **Expiry calendar:** Set up a 90-day and 30-day expiry alert for all active commitments; review renewal vs. let-expire decision at the preceding monthly summary

### Phase 5 — Monthly Rhythm (Month 1 onward)

18. **Week 1 of each month:** Anomaly review and Monday digest; process prior month billing close
19. **Week 1, Day 3–5:** Draft monthly executive summary; validate saving figures against FOCUS export
20. **5th of each month:** Deliver executive summary; issue gain-share invoice if applicable
21. **Every Monday:** Weekly cost digest delivered by 10:00 AM IST
22. **End of each quarter:** Schedule and conduct quarterly deep-dive; update commitment portfolio model and 90-day action backlog

---

## Service-Level Expectations

| Metric | Commitment |
|--------|------------|
| **Weekly digest delivery** | Every Monday by 10:00 AM IST; no exceptions for Indian public holidays (delivered prior Friday if Monday is a holiday) |
| **Anomaly response** | Acknowledgement within 4 business hours of a spike alert; root-cause hypothesis within 1 business day |
| **Ad-hoc questions (async)** | Response within 1 business day via agreed channel |
| **Monthly report delivery** | By the 5th calendar day of the following month |
| **Quarterly deep-dive scheduling** | Booked at least 2 weeks in advance; reschedulable once with 5 business days' notice |
| **Commitment purchase execution** | Client approval required before any commitment purchase; purchase executed within 1 business day of approval |
| **Escalation response** | See Escalation Path below |

---

## Escalation Path

**Level 1 — Weekly digest or ad-hoc query not resolved within SLA**
Contact Anushka B directly via the agreed WhatsApp or Slack channel. Mark the message `[ESCALATION]`. Response within 2 hours during business hours (9:00–18:00 IST, Mon–Fri).

**Level 2 — Billing anomaly with potential production impact or spend spike >50% in a single day**
Emergency async call triggered; we will initiate a video call within 3 hours of notification regardless of time of day. Engineering lead and finance contact should be available.

**Level 3 — Commitment purchase error, billing dispute with cloud provider, or gain-share calculation dispute**
Senior architect escalation; direct involvement in any cloud provider support case; resolution SLA per cloud provider's support tier (Enterprise Support recommended for Level 3 scenarios).

---

## Tooling

All tooling is open-source or client-owned. No AICloudStrategist proprietary platform licences are required.

| Tool | Role | Notes |
|------|------|-------|
| **OpenCost** | Kubernetes namespace and workload cost allocation | Deployed in client cluster; data retained in client's Prometheus/Thanos |
| **Infracost** | Pre-deployment cost delta in CI/CD pipelines | Integrated with GitHub Actions, GitLab CI, or Azure DevOps; cost policy-as-code via `infracost comment` |
| **FOCUS 1.0 billing exports** | Normalised multi-cloud billing data | AWS CUR 2.0, Azure FOCUS export, GCP BigQuery FOCUS view; all exported to client-owned storage |
| **BigQuery dashboards** | GCP cost analysis and cross-cloud unified view | Client-owned BigQuery dataset; AICloudStrategist-maintained Looker or Grafana data source |
| **Athena dashboards** | AWS CUR analysis and savings opportunity modelling | Client-owned S3 + Athena workspace; AICloudStrategist-maintained SQL query library |
| **AWS Budgets / Azure Budgets / GCP Budget Alerts** | Real-time anomaly alerting | Configured to client's Slack, PagerDuty, or email |
| **AWS Config / Azure Policy / GCP Org Policy** | Tagging enforcement at resource creation | Policy-as-code; deployed in client's account; client retains full control |

---

## Out of Scope

The following are explicitly not included in the monthly retainer. Each can be commissioned as a separate fixed-fee workstream:

- **Code changes or infrastructure modifications:** The retainer identifies and recommends; implementation is the client's responsibility or a separately scoped Implementation Sprint workstream
- **New landing zone or account structure design:** Covered under Service 4 (Implementation Sprint)
- **Cloud provider commercial negotiations:** EDP, PPA, or enterprise agreement renegotiation is a separately scoped commercial advisory engagement
- **Security posture work:** CSPM findings, IAM remediation, and compliance mapping are covered under Service 3 (Cloud Security Posture Review)
- **Application performance or reliability work:** SLO configuration, alert routing, and observability stack work are covered under Service 2 (Reliability & Observability Sprint)
- **Data engineering or ETL pipeline cost optimisation:** BigQuery slot management, Spark cluster sizing, or Snowflake credit optimisation require a separate scoped engagement
- **Tool vendor procurement or negotiation:** AICloudStrategist does not act as a reseller or procurement agent for any cloud vendor or SaaS tool

---

## Exit Clause and Handover Process

The retainer is month-to-month. Either party may terminate with 60 days' written notice.

**What we deliver at exit:**

1. **Full documentation package:** All dashboard configurations, Athena/BigQuery query libraries, OpenCost Helm values, tagging policy-as-code, and budget alert configurations — exported in portable formats
2. **Commitment portfolio handover:** Spreadsheet model of all active commitments, expiry calendar, and recommended renewal decisions for the next 12 months
3. **KPI history export:** 12-month (or engagement-duration) trend for all agreed KPIs in CSV format
4. **Final executive summary:** Covering the terminal month and a summary of verified savings realised across the full engagement
5. **30-minute handover call:** Walk-through of all assets with the client's engineering and finance contacts; recording provided

**What the client retains after exit:** All tooling, dashboards, policies, and data stay in the client's own infrastructure. No proprietary platforms or licence dependencies left behind.

**Gain-share final settlement:** Calculated on the last full month of billing data available at exit. No gain-share charged for partial months.

---

## References

- **FinOps Foundation Maturity Model:** [finops.org/framework/maturity-model](https://www.finops.org/framework/maturity-model/) — Crawl/Walk/Run framework used in quarterly deep-dive assessments
- **FOCUS 1.0 Specification:** [focus.finops.org](https://focus.finops.org/) — Billing normalisation standard for all multi-cloud exports
- **ProsperOps:** [prosperops.com](https://www.prosperops.com/) — Autonomous RI/SP management reference; AICloudStrategist applies equivalent portfolio logic with human oversight
- **Duckbill Group (Corey Quinn):** [duckbillhq.com](https://www.duckbillhq.com/) — Industry reference for the embedded cloud economist retainer model and monthly cadence structure
- **Vantage:** [vantage.sh](https://www.vantage.sh/) — FOCUS-compatible cost visibility tooling landscape reference
- **AWS Cloud Financial Management Blog:** [aws.amazon.com/blogs/aws-cloud-financial-management](https://aws.amazon.com/blogs/aws-cloud-financial-management/) — Primary source for CUR 2.0, Savings Plans, and Compute Optimizer updates
- **OpenCost:** [opencost.io](https://www.opencost.io/) — CNCF-graduated Kubernetes cost allocation standard used in this retainer
- **Infracost:** [infracost.io](https://www.infracost.io/) — Pre-deployment cost policy-as-code integrated into client CI/CD pipelines
