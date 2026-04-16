# DevOps & Platform Engineering

**Service code:** AICS-09
**Price range:** ₹1,50,000 – ₹3,50,000
**Timeline:** 3–4 weeks
**Delivery:** Founder-led. Enterprise-reviewed.

---

## Service Overview

Build or modernise the developer platform that actually ships your product.

DevOps has become the default word for everything from "a Jenkins pipeline that works" to "a fully self-service internal developer platform." This service cuts through that ambiguity. We audit your current deployment reality, identify the specific bottlenecks that make releases slow, fragile, or manual — and build the pipelines, GitOps layer, and platform primitives that measurably move your DORA metrics: lead time for changes, deployment frequency, change failure rate, mean time to recovery.

The output is not a reference architecture that sits in Confluence. It is working infrastructure, merged PRs, and engineers who can deploy confidently on their own by the end of the engagement.

## Ideal Client Profile

- Indian SMB or mid-market tech company shipping product on AWS, Azure, or GCP
- Engineering team between 8 and 80 people
- Currently on one of these patterns (often several at once):
  - Deployments take over 30 minutes or require a senior engineer on-call
  - Production is updated manually (SSH into instance, run migration, restart service)
  - No staging environment, or staging that drifts from production
  - CI pipeline that takes over 20 minutes to give feedback
  - Infrastructure changes happen out-of-band (manual console edits that nobody commits)
  - Kubernetes adopted 18+ months ago but no team actually runs it confidently
  - Secrets in environment variables, in git, or in Slack messages
  - Rollbacks are a multi-hour event
- Pain points expressed by leadership: "releases are a scary thing," "we lose a day every time we deploy," "we can't ship Fridays," "new engineers take 6 weeks to deploy anything"
- Platform readiness: the team has recognised that every feature team reinventing deployment is not scaling, and a platform layer is worth investing in

## Delivery Plan — Week by Week

### Week 1: Discovery and Current-State Audit (Days 1–5)

**Day 1 — Kickoff**
- 90-minute session with engineering lead, platform/DevOps lead (if one exists), and 1–2 senior developers who ship code daily
- Define scope: which services, which environments, which clouds
- Agree on DORA baseline measurement approach (GitHub/GitLab API + incident tracker)
- Provision access: CI system, cloud read-only, repo read access, container registry, Kubernetes if applicable
- NDA signed

**Day 2–3 — Current-State Audit**

*CI/CD Pipeline:*
- Map every pipeline: triggers, steps, duration, failure rate
- Identify slow stages (typically: monolithic test suites, uncached dependencies, serial builds)
- Audit build artefacts: container images, binary outputs, release bundles — where stored, how promoted
- Secrets and credentials: how they enter the pipeline, where they rest

*Deployment Mechanics:*
- Document current deployment method per service: who clicks what, when, where
- Rollback procedure: is it documented? has it been rehearsed in the last 6 months?
- Environment parity: dev vs staging vs prod configuration drift
- Database migration handling: manual, automated, versioned

*Infrastructure as Code:*
- What fraction of production infrastructure is defined in code? (This is often the single most revealing number — typically 40–70% for mid-market teams who think they are "IaC-driven")
- Terraform / OpenTofu / Pulumi / CloudFormation / ARM / Deployment Manager — which, how organised, state management hygiene
- Drift detection: is anyone running `terraform plan` on a schedule and catching manual changes?
- Policy-as-code: OPA / Sentinel / Checkov / tfsec — present or absent

*Kubernetes (if applicable):*
- Cluster topology, node pools, autoscaling configuration
- Ingress strategy (NGINX / ALB / Istio / Traefik)
- Helm chart organisation or Kustomize overlays
- RBAC hygiene, network policies, pod security standards

*Developer Experience:*
- How long from a new engineer's first day to their first production deploy?
- Self-service capabilities: can a developer spin up a preview environment, request a new service, or rotate a secret without a ticket?
- Documentation state: runbooks, architectural decision records, onboarding guides

**Day 4–5 — DORA Baseline Measurement**

Pull 90 days of data from source systems (GitHub/GitLab/Bitbucket + incident tracker) and produce the baseline:

| DORA Metric | How we measure |
|---|---|
| **Lead time for changes** | Commit merge timestamp → production deploy timestamp |
| **Deployment frequency** | Count of successful production deploys per week |
| **Change failure rate** | % of deploys that required a rollback, hotfix, or caused an incident |
| **Mean time to recovery (MTTR)** | Incident start → resolution, production-impacting only |

Categorise the team against the DORA performance tiers (Low / Medium / High / Elite). This is the number we will move, and the number the engagement is measured against.

### Week 2: Platform Design and Quick Wins (Days 6–10)

**Day 6–7 — Architecture Design**

Based on audit findings, design the target platform:

