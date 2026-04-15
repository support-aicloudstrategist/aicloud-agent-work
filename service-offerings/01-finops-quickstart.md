# FinOps QuickStart
## Service Offering — AICloudStrategist

**Version:** 1.0 | **Date:** April 2026  
**Status:** Active | **Tier:** Entry | **Label:** Most Popular · Door-Opener

---

## Service Overview

The FinOps QuickStart is a structured, two-week cost intelligence engagement that gives Indian SMBs and mid-market technology companies their first clear, honest picture of cloud spend — without requiring a platform migration, architectural overhaul, or proprietary software licence.

In two weeks, AICloudStrategist delivers a ranked savings backlog with verified INR figures, a tagging and cost-allocation baseline, and a 90-day implementation plan — all using open-source tooling that stays with the client after the engagement ends. No vendor licensing fees. No recurring lock-in.

The engagement is deliberately scoped as a diagnostic sprint, not a transformation programme. The goal is speed to insight: clients typically surface 15–30% in addressable monthly spend within the first seven days of analysis. The second week converts findings into a prioritised action plan their own team can execute — or which transitions cleanly into an AICloudStrategist Implementation Sprint or Managed FinOps Retainer.

> **Positioning:** Founder-led delivery by Anushka B (7+ years in cloud/DevOps/automation), with senior architect oversight carrying 22+ years of Fortune 500 cloud economics experience. You get practitioner judgment, not a junior analyst reading a dashboard.

---

## Ideal Client Profile

The FinOps QuickStart is designed for organisations that meet three or more of the following criteria:

| Signal | Typical Pattern |
|---|---|
| **Monthly cloud spend** | INR 5 lakh – 20 lakh+ across AWS, Azure, or GCP |
| **Spend growth** | Bill has grown 30–80% year-over-year without equivalent workload growth |
| **FinOps maturity** | No formal cost governance practice; cost allocation is informal or absent |
| **Commitment coverage** | Reserved Instance / Savings Plan coverage below 40% on stable workloads |
| **Tagging posture** | Less than 60% of resources are tagged to a cost centre, team, or product |
| **Stakeholder pressure** | CFO or board has questioned cloud bill growth in the last two quarters |
| **Architecture vintage** | Core infrastructure built 2019–2023, never reviewed for cost efficiency |
| **Cloud footprint** | Primarily AWS or Azure; GCP-only or heavily multi-cloud engagements may require scoping call |

**Who this is not for:** Organisations with monthly spend below INR 2 lakh (savings opportunity too small to justify the investment), teams with a mature FinOps practice already producing monthly cost reports, or companies in the middle of a major platform migration (wait until the footprint stabilises).

---

## Two-Week Delivery Plan

### Week 1 — Discover and Diagnose

**Day 1 — Kick-off and Access**
- 90-minute kick-off call with engineering lead and finance contact
- Collect read-only IAM role (AWS) / service principal (Azure) / service account (GCP)
- Confirm tagging conventions in use (even if inconsistently applied)
- Establish Slack or WhatsApp channel for async communication

**Day 2 — Data Pull and Baseline**
- Enable AWS Cost and Usage Report (CUR) or Azure Cost Management export if not already active
- Pull 6-month cost history from native cost explorers (AWS Cost Explorer, Azure Cost Analysis, GCP Billing Console)
- Run Infracost against available Terraform/Pulumi codebases to establish pre-deployment cost baseline
- Deploy OpenCost in read-only mode against Kubernetes clusters (if applicable) to surface per-namespace, per-workload cost allocation

**Day 3 — Commitment Coverage Analysis**
- Map all running EC2 / RDS / ElastiCache / Azure Compute / GCP Compute instances against active Reserved Instances and Savings Plans
- Calculate effective RI/SP coverage rate (industry benchmark: 70%+ for stable workloads; most clients are at 34–45%)
- Identify instances running on-demand that have 6+ months of stable utilisation — immediate candidates for commitment purchase
- Flag expiring reservations within 90 days

**Day 4 — Waste and Idle Resource Audit**
- Identify unattached EBS volumes, unused Elastic IPs, idle load balancers, and orphaned snapshots
- Flag EC2 / Azure VM instances with average CPU below 10% over 30 days (right-sizing candidates)
- Review S3/Blob/GCS storage lifecycle policies — non-lifecycle-managed object storage is a consistent source of silent spend growth
- Scan for development/staging resources running 24×7 without scheduled shutdown policies

