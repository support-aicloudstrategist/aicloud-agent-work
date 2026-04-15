# Service Offerings — Consolidated Reference

Six fixed-fee cloud services for Indian SMBs and mid-market tech companies. Each engagement is scoped, time-boxed, and designed to be stacked sequentially as a client matures.

---

## Services at a Glance

### 01 · [FinOps QuickStart](01-finops-quickstart.md)
A two-week cost intelligence diagnostic that gives cloud-spending teams their first clear picture of where money goes—without requiring migration or re-architecture. Delivers a ranked savings backlog with verified INR figures, a tagging baseline, and a 90-day implementation roadmap using open-source tooling.

**Price:** ₹75,000 – ₹1,50,000 &nbsp;|&nbsp; **Timeline:** 2 weeks

---

### 02 · [Reliability & Observability Sprint](02-reliability-observability-sprint.md)
Installs a production-grade LGTM stack (Loki, Grafana, Tempo, Mimir/Prometheus) with OpenTelemetry instrumentation and defines SLIs/SLOs tied to business outcomes. Engineering teams leave with working dashboards, multi-burn-rate alerts, and runbooks—replacing intuition and log-grepping as an incident response strategy.

**Price:** ₹1,00,000 – ₹2,00,000 &nbsp;|&nbsp; **Timeline:** 3 weeks

---

### 03 · [Cloud Security Posture Review](03-cloud-security-posture-review.md)
A read-only two-week diagnostic that produces a complete, ranked cloud security exposure report aligned to CIS Benchmarks v8, NIST CSF 2.0, AWS Well-Architected Security, and OWASP Cloud-Native Top 10. Includes a DPDP Act 2023 gap assessment and a boardroom-ready executive summary.

**Price:** ₹2,50,000 – ₹5,00,000 &nbsp;|&nbsp; **Timeline:** 2 weeks

---

### 04 · [Implementation Sprint](04-implementation-sprint.md)
Hands-on execution engagement that converts the ranked backlog from any prior diagnostic into working, PR-reviewed infrastructure. Engineers write Terraform/OpenTofu directly in client environments across modular workstreams (FinOps execution, security remediation, landing zone, GitOps pipeline, Kubernetes platform, observability wiring).

**Price:** ₹1,50,000 – ₹3,00,000 per workstream &nbsp;|&nbsp; **Timeline:** 4–6 weeks (3–5 workstreams)

---

### 05 · [Migration & Re-Architecture](05-migration-rearchitecture.md)
High-complexity engagement covering three migration patterns: Data Centre → Cloud, Cloud → Cloud, and Monolith → Microservices (Strangler Fig). Uses 7 Rs portfolio classification and wave-based execution planning; every cutover is backed by a tested rollback procedure delivered via GitOps-native tooling.

**Price:** ₹9,00,000 – ₹28,00,000 &nbsp;|&nbsp; **Timeline:** 8–16 weeks

---

### 06 · [Managed FinOps Retainer](06-managed-finops-retainer.md)
Ongoing monthly cloud cost governance that preserves savings realised in QuickStart or Implementation Sprint. Provides weekly anomaly triage, monthly executive-grade reporting, quarterly strategic deep-dives, and Savings Plan / Reserved Instance portfolio management—acting as the embedded FinOps function most companies cannot justify hiring full-time.

**Price:** ₹45,000 – ₹1,50,000 / month &nbsp;|&nbsp; **Timeline:** Month-to-month (60-day exit)

---

## Typical Client Journey

Most clients move through four stages, though any service can be purchased standalone.

**Stage 1 — Health Check (Diagnostic):** The client has no formal cloud governance practice and needs a baseline. Entry point is either the **FinOps QuickStart** (cost exposure), the **Reliability & Observability Sprint** (reliability exposure), or the **Cloud Security Posture Review** (security exposure). These engagements are read-heavy and produce prioritised backlogs without modifying production infrastructure.

**Stage 2 — QuickStart:** For cost-focused clients, the FinOps QuickStart specifically is often the first touchpoint: bill has grown without equivalent workload growth, RI/SP coverage is below 40%, and nobody owns cloud spend. Two weeks, fixed fee, no migration required.

**Stage 3 — Implementation Sprint:** Once a diagnostic backlog exists, the Implementation Sprint converts it into merged PRs and production changes. Clients who have completed any diagnostic and have a named engineering owner available move here. This is where measured savings and risk reduction are actually realised.

**Stage 4 — Retainer:** After implementation, savings erode without ongoing governance. The Managed FinOps Retainer locks in a continuous oversight layer: anomaly detection, portfolio rebalancing, executive reporting, and a named FinOps owner. Appropriate once monthly cloud spend exceeds ₹8L and cost governance is a recurring business requirement.

For clients with an imminent data centre exit or a stranded cloud account, the **Migration & Re-Architecture** engagement operates outside this linear sequence and is scoped independently.

---

## Client Signal → Service Routing