- **CI/CD layer:** GitHub Actions / GitLab CI / Jenkins / Azure DevOps — which, with what patterns (matrix builds, caching strategy, parallelism, reusable workflows)
- **GitOps layer:** ArgoCD or Flux — selected based on team familiarity and Kubernetes version. GitOps-native deployment, ephemeral environments, progressive rollouts
- **IaC structure:** Terraform module library, workspace layout, remote state backend, state locking, drift detection job
- **Policy-as-code:** OPA Gatekeeper (cluster admission), Checkov / tfsec (pre-merge scan), Sentinel (if using HCP Terraform)
- **Secrets management:** AWS Secrets Manager / Azure Key Vault / GCP Secret Manager / HashiCorp Vault — with a named rotation strategy
- **Observability hooks:** deploy markers into your monitoring stack, release dashboards, pipeline telemetry

Document the target state as an architecture decision record (ADR) — so future changes have context.

**Day 8–10 — Quick Wins Execution**

Before the bigger platform build, fix 2–3 bottlenecks identified in the audit. These are high-leverage, low-risk changes that produce immediate DORA movement:

- Add build caching to the slowest CI job (typical impact: 40–60% pipeline time reduction)
- Containerise a still-manual deployment step
- Add a `terraform plan` drift-detection job running nightly
- Pull secrets out of CI variables into a managed secrets store
- Implement a reliable rollback path for the highest-risk service

Each quick win ships as a PR, reviewed by a client engineer, merged into trunk.

### Week 3: Core Platform Build (Days 11–15)

**Day 11–12 — GitOps and Deployment Pipelines**

- Stand up ArgoCD or Flux pointed at a central `platform-manifests` repo
- Migrate 2–3 priority services from the existing deploy method to GitOps
- Implement progressive rollout: canary or blue-green for the highest-traffic service
- Wire deployment events into the observability stack (deploy markers on dashboards, Slack notifications)

**Day 13 — Internal Developer Platform (lightweight)**

For teams ready for it, build a self-service layer. This does not require Backstage on day one — often a well-structured Terraform module catalogue + a `devctl` CLI wrapper gets 80% of the value:

- Service scaffold: `new-service <name>` produces a repo with CI, IaC, observability, and deployment config pre-wired
- Environment provisioning: self-service preview environments for PRs
- Common primitives as modules: databases, queues, caches, ingress

**Day 14 — Policy and Guardrails**

- OPA Gatekeeper policies on the cluster (no `:latest` images, required labels, resource limits mandatory)
- Pre-merge policy scans on IaC (Checkov / tfsec / KICS)
- Cost guardrails via Infracost in PRs (cross-references FinOps QuickStart if already engaged)
- RBAC cleanup: principle of least privilege audit

**Day 15 — Release Dashboard + Runbook Template**

- Release dashboard in Grafana: deploys per week, lead time trend, change failure rate, MTTR — the DORA view, live
- Runbook template and 3 sample runbooks for the highest-risk failure modes identified in the audit

### Week 4: Enablement and Handover (Days 16–20)

**Day 16 — Internal Architecture Review**

Senior-architect oversight review of the platform build. Calibration pass: is the complexity level right for this team? Are we over-engineering? Under-engineering? What will this look like in 6 months if the team does nothing?

**Day 17–18 — Hands-On Enablement**

Two working sessions with the engineering team:

- **Session 1 — Platform walkthrough (90 min):** deploy flow, rollback procedure, how to add a new service, where to find what
- **Session 2 — Failure mode rehearsal (90 min):** deliberately break something (in a non-prod environment) and walk through the full recovery. The team runs the rollback, not us.

**Day 19 — Documentation Handover**

- Platform README — single source of truth for how deployment works now
- Runbooks committed in-repo (not in Confluence where they rot)
- ADRs for every significant decision taken during the engagement
- 90-day roadmap for continuing the work after we leave

**Day 20 — Executive Presentation + DORA Re-measurement**

- 60-minute session with engineering leadership and CTO
- Baseline DORA metrics vs end-of-engagement DORA metrics (where immediately measurable)
- Residual risks and named owners
- Optional: scope a follow-on Implementation Sprint (Service 04) or a DevOps retainer for ongoing coaching

## Pricing — INR

| Scope | Price | Timeline |
|---|---|---|
| CI/CD modernisation only (one cloud, 3–5 services) | ₹1,50,000 | 3 weeks |
| Full platform build (CI/CD + GitOps + IaC + secrets) | ₹2,50,000 | 3–4 weeks |
| Platform + lightweight IDP (service scaffolding, self-service previews) | ₹3,50,000 | 4 weeks |

**Payment terms:** 50% advance, 50% on delivery.
**DORA-linked gain-share option:** If the engagement moves the team from Low to Medium DORA tier (or Medium to High) as measured 60 days post-delivery, a 15% performance bonus on the fixed fee can be agreed up front. Discussed during scoping.

## Deliverables