**Day 5 — Tagging and Allocation Review**
- Map existing tags against cost centre and team structure
- Identify untagged or mis-tagged spend (frequently 20–35% of total bill in early-stage accounts)
- Produce tagging coverage heatmap: which services, which regions, which accounts are blind spots
- Draft a recommended tagging taxonomy aligned to the client's org structure

---

### Week 2 — Quantify and Prioritise

**Day 6 — Architecture Cost Pattern Review**
- Review data transfer and egress charges (a frequently overlooked cost driver — can represent 8–15% of AWS bills in data-heavy workloads)
- Examine NAT Gateway usage patterns; centralised egress architectures frequently eliminate 60–80% of NAT costs
- Review database instance sizing and multi-AZ configuration against actual traffic patterns
- Check for oversized Lambda memory allocations and CloudFront distribution configurations

**Day 7 — Savings Quantification**
- Assign INR value to each identified opportunity using a conservative, mid, and optimistic scenario
- Prioritise opportunities by: (i) ease of implementation, (ii) INR impact, (iii) risk to production workload
- Cross-reference findings against AWS Well-Architected Cost Optimization Pillar five focus areas: Cloud Financial Management, Expenditure Awareness, Cost-Effective Resources, Demand Management, and Continuous Optimisation

**Day 8 — Backlog Construction**
- Draft the ranked savings backlog: each item includes resource ID, current monthly cost, projected post-action cost, INR delta, effort estimate (hours), and owner recommendation
- Categorise items: Quick Wins (< 2 hours, no downtime), Planned Actions (2–8 hours, change window required), Strategic Initiatives (> 1 sprint, architecture decision required)

**Day 9 — 90-Day Roadmap and Report Drafting**
- Sequence the backlog into a 90-day implementation plan with week-by-week milestones
- Draft the full findings report with executive summary for CFO/CTO, and technical appendix for engineering leads
- Prepare tagging governance policy document

**Day 10 — Presentation and Handover**
- 2-hour readout session: executive summary (30 min), findings walkthrough (60 min), Q&A and next steps (30 min)
- Deliver all documentation and tooling credentials
- If gain-share clause applies, confirm baseline spend figure and start monitoring window

---

## Pricing Model

| Package | Price (INR) | Best For |
|---|---|---|
| **QuickStart Standard** | ₹75,000 | Single-cloud (AWS or Azure), spend up to INR 10L/month |
| **QuickStart Pro** | ₹1,10,000 | Multi-cloud or GCP-included, spend INR 10L–20L/month |
| **QuickStart Enterprise** | ₹1,50,000 | Multi-account org / AWS Organisations, spend INR 20L+/month |

**Pricing rationale:**  
At the Standard tier, a client spending INR 8L/month who realises a conservative 18% reduction (INR 1.44L/month) recovers the engagement fee in under three weeks. The pricing is structured to be defensible to a CFO on the first day: the worst-case scenario is cost-neutral by month two.

All prices are fixed-scope, fixed-fee. No hourly overruns. No travel surcharges for remote-first delivery. GST additional as applicable.

**Payment terms:** 50% on engagement start; 50% on final report delivery.

---

## Step-by-Step Implementation Guide

### Phase 1 — Discovery (Days 1–2)

1. **Access provisioning:** Client creates a read-only IAM role (AWS: `ReadOnlyAccess` + `CostExplorer:*` permissions; Azure: `Cost Management Reader` role; GCP: `Viewer` + `Billing Account Viewer`)
2. **CUR/export activation:** Enable AWS Cost and Usage Report to S3 with resource-level granularity; Azure Cost Management export to storage account; GCP Billing export to BigQuery
3. **Terraform/IaC codebase access:** Read-only clone or repository access for Infracost integration
4. **Kick-off questionnaire:** Client completes a 15-question pre-engagement form covering architecture, team structure, recent incidents, and known cost pain points

### Phase 2 — Data Pull (Days 2–3)