| Signal | Primary Service | Secondary |
|--------|----------------|-----------|
| Cloud bill grew 30–80% YoY; no cost ownership | FinOps QuickStart | Managed Retainer |
| MTTR > 45 min; incidents resolved by log-grepping | Reliability Sprint | Implementation Sprint |
| Root account used operationally; no MFA; preparing for SOC 2 / ISO 27001 / DPDP | Security Posture Review | Implementation Sprint |
| Diagnostic backlog exists; IaC codebase in place; engineering owner available | Implementation Sprint | — |
| Data centre lease expiring in 6–18 months; 10–100 VMs to migrate | Migration & Re-Architecture | Implementation Sprint |
| Legacy monolith; >1-week deployment cycle; vertical scaling only | Migration & Re-Architecture | Reliability Sprint |
| Cloud spend ₹8L–₹80L/month; no dedicated FinOps engineer; board scrutiny | Managed Retainer | FinOps QuickStart |
| RI/SP coverage below 40% on stable workloads | FinOps QuickStart | Managed Retainer |
| Alert fatigue; threshold-only monitors; no SLOs defined | Reliability Sprint | Implementation Sprint |
| BFSI / healthtech / edtech; personal data in cloud; regulatory audit pending | Security Posture Review | Implementation Sprint |

---

## Bibliography

Deduplicated across all six service offering documents.

**FinOps & Cloud Cost**
- FinOps Foundation — State of FinOps 2026: https://data.finops.org/
- FinOps Foundation — Framework Overview and Principles: https://www.finops.org/framework/
- FinOps Foundation — Maturity Model: https://www.finops.org/framework/maturity-model/
- FOCUS 1.0 Specification: https://focus.finops.org/
- FinOps Foundation — FinOps Cloud+ Expansion (March 2026): https://cloudmonitor.ai/2026/03/finops-cloud/
- CloudZero — FinOps Tools Definitive Guide 2026: https://www.cloudzero.com/blog/finops-tools/
- Vantage — Top FinOps Tools for Cloud Cost Optimization 2026: https://www.vantage.sh/blog/top-finops-tools-for-cloud-cost-optimization
- Corey Quinn / The Duckbill Group — The Innovation–Optimisation Continuum: https://www.duckbillhq.com/blog/the-continuum/
- ProsperOps: https://www.prosperops.com/
- Flexera — 8 FinOps Best Practices for 2026: https://www.nops.io/blog/top-finops-practices-to-effectively-manage-cloud-costs/
- Medium / Haseeb — How to Start Your FinOps Journey: A Practical Guide to Cost Sprints: https://medium.com/@haseeb_53286/how-to-start-your-finops-journey-a-practical-guide-to-cost-sprints-dcd8c3d8c7c9

**Open-Source Tooling (Cost)**
- OpenCost — Open Source Cost Monitoring for Cloud Native Environments: https://opencost.io/
- Infracost — Cloud Cost Estimates for Terraform in Pull Requests: https://github.com/infracost/infracost
- Infracost — How to Set Up Infracost in CI/CD Pipelines for Terraform (2026): https://oneuptime.com/blog/post/2026-02-23-how-to-set-up-infracost-in-cicd-pipelines-for-terraform/view
- Open Source For You — Cloud Cost Governance Using Kubecost, OpenCost, and Infracost (Jan 2026): https://www.opensourceforu.com/2026/01/cloud-cost-governance-using-kubecost-opencost-and-infracost/
- AWS Cloud Financial Management Blog: https://aws.amazon.com/blogs/aws-cloud-financial-management/

**Reliability & Observability**
- Google SRE Book: Service Level Objectives: https://sre.google/sre-book/service-level-objectives/
- Google SRE Workbook: Implementing SLOs: https://sre.google/workbook/implementing-slos/
- Google Cloud: SRE Fundamentals — SLIs, SLOs, SLAs: https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos
- OpenTelemetry: LGTM Stack Integration (2026): https://oneuptime.com/blog/post/2026-02-06-lgtm-stack-opentelemetry/view
- Grafana Labs: Cloud-Native Observability Stack 2026: https://johal.in/cloud-native-observability-stack-prometheus-grafana-loki-and-tempo-integration-for-full-stack-monitoring-2026-3/
- Honeycomb: Observability and the DORA Metrics: https://www.honeycomb.io/blog/observability-dora-metrics
- Honeycomb: What the 2025 DORA Report Teaches Us About Observability: https://www.honeycomb.io/blog/what-2025-dora-report-teaches-us-about-observability-platform-quality
- Nobl9: SLO Best Practices: https://www.nobl9.com/service-level-objectives/slo-best-practices
- Nobl9: Multi-Burn Rate Alerting: https://docs.nobl9.com/slocademy/manage-slo/create-alerts/
- Nobl9: Runbook Best Practices: https://www.nobl9.com/it-incident-management/runbook-example
- CNCF: OpenTelemetry Unified Observability (2025): https://www.cncf.io/blog/2025/11/27/from-chaos-to-clarity-how-opentelemetry-unified-observability-across-clouds/
- CNCF: Observability Trends 2025: https://www.cncf.io/blog/2025/03/05/observability-trends-in-2025-whats-driving-change/
- Datadog + AWS: Observability Maturity Model 2026: https://dev.to/aws-builders/datadog-aws-observability-maturity-model-2026-210m