1. **Current-State Audit Report** — every pipeline, every deployment method, every IaC module, mapped and scored
2. **DORA Baseline + Target** — 90 days of historical DORA metrics, current tier classification, target tier with timeline
3. **Target Platform Architecture** — design document with ADRs for every major decision
4. **Working CI/CD Pipelines** — reusable workflows, caching strategy, parallel test execution, secrets handled correctly
5. **GitOps Deployment Layer** — ArgoCD or Flux installed, 2–3 priority services migrated, progressive rollout configured
6. **IaC Module Library** — Terraform / OpenTofu modules for common primitives (database, queue, service, environment)
7. **Policy-as-Code Guardrails** — OPA, Checkov, tfsec configured in CI and cluster
8. **Release Dashboard** — Grafana dashboard showing live DORA metrics
9. **Runbook Template + 3 Sample Runbooks** — for the top 3 failure modes identified in the audit
10. **Platform README + ADRs** — committed in-repo, ready for next engineer to inherit
11. **Two Enablement Sessions** — platform walkthrough + failure mode rehearsal (recorded)

## Tooling Stack

| Category | Preferred Tools (selected to team fit) |
|---|---|
| CI/CD | GitHub Actions, GitLab CI, Jenkins, Azure DevOps |
| GitOps | ArgoCD, Flux |
| IaC | Terraform, OpenTofu, Pulumi |
| Policy-as-code | OPA Gatekeeper, Checkov, tfsec, KICS, Sentinel |
| Secrets | AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, HashiCorp Vault, Sealed Secrets, External Secrets Operator |
| Container registry | ECR, ACR, Artifact Registry, Harbor |
| Kubernetes | EKS, AKS, GKE, self-managed; Helm, Kustomize |
| Release orchestration | Argo Rollouts, Flagger (progressive delivery) |
| Observability hooks | Grafana deploy markers, OpenTelemetry trace correlation, Prometheus release labels |
| Cost guardrails | Infracost (PR comments) |
| Internal developer platform | Backstage (if scope justifies), custom Terraform module catalogue + devctl CLI for lighter setups |

All tooling choices are biased toward open-source. Client owns everything deployed.

## Out of Scope

- Application code refactoring (we build the platform that ships code; we don't rewrite the code)
- Test strategy design or test suite authoring (recommend separate QA engagement)
- Database schema migration tooling selection (we integrate whatever you use; we don't build it)
- SRE incident response process design (covered by Reliability & Observability Sprint, Service 02)
- Cost optimisation of cloud infrastructure (covered by FinOps QuickStart, Service 01)
- 24×7 operational support (can be scoped as a DevOps retainer)

## When This Service Makes Sense

- **"Releases are scary"** — deployments require a war-room, a senior engineer, and a backup plan that nobody has rehearsed
- **"We can't ship Fridays"** — team is working around a fragile deployment pipeline rather than fixing it
- **New engineer ramp-up is painfully slow** — a new hire takes 4+ weeks to deploy their first change to production
- **Growing from 10 to 50 engineers** — the deployment pattern that worked for 10 people breaks at 30
- **Kubernetes adoption stalled** — the cluster is running but nobody on the team is confident operating it
- **Manual changes are accumulating** — console edits, one-off scripts, "just this once" deployments that nobody committed
- **Compliance or investor requirement** — audit evidence requires automated deployments, documented rollbacks, and IaC coverage

## DORA Metrics: What Good Looks Like

From the 2024 Google DORA State of DevOps report — the industry reference for platform maturity:

| Metric | Low | Medium | High | Elite |
|---|---|---|---|---|
| Lead time for changes | > 6 months | 1 week – 1 month | 1 day – 1 week | < 1 hour |
| Deployment frequency | < 1 / month | 1/month – 1/week | 1/week – 1/day | On-demand (multiple/day) |
| Change failure rate | > 30% | 16–30% | 16–30% | 0–15% |
| MTTR | > 1 week | 1 day – 1 week | < 1 day | < 1 hour |

Most Indian mid-market teams we have audited start in the Low-to-Medium band. The realistic and worthwhile target of a 4-week engagement is a visible move into Medium, with a credible 6-month roadmap to High.

## References

- DORA — Accelerate State of DevOps Report: https://dora.dev/research/
- Google Cloud — DORA Metrics: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance
- Nicole Forsgren, Jez Humble, Gene Kim — Accelerate: The Science of Lean Software and DevOps (IT Revolution, 2018)
- Team Topologies — Matthew Skelton and Manuel Pais: https://teamtopologies.com/
- Backstage — Spotify's Internal Developer Platform: https://backstage.io
- ArgoCD Documentation: https://argo-cd.readthedocs.io/
- Flux Documentation: https://fluxcd.io/flux/
- Terraform Best Practices — Gruntwork: https://www.gruntwork.io/
- OpenTofu: https://opentofu.org/
- HashiCorp Well-Architected Framework: https://developer.hashicorp.com/well-architected-framework
- Thoughtworks Technology Radar — GitOps, IaC, Platform Engineering: https://www.thoughtworks.com/radar
- CNCF Landscape — CI/CD and Platform Engineering: https://landscape.cncf.io/
- Charity Majors — The Engineer/Manager Pendulum and Platform Thinking: https://charity.wtf/
- OPA / Gatekeeper: https://www.openpolicyagent.org/
- Infracost — Cloud Cost Estimates for Terraform in Pull Requests: https://www.infracost.io

---

*AICloudStrategist · Founder-led. Enterprise-reviewed.*
*Anushka B, Founder · support@aicloudstrategist.com*