1. **Native cost explorers:** Pull 6-month history from AWS Cost Explorer (resource-level), Azure Cost Analysis, and/or GCP Billing Console
2. **OpenCost deployment:** For Kubernetes workloads, deploy OpenCost as a lightweight Helm chart; no persistent storage required for a read-only assessment
3. **Infracost scan:** Run `infracost breakdown` against all available Terraform workspaces; export JSON for later quantification
4. **Commitment coverage report:** Use AWS Cost Explorer RI/SP coverage and utilisation reports; Azure Reservations Utilisation report; GCP Committed Use Discount analysis

### Phase 3 — Analysis (Days 3–7)

1. **Waste identification:** Cross-reference running resources against billing data; flag resources with zero or near-zero utilisation metrics
2. **Right-sizing analysis:** Use AWS Compute Optimizer recommendations, Azure Advisor cost recommendations, and/or GCP Recommender output as a baseline; apply manual judgment to confirm
3. **Commitment gap analysis:** Model the savings from converting identified on-demand stable workloads to 1-year No-Upfront Reserved Instances / Savings Plans
4. **Storage lifecycle audit:** Review S3/Blob/GCS bucket configurations; model cost of adding lifecycle rules to move infrequently accessed objects to cheaper storage tiers

### Phase 4 — Backlog Construction (Days 7–9)

1. **INR quantification:** Each finding is assigned a conservative monthly savings estimate in INR, calculated from actual billing rates in the client's region
2. **Effort scoring:** Each item is scored on a 1–5 scale for implementation effort; items scoring 1–2 are designated Quick Wins
3. **Risk tagging:** Each item is tagged Low/Medium/High production risk; High-risk items include implementation notes and rollback procedures
4. **Backlog format:** Delivered as a structured spreadsheet (Google Sheets or Excel) with sortable columns and a summary pivot table

### Phase 5 — Presentation (Day 10)

1. **Executive summary:** One-page PDF for CFO/Board: total identified savings in INR per month, annualised, confidence interval, and recommended next action
2. **Technical readout:** Full slide deck for engineering leads covering each finding category with specific resource IDs and implementation guidance
3. **Live Q&A:** Session recorded (with permission) for internal distribution
4. **Handover:** All tooling, scripts, and credentials returned or documented for client self-service

---

## Deliverables

| Deliverable | Format | Recipient |
|---|---|---|
| Ranked Savings Backlog | Google Sheets / Excel | Engineering Lead |
| Executive Cost Summary | 1-page PDF | CFO / CTO |
| Findings Presentation Deck | PDF + PPTX | Engineering + Finance |
| Tagging Coverage Heatmap | Google Sheets | Platform / DevOps Team |
| Recommended Tagging Taxonomy | Markdown / Confluence-ready doc | Engineering Lead |
| Commitment Coverage Analysis | PDF with charts | CTO / Engineering |
| 90-Day Implementation Roadmap | Google Sheets Gantt | Engineering Lead |
| RI/SP Opportunity Model | Excel with scenario modelling | CFO / CTO |
| OpenCost Deployment Guide | Markdown runbook | DevOps Team |
| Infracost Integration Notes | Markdown runbook | DevOps Team |

**Sample backlog item format:**

```
ID: COS-042
Resource: i-0abc123def456789 (EC2, m5.2xlarge, us-east-1)
Current cost: ₹38,400/month (on-demand)
Recommended action: Convert to 1-year No-Upfront Reserved Instance
Post-action cost: ₹24,700/month
Monthly saving: ₹13,700 | Annual saving: ₹1,64,400
Effort: 1 hour (console action, no downtime)
Risk: Low
Owner: DevOps Lead
```

---

## Tooling Stack

All tools used are open-source or natively available at no additional cost. No proprietary platform licences are purchased or required.

| Tool | Purpose | Licence |
|---|---|---|
| **AWS Cost Explorer** | Native AWS cost analysis, RI/SP coverage, anomaly detection | Included with AWS account |
| **Azure Cost Management** | Native Azure cost analysis, advisor recommendations | Included with Azure subscription |
| **GCP Billing Console + BigQuery** | Native GCP cost analysis, committed use discount reporting | Included with GCP account |
| **OpenCost** | Kubernetes-level cost allocation by namespace, workload, and team | Apache 2.0 (CNCF Incubating) |
| **Infracost** | Pre-deployment cost estimation from Terraform/Pulumi IaC | Apache 2.0 |
| **AWS Compute Optimizer** | ML-based right-sizing recommendations for EC2, EBS, Lambda | Included with AWS account |
| **Azure Advisor** | Right-sizing and idle resource recommendations | Included with Azure subscription |
| **Cloud Custodian** | Policy-as-code for tagging enforcement and idle resource cleanup | Apache 2.0 |
| **Steampipe** | SQL-based cloud inventory querying across providers | AGPL 3.0 |
| **Google Sheets / Excel** | Backlog and roadmap delivery (client-editable, no tool dependency) | Client-provided |