**Cloud Security**
- CIS Benchmarks — Cloud Security Hardening: https://www.cisecurity.org/cis-benchmarks
- CIS Benchmarks March 2026 Update: Zero Trust and Passwordless Authentication: https://iplogger.org/blog/cis-benchmarks-march-2026-update/
- NIST Cybersecurity Framework 2.0: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
- NIST CSF 2.0 Complete Guide 2026: https://www.saltycloud.com/blog/nist-csf-2-0-complete-guide-2026/
- AWS Well-Architected Security Pillar: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html
- Microsoft Cloud Security Benchmark — Posture and Vulnerability Management: https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-posture-vulnerability-management
- Cloud Security Posture Management in 2026 — Security Boulevard: https://securityboulevard.com/2026/03/cloud-security-posture-management-in-2026/
- OWASP Cloud-Native Application Security Top 10: https://nest.owasp.org/projects/cloud-native-application-security-top-10
- Prowler CSPM Use Cases: https://prowler.com/use-cases/cloud-security-posture-management
- Prowler vs ScoutSuite vs cloud-audit 2026: https://haitmg.pl/blog/aws-security-scanners-compared/
- Top 9 Open Source CSPM Tools 2026 — SentinelOne: https://www.sentinelone.com/cybersecurity-101/cloud-security/open-source-cspm/
- Wiz Pricing 2026: https://www.wizpricing.com/
- Orca Security: What are CIS Benchmarks in Cloud Security?: https://orca.security/resources/blog/what-are-cis-benchmarks-in-cloud-security/
- DPDP Act 2023 and DPDP Rules 2025 — EY India: https://www.ey.com/en_in/insights/cybersecurity/decoding-the-digital-personal-data-protection-act-2023
- India's DPDP Rules 2025 — Deloitte: https://www.deloitte.com/in/en/services/consulting/about/indias-dpdp-rules-2025-leading-digital-privacy-compliance.html
- DPDP Rules 2025 Notified — PIB India: https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf

**Infrastructure as Code & GitOps**
- AWS Well-Architected Framework — Cost Optimization Pillar: https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html
- AWS Well-Architected Review Checklist 2026: https://towardsthecloud.com/blog/aws-well-architected-review-checklist
- AWS — Landing Zone Accelerator on AWS: https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/
- AWS — Best Practices for Rapidly Deploying Landing Zone Accelerator: https://aws.amazon.com/blogs/devops/best-practices-for-rapidly-deploying-landing-zone-accelerator-on-aws/
- Microsoft — Azure Cloud Adoption Framework: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/
- Google Cloud — Enterprise Foundations Blueprint: https://docs.cloud.google.com/architecture/blueprints/security-foundations
- GoogleCloudPlatform — Cloud Foundation Toolkit: https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit
- HashiCorp Well-Architected Framework — Infrastructure as Code: https://developer.hashicorp.com/well-architected-framework/define-and-automate-processes/define/as-code/infrastructure
- HashiCorp — Phases of Terraform Adoption: https://developer.hashicorp.com/terraform/intro/phases
- Gruntwork — Scalable IaC for Terraform and OpenTofu: https://www.gruntwork.io/
- Anton Babenko — Terraform AWS Modules: https://github.com/antonbabenko
- Thoughtworks Technology Radar — GitOps: https://www.thoughtworks.com/radar/techniques/gitops
- Thoughtworks Technology Radar — Pipelines for Infrastructure as Code: https://www.thoughtworks.com/en-br/radar/techniques/pipelines-for-infrastructure-as-code
- DEV Community — ArgoCD vs FluxCD: Which GitOps Tool Should You Use in 2026?: https://dev.to/mechcloud_academy/the-gitops-standard-in-2026-a-comparative-research-analysis-of-argocd-and-fluxcd-46d8
- Calmops — GitOps 2026 Complete Guide: https://calmops.com/devops/gitops-2026-complete-guide/
- Atmosly — GitOps for Kubernetes: Complete Implementation Guide (2026): https://atmosly.com/blog/gitops-for-kubernetes-implementation-guide-2025

**Migration & Architecture**
- AWS Application Migration Service (MGN) documentation
- Azure Migrate — wave planning, agentless VMware discovery, Azure Copilot Migration Agent (March 2026)
- GCP Migration Center — wave grouping, M4CE live/cold/offline migration modes
- The 7 Rs of Cloud Migration — originally Gartner 5 Rs (2010); expanded to 7 Rs by AWS
- Martin Fowler — StranglerFigApplication: https://martinfowler.com/bliki/StranglerFigApplication.html
- Sam Newman — Monolith to Microservices (O'Reilly, 2019)
- TOGAF Cloud Migration Patterns — Architecture Vision, Migration Planning, Transition Architecture
- Gartner — 3 Journeys for Migrating a Data Center to Cloud IaaS
