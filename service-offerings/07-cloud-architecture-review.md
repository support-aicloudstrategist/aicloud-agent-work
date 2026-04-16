# Cloud Architecture Review & Consulting

**Service code:** AICS-07
**Price range:** ₹1,25,000 – ₹2,50,000
**Timeline:** 2–3 weeks
**Delivery:** Founder-led. Enterprise-reviewed.

---

## Service Overview

A senior-architect-grade review of your AWS, Azure, or GCP architecture — mapped against the provider's Well-Architected Framework pillars and the practical realities of running production workloads at Indian mid-market scale.

This is not a dashboard exercise. It is a structured, hands-on review conducted by walking through your infrastructure alongside your engineering team. The output is a current-state architecture map, a gap analysis scored by risk and cost impact, and a prioritised remediation roadmap with named owners and timelines.

Most companies that engage us for this service have grown their cloud estate organically — quick decisions during migration, inherited architectures from departed engineers, infrastructure that nobody has reviewed since the original build. The architecture still works. It is also quietly accumulating risk, cost, and operational debt.

## Ideal Client Profile

- Indian SMB or mid-market company running production workloads on AWS, Azure, or GCP
- Cloud estate has not been formally reviewed by a senior architect in the last 12+ months
- Monthly cloud spend between ₹5L and ₹50L
- Engineering team between 10 and 150 people — strong on product, light on infrastructure governance
- Preparing for scale (Series A/B, geographic expansion, enterprise client onboarding) and needs confidence that the architecture will hold
- Post-incident situation: something broke, leadership wants to know what else is fragile
- Compliance preparation: SOC 2, ISO 27001, or DPDP readiness requires a documented architecture baseline

## Delivery Plan — Week by Week

### Week 1: Discovery and Data Collection (Days 1–5)

**Day 1 — Kickoff and Access**
- 90-minute kickoff call with engineering lead and CTO/VP Eng
- Define scope: which accounts, regions, and workloads are in scope
- Provision read-only IAM access (CloudTrail / Activity Log / Audit Log enabled)
- NDA and data handling agreement signed

**Day 2–3 — Automated Discovery**
- Run infrastructure inventory using: `aws configservice`, `azure resource graph`, or `gcloud asset inventory`
- Generate network topology map (VPC/VNet layout, peering, transit gateways, NAT, load balancers)
- Catalog compute fleet (instance types, sizes, utilisation via CloudWatch/Azure Monitor/Cloud Monitoring)
- Map storage tiers, lifecycle policies, cross-region replication
- Inventory databases (RDS/Cloud SQL/Azure SQL — engine versions, Multi-AZ, backup retention, sizing)
- Review IAM: policies, roles, service accounts, last-used timestamps, over-privileged principals
- Export IaC state (Terraform state files, CloudFormation stacks, ARM templates) if available

**Day 4–5 — Engineering Interviews**
- 3–4 × 45-minute sessions with team leads covering:
  - Deployment pipeline and release cadence
  - Incident history (last 6 months): what broke, what was the blast radius, how long to recover
  - Scaling patterns: what triggers scale, how far ahead is capacity planned
  - Data flow: how does data move between services, regions, and external systems
  - Pain points: what keeps the team up at night
- Document tribal knowledge that isn't in runbooks

### Week 2: Analysis and Gap Assessment (Days 6–10)

**Day 6–7 — Well-Architected Mapping**

Score the architecture against the 6 Well-Architected pillars (AWS) or equivalent framework:

| Pillar | What we assess |
|---|---|
| **Operational Excellence** | Deployment automation, monitoring coverage, runbook maturity, on-call rotation |
| **Security** | IAM hygiene, encryption at rest/transit, network segmentation, secrets management, compliance posture |
| **Reliability** | Multi-AZ/multi-region strategy, backup/restore testing, DR plan, RTO/RPO alignment |
| **Performance Efficiency** | Instance right-sizing, auto-scaling configuration, caching strategy, database query performance |
| **Cost Optimisation** | RI/SP coverage, storage lifecycle, orphaned resources, egress patterns (cross-references our FinOps QuickStart) |
| **Sustainability** | Right-sizing, region selection for carbon intensity, serverless where appropriate |

Each finding is scored: **Critical / High / Medium / Low** by risk, and tagged with estimated remediation effort (hours) and cost impact (₹/month).

**Day 8–9 — Deep Dives on Top Findings**
- Detailed analysis of the top 10 findings
- For each: root cause, blast radius if unaddressed, specific remediation steps, IaC code snippets where applicable
- Cross-reference with incident history: "Finding #3 (no Multi-AZ on primary RDS) is the same class of failure as the March outage"

**Day 10 — Draft Report Assembly**
- Architecture diagrams (current state) created in draw.io / Excalidraw — editable, not locked PDFs
- Gap analysis table with scoring
- Remediation roadmap: 30 / 60 / 90-day lanes, named owners, effort estimates