**On proprietary platforms:** Tools such as Vantage, CloudZero, and Flexera/ProsperOps offer valuable ongoing automation (particularly for autonomous Savings Plan management). These are referenced in the findings report where appropriate, and clients are free to evaluate them independently. AICloudStrategist does not receive referral fees from any platform vendor.

---

## What Is Explicitly Out of Scope

The following are not included in the FinOps QuickStart and require a separate engagement (Implementation Sprint or Managed FinOps Retainer):

- **Actual implementation of recommendations** — the QuickStart delivers a backlog and plan; execution is either client-led or covered in a subsequent sprint
- **Architecture redesign or re-engineering** — workload migration, service replacement, or cloud-native refactoring
- **Kubernetes cluster optimisation beyond cost visibility** — node right-sizing, HPA/VPA configuration, cluster autoscaler tuning
- **Negotiation of AWS/Azure/GCP enterprise agreements or private pricing** — EDPs, EA negotiations, or marketplace deals
- **Security posture review** — IAM, network, data security are not assessed; refer to Cloud Security Posture Review offering
- **Application-level profiling** — code optimisation, database query tuning, or caching layer review
- **Multi-month monitoring** — ongoing anomaly detection and monthly reporting are part of the Managed FinOps Retainer
- **SaaS spend management** — third-party SaaS subscriptions (Datadog, Snowflake, GitHub, etc.) are noted but not deeply analysed unless pre-agreed in scope
- **FinOps team training or internal enablement programmes**

---

## Gain-Share Clause

For clients who prefer a performance-aligned model, a gain-share option is available in place of the standard fixed fee.

**Structure:**
- **Baseline:** Agreed average monthly cloud spend over the 3 months prior to engagement start, documented and co-signed at kick-off
- **Floor:** Gain-share applies only to verified savings above 10% of baseline (i.e., the first 10% of savings is included in the fixed-fee value proposition)
- **Rate:** AICloudStrategist receives 20% of verified net savings for a 6-month measurement window
- **Verification:** Monthly savings are calculated from the client's own billing console exports; no third-party metering required
- **Cap:** Gain-share is capped at 3× the equivalent fixed-fee price for the applicable QuickStart tier
- **Example:** Client with INR 12L/month baseline achieves 22% reduction (INR 2.64L/month saved). Floor excluded: INR 1.2L. Gain-share pool: INR 1.44L/month. AICloudStrategist receives 20% = INR 28,800/month for 6 months = INR 1,72,800 total (within cap of ₹3,30,000 for Pro tier)

**Eligibility:** Gain-share is available on Standard and Pro tiers only. The client must be willing to share monthly billing exports for the 6-month measurement window. Gain-share replaces, not supplements, the fixed fee.

---

## Engagement Pre-Conditions

For an accurate and timely engagement, clients are requested to have the following ready at kick-off:

1. Read-only cloud access credentials provisioned before Day 1
2. At least 3 months of billing history available in native cost tools (6 months preferred)
3. A named engineering contact available for 1–2 hours on Days 1 and 10, and async on Slack/WhatsApp during the engagement
4. Access to Infrastructure-as-Code repository (Terraform, Pulumi, CloudFormation) if available
5. A brief on any recent major infrastructure changes (migrations, traffic spikes, new products launched) that may distort billing data

---

## Why Now

The FinOps Foundation's State of FinOps 2026 report identifies that structured FinOps programmes consistently deliver 25–30% reductions in monthly cloud spend, with mature programmes cutting waste from 40% down to 15–20%. The report also marks a significant expansion of FinOps scope — from cloud infrastructure to AI workloads, SaaS, and private cloud — making a current-state baseline more valuable, not less, as AI spend accelerates.

For Indian mid-market companies, the urgency is amplified by two converging pressures: INR-denominated cloud bills rising with both USD exchange rate movement and raw consumption growth, and CFO scrutiny that has intensified since the 2024–2025 interest rate environment made "growth at all costs" a difficult board-room position to defend.