### Week 3 (if needed): Presentation and Handover (Days 11–15)

**Day 11 — Internal Review**
- Senior-architect oversight review of all findings and recommendations before client delivery
- Calibration: are we recommending the right things for this team's maturity and bandwidth?

**Day 12 — Executive Presentation**
- 60-minute presentation to CTO/VP Eng + CFO (if relevant)
- Format: 10 slides. Current state → top 5 risks → remediation roadmap → cost impact → next steps
- No 50-page readout. Decisions should happen in the room.

**Day 13–15 — Handover and Q&A**
- Deliver full report package (see Deliverables below)
- 2 × 45-minute working sessions with the engineering team to walk through implementation details
- Transfer architecture diagrams to the client's tooling (Confluence, Notion, internal wiki)
- Optional: scope an Implementation Sprint (Service 04) to execute the roadmap

## Pricing — INR

| Scope | Price | Timeline |
|---|---|---|
| Single cloud, single region, ≤50 resources | ₹1,25,000 | 2 weeks |
| Single cloud, multi-region, 50–200 resources | ₹1,75,000 | 2–3 weeks |
| Multi-cloud or 200+ resources | ₹2,50,000 | 3 weeks |

**Payment terms:** 50% advance, 50% on delivery.
**Gain-share option:** If the review identifies cost savings exceeding ₹2L/month, a 15% gain-share on verified savings in the first 6 months can replace or supplement the fixed fee. Discussed during scoping.

## Deliverables

1. **Architecture-as-Code Diagrams** — current-state architecture in draw.io / Excalidraw, editable, exportable to PNG/SVG/PDF
2. **Well-Architected Gap Analysis** — scored findings table (Critical/High/Medium/Low) with effort and cost-impact estimates
3. **Remediation Roadmap** — 30/60/90-day plan with named owners, Jira/Linear ticket templates, and dependency mapping
4. **Executive Summary** — 2-page boardroom-ready document for CTO/CFO: risks, costs, and recommended actions
5. **IaC Recommendations** — Terraform / CloudFormation / Pulumi code snippets for the top 5 remediation items
6. **Knowledge Transfer Sessions** — 2 × 45-minute recorded sessions walking the engineering team through findings

## Tooling Stack

| Category | Tools |
|---|---|
| Infrastructure inventory | AWS Config, Azure Resource Graph, GCP Asset Inventory, Steampipe |
| Architecture diagramming | draw.io, Excalidraw, Cloudcraft (read-only import) |
| Security posture | Prowler (AWS), ScoutSuite (multi-cloud), AWS Security Hub, Azure Defender, GCP SCC |
| Cost visibility | OpenCost, Infracost, native Cost Explorer / Cost Management |
| IaC analysis | Terraform plan, tfsec, Checkov, KICS |
| Performance / utilisation | CloudWatch, Azure Monitor, Cloud Monitoring, Datadog (if client has licence) |

All open-source where possible. Client owns all tooling deployed during the engagement.

## Out of Scope

- Hands-on remediation (covered by Implementation Sprint, Service 04)
- Application-layer code review (we review infrastructure, not business logic)
- Penetration testing or vulnerability scanning (covered by Cloud Security Posture Review, Service 03, or a dedicated pentest partner)
- AI/ML-specific architecture (covered by AI Architecture Review, Service 08)
- Ongoing monitoring or alerting setup (covered by Managed FinOps Retainer, Service 06)
- Multi-cloud unification strategy (can be scoped as a separate engagement)

## When This Service Makes Sense

- Before a funding round — investors and auditors want to see that infrastructure risk is documented and managed
- After a significant incident — understand the systemic weaknesses, not just the proximate cause
- Before scaling — if you are about to 3× traffic, 2× team, or enter a new region, validate the foundation first
- During compliance preparation — SOC 2 and ISO 27001 auditors ask for architecture documentation; this gives you a head start
- When the original architect has left — the team is operating on inherited decisions they don't fully understand

## References

- AWS Well-Architected Framework (2025): https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- Azure Well-Architected Framework: https://learn.microsoft.com/en-us/azure/well-architected/
- Google Cloud Architecture Framework: https://cloud.google.com/architecture/framework
- CIS Benchmarks for AWS/Azure/GCP: https://www.cisecurity.org/cis-benchmarks
- Steampipe (open-source cloud inventory): https://steampipe.io
- Prowler (AWS security): https://github.com/prowler-cloud/prowler
- Infracost (IaC cost estimation): https://www.infracost.io
- TOGAF Standard (architecture governance): https://www.opengroup.org/togaf

---

*AICloudStrategist · Founder-led. Enterprise-reviewed.*
*Anushka B, Founder · support@aicloudstrategist.com*