The FinOps QuickStart delivers clarity in two weeks. No long consulting engagement. No proprietary platform dependency. No re-architecture risk. Just a ranked list of INR savings, a plan to capture them, and a team that has done this before.

---

## References

1. **FinOps Foundation — State of FinOps 2026**  
   [https://data.finops.org/](https://data.finops.org/)  
   Primary authority on FinOps maturity benchmarks, team structures, and savings outcomes cited in this document.

2. **FinOps Foundation — Framework Overview and Principles**  
   [https://www.finops.org/framework/](https://www.finops.org/framework/)  
   Inform–Optimize–Operate lifecycle and FinOps principles underpinning the engagement methodology.

3. **AWS Well-Architected Framework — Cost Optimization Pillar**  
   [https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)  
   Five best-practice areas (Cloud Financial Management, Expenditure Awareness, Cost-Effective Resources, Demand Management, Continuous Optimisation) used to structure the Week 2 analysis.

4. **Corey Quinn / The Duckbill Group — The Innovation–Optimisation Continuum**  
   [https://www.duckbillhq.com/blog/the-continuum/](https://www.duckbillhq.com/blog/the-continuum/)  
   Framework for positioning cost optimisation work relative to innovation investment cycles; referenced in scoping conversations with engineering leadership.

5. **CloudZero — FinOps Tools Definitive Guide 2026**  
   [https://www.cloudzero.com/blog/finops-tools/](https://www.cloudzero.com/blog/finops-tools/)  
   Tool landscape survey used to inform tooling stack selection rationale.

6. **Vantage — Top FinOps Tools for Cloud Cost Optimization 2026**  
   [https://www.vantage.sh/blog/top-finops-tools-for-cloud-cost-optimization](https://www.vantage.sh/blog/top-finops-tools-for-cloud-cost-optimization)  
   Platform capability comparison referenced in tooling stack notes.

7. **OpenCost — Open Source Cost Monitoring for Cloud Native Environments**  
   [https://opencost.io/](https://opencost.io/)  
   CNCF Incubating project; primary tool for Kubernetes workload cost allocation in this engagement.

8. **Infracost — Shift FinOps Left**  
   [https://www.infracost.io/](https://www.infracost.io/)  
   Pre-deployment cost estimation from Terraform/Pulumi; used in Phase 2 data pull.

9. **Open Source For You — Cloud Cost Governance Using Kubecost, OpenCost, and Infracost (January 2026)**  
   [https://www.opensourceforu.com/2026/01/cloud-cost-governance-using-kubecost-opencost-and-infracost/](https://www.opensourceforu.com/2026/01/cloud-cost-governance-using-kubecost-opencost-and-infracost/)  
   Practical tooling integration guide; referenced for open-source FinOps governance patterns.

10. **Flexera — 8 FinOps Best Practices for 2026**  
    [https://www.nops.io/blog/top-finops-practices-to-effectively-manage-cloud-costs/](https://www.nops.io/blog/top-finops-practices-to-effectively-manage-cloud-costs/)  
    Industry benchmark: 25–30% average savings from structured FinOps programmes.

11. **FinOps Foundation — FinOps Cloud+ Expansion (March 2026)**  
    [https://cloudmonitor.ai/2026/03/finops-cloud/](https://cloudmonitor.ai/2026/03/finops-cloud/)  
    Expansion of FinOps scope to AI, SaaS, and private cloud; context for "Why Now" section.

12. **Medium / Haseeb — How to Start Your FinOps Journey: A Practical Guide to Cost Sprints**  
    [https://medium.com/@haseeb_53286/how-to-start-your-finops-journey-a-practical-guide-to-cost-sprints-dcd8c3d8c7c9](https://medium.com/@haseeb_53286/how-to-start-your-finops-journey-a-practical-guide-to-cost-sprints-dcd8c3d8c7c9)  
    Sprint-based FinOps delivery methodology referenced in the engagement structure.

---

*AICloudStrategist is a founder-led cloud advisory based in Rohini, Delhi. All engagements are delivered directly by the founding team. No offshore subcontracting. No junior analyst handoffs.*

*For enquiries: connect via LinkedIn or the contact form at aicloudstrategist.com*
