# Migration & Re-Architecture

**Service 5 of 6 — AICloudStrategist**
**Fixed Price: ₹9,00,000–₹28,00,000 | Duration: 8–16 weeks**

---

## Overview

Most Indian mid-market technology companies are running workloads that were never designed for the cloud they're running on. The data centre lease is expiring. The monolith is choking on traffic. The AWS account that started as a proof-of-concept in 2019 is now production — with no landing zone, no tagging, and infrastructure provisioned by hand. The cost of not migrating is compounding.

Migration & Re-Architecture is AICloudStrategist's highest-complexity, highest-leverage engagement. It covers three distinct migration patterns, each with its own risk profile, tooling selection, and delivery approach:

1. **Data Centre → Cloud** — physical or virtualised on-premises workloads moved to AWS, Azure, or GCP using block-level continuous replication with AWS MGN, Azure Migrate, or GCP Migrate to Virtual Machines (M4CE).
2. **Cloud → Cloud** — workloads stranded on the wrong cloud (legacy AWS in a GCP-first org, shadow Azure subscriptions, Oracle Cloud migrations) re-homed with minimal downtime.
3. **Monolith → Microservices** — application re-architecture using Martin Fowler's Strangler Fig pattern and Sam Newman's decomposition playbook: extract domain boundaries incrementally, ship to production at each step, never rewrite from scratch.

Every engagement is structured around the **7 Rs** portfolio classification (Rehost · Replatform · Refactor · Repurchase · Retain · Retire · Relocate), wave-based execution planning, and GitOps-native delivery. Every workload that moves is tested before it's cut over. Every cut-over has a tested rollback procedure.

> **Positioning:** Founder-led delivery by Anushka B (7+ years in cloud/DevOps/automation), with senior architect oversight carrying 22+ years of Fortune 500 infrastructure migration experience — including data centre exits and monolith decompositions for fintech, e-commerce, and healthcare clients. You get an architect who has run cutovers at 2 AM, not a project manager who has managed the RAID log.

---

## Ideal Client Profile

| Signal | Typical Pattern |
|--------|-----------------|
| **Data centre exit** | On-premises lease expiring in 6–18 months; 10–100 VMs or bare-metal servers to migrate; VMware vSphere, Hyper-V, or bare-metal Linux/Windows |
| **Cloud-to-cloud stranded workloads** | Legacy cloud account with no landing zone, no tagging governance, and infrastructure that has drifted from any original design; team has decided to standardise on a different primary cloud |
| **Monolith under strain** | Single deployable unit with 50k–500k LOC; deployment cycle >1 week; a single team owns the entire codebase; scaling requires vertically resizing the whole application; one broken module blocks all other releases |
| **Spend range** | Monthly infrastructure spend INR 5 lakh–50 lakh+; migration ROI is positive within 18 months |
| **IaC readiness** | Has or is willing to adopt Terraform or OpenTofu; no console-only clients for workloads that land in the target environment |
| **Team access** | Can provide read access to source environment and administrative access to target; has a named technical owner for the engagement |
| **Decision authority** | Can approve change windows, DNS cutover, and (for cloud-to-cloud) parallel-run cost during migration |

**Who this is not for:** Organisations mid-incident or mid-audit (stabilise first). Clients with no intention of adopting IaC in the target environment — the migration produces Terraform state; if you are unwilling to maintain it, the landing will be unstable. Single-region hobby or dev workloads below ₹1L/month (the fixed-fee structure does not yield value at that scale).

---

## 8–16 Week Delivery Cadence

### Phase 1 — Portfolio Assessment & Migration Strategy (Weeks 1–3)

**Goal:** Classify every workload using the 7 Rs framework; produce a scored migration backlog; agree wave sequencing before a single VM moves.

| Week | Activity | Milestone |
|------|----------|-----------|
| **W1** | Kick-off; collect asset inventory (VMware exports, AWS Config snapshots, Azure Resource Graph queries, GCP Asset Inventory); dependency mapping using network flow logs and application-level call graphs | Asset inventory spreadsheet; dependency map (draw.io / Structurizr) |
| **W2** | Score each workload on two axes: migration complexity (data volume, external integrations, licensing, compliance classification) and business criticality (revenue dependency, SLA tier, change-risk appetite); apply 7 Rs classification | 7 Rs classification matrix; scored migration backlog |
| **W3** | Wave plan: group workloads into 3–5 migration waves ordered by risk (low-complexity Rehost candidates in Wave 1; Refactor candidates in final waves); define success criteria, rollback triggers, and parallel-run durations for each wave | Signed wave plan; migration runbook template |

**Phase 1 gate:** Client and AICloudStrategist sign off on the wave plan before landing zone build begins. No workloads move before this gate.

---

### Phase 2 — Landing Zone & Pilot Migration (Weeks 4–7)

**Goal:** Build the target environment; execute Wave 1 (3–5 low-risk workloads) as a live rehearsal of the full migration process.

| Week | Activity | Milestone |
|------|----------|-----------|
| **W4** | Deploy target landing zone: AWS Control Tower + LZA, Azure CAF Landing Zone, or GCP Foundation Blueprint; configure network topology (hub-and-spoke, shared VPC, or Transit Gateway), IAM governance, logging baseline, and tagging enforcement via Terraform/OpenTofu | Landing zone live in target account; all changes in version-controlled IaC |
| **W5** | Install replication agents on Wave 1 source workloads: AWS MGN agent (block-level continuous replication to EC2), Azure Migrate appliance (agentless VMware discovery + replication), or GCP M4CE (live migration, cold migration, or offline image import); configure data replication lag monitoring | Replication established; lag < 30 seconds for Wave 1 workloads |
| **W6** | Validate Wave 1 in target: smoke tests, performance baseline comparison, integration endpoint checks, security group/firewall rule equivalence audit | Wave 1 validation report |
| **W7** | Wave 1 cutover: schedule change window; stop writes on source; sync final delta; update DNS / load balancer targets; monitor for 72 hours; decommission source only after stability confirmation | Wave 1 live in target; rollback not triggered |

**Phase 2 gate:** Wave 1 runs stably for 72 hours post-cutover with no P1 incidents before Wave 2 begins.

---

### Phase 3 — Wave Execution & Iteration (Weeks 8–13)

**Goal:** Execute remaining migration waves using the playbook validated in Phase 2; apply Replatform and Refactor strategies for workloads that require it.

Each wave follows the same loop: **Replicate → Validate → Cutover → Stabilise → Decommission source**.

For **Replatform** workloads (e.g., self-managed MySQL → RDS/Cloud SQL, self-managed Kafka → MSK/Confluent Cloud): database migration runs via AWS DMS or equivalent with CDC (Change Data Capture) for near-zero downtime; application connection strings updated in Terraform.

For **Refactor / Strangler Fig** workloads (monolith decomposition): AICloudStrategist deploys an API gateway or edge proxy in front of the monolith on Day 1; new microservices are extracted domain-by-domain and routed through the proxy; the monolith handles only the domains not yet extracted. Traffic percentage shifts are controlled via feature flags. No big-bang rewrite. Each extracted service ships to production independently with its own CI/CD pipeline before the next extraction begins.

| Week | Activity | Milestone |
|------|----------|-----------|
| **W8–9** | Wave 2 execution (Rehost + Replatform workloads) | Wave 2 live in target |
| **W10–11** | Wave 3 execution; Strangler Fig proxy deployed for monolith candidates; first microservice extracted and shipped | Wave 3 live; proxy routing 10–30% of monolith traffic to new service |
| **W12–13** | Wave 4 execution; 2nd and 3rd microservice extractions; mid-programme architecture review | Wave 4 live; monolith traffic share reduced to <70% |

---

### Phase 4 — Final Cutover, Optimisation & Decommission (Weeks 14–16)

**Goal:** Complete all remaining cutovers; right-size the target environment; decommission source infrastructure; hand over documentation.

| Week | Activity | Milestone |
|------|----------|-----------|
| **W14** | Final wave cutover (highest-complexity, highest-criticality workloads); extended parallel-run window (7 days); 24/7 monitoring during cutover | All workloads live in target |
| **W15** | Post-migration right-sizing: 2-week usage sample from CloudWatch / Azure Monitor / Cloud Monitoring feeds into right-sizing recommendations; RI/CUD purchase recommendations produced; tagging and cost allocation validated in OpenCost | Right-sizing report; RI/CUD recommendations |
| **W16** | Source decommission: produce decommission checklist; client executes shutdowns and cancellations with AICloudStrategist on async call; access revocation; final architecture documentation | Source environment decommissioned; all AICloudStrategist credentials removed; final handover pack delivered |

---

## INR Pricing

Pricing is based on workload footprint. A "workload" is one independently deployable service, application tier, or VM group migrated together (e.g., a 3-tier web application counts as one workload; a standalone batch job counts as one).

| Tier | Footprint | Duration | Fixed Fee |
|------|-----------|----------|-----------|
| **Small** | Up to 20 workloads | 8 weeks | ₹9,00,000–₹12,00,000 |
| **Mid** | 21–50 workloads | 12 weeks | ₹14,00,000–₹18,00,000 |
| **Large** | 51–100 workloads | 16 weeks | ₹20,00,000–₹28,00,000 |

**Payment milestones:**

| Milestone | % of Total Fee | Trigger |
|-----------|---------------|---------|
| Engagement start | 25% | Signed SOW + access provisioned |
| Phase 1 gate | 20% | Wave plan signed off |
| Phase 2 gate | 20% | Wave 1 cutover stable 72 hours |
| Phase 3 completion | 20% | Final wave cutover live |
| Phase 4 handover | 15% | Decommission checklist complete, documentation delivered |

**Expenses:** Cloud costs during parallel-run (source + target running simultaneously) are borne by the client. AICloudStrategist provides a parallel-run cost estimate per wave before Phase 2 begins; typical parallel-run window is 72 hours per wave.

**Gain-share option (Mid and Large tiers):** For clients migrating from data centre to cloud, AICloudStrategist offers a reduced fixed fee (−20%) in exchange for a gain-share of 20% of verified net infrastructure cost reduction against the pre-migration on-premises TCO baseline, measured over 12 months. Requires client agreement to TCO baseline methodology before engagement start.

---

## Step-by-Step Implementation Guide

### Step 1: Portfolio Assessment Using the 7 Rs

Every workload receives a classification before anything moves:

| Strategy | Decision Criteria | Tooling |
|----------|------------------|---------|
| **Rehost** (Lift & Shift) | Stable workload, no code change required, time-sensitive migration | AWS MGN, Azure Migrate, GCP M4CE |
| **Relocate** | VMware-to-VMware (e.g., on-prem VMware → VMware Cloud on AWS) | VMware HCX, vMotion |
| **Replatform** | Minor OS/runtime/database upgrade yields meaningful managed-service benefit | AWS DMS, Database Migration Service (GCP), Azure DMS |
| **Refactor** | Workload is a bottleneck for scaling or deployment velocity; domain boundaries are clear | Strangler Fig pattern, API gateway proxy, Branch by Abstraction |
| **Repurchase** | Workload is commodity functionality better served by SaaS | SaaS vendor evaluation; data migration script |
| **Retain** | Compliance, latency, or licensing constraint makes migration uneconomic within 18 months | Document constraint; revisit at next review cycle |
| **Retire** | Workload has no active users or business function | Decommission immediately; recover cost |

### Step 2: Wave Planning

Waves are sequenced by risk, not by technical similarity. Wave 1 always contains the simplest, least business-critical Rehost candidates — used as a live rehearsal of the migration process. Subsequent waves increase in complexity. Refactor workloads are always last: they require the target platform to be stable and the team's operational muscle memory to be built.

Wave dependencies are mapped explicitly: a workload that calls another workload must migrate in the same wave or after the workload it depends on. Azure Migrate's wave planning module, GCP Migration Center's wave grouping, or a simple spreadsheet dependency graph suffices.

### Step 3: Pilot Migration (Wave 1)

Wave 1 is the migration process under controlled conditions. It produces: a validated cutover runbook, a measured replication lag profile, a DNS cutover SOP, and a rollback procedure that has been tested (not just written). Everything discovered in Wave 1 — access problems, firewall gaps, agent deployment issues, DNS TTL surprises — is fixed in the runbook before Wave 2 begins.

### Step 4: Wave Iteration

Waves 2–N reuse the Wave 1 runbook with workload-specific amendments. Each wave has a defined rollback trigger: if a P1 incident is not resolved within 4 hours post-cutover, the source workload is automatically reactivated (DNS re-pointed, load balancer target swapped back) while root cause is investigated. No wave is decommissioned until 72 hours of post-cutover stability.

For Strangler Fig decompositions, each extracted microservice follows the same stability gate before the next extraction begins. The proxy layer ensures the monolith remains the fallback at all times until the final service is extracted.

### Step 5: Cutover

Final cutover for each wave is scheduled during a low-traffic change window (Sunday 01:00–05:00 IST by default, adjusted for client traffic patterns). All stakeholders are on a shared video call. Pre-cutover checklist is run line-by-line. DNS TTLs are pre-reduced to 60 seconds 48 hours before cutover. The source is kept live (read-only after write stop) for 72 hours post-cutover.

### Step 6: Decommission

Source infrastructure is decommissioned only after:
1. Target has been stable for ≥72 hours post-cutover.
2. Client engineering lead has signed the stability confirmation.
3. All application-level smoke tests pass against the target endpoint.
4. Monitoring shows no anomalous error rates against the 14-day pre-migration baseline.

Decommission is executed by the client with AICloudStrategist on an async call. AICloudStrategist does not hold client billing credentials and cannot decommission source infrastructure unilaterally.

---

## Deliverables

| Deliverable | Format | Delivered |
|-------------|--------|-----------|
| 7 Rs classification matrix | Google Sheet / Excel | Phase 1 gate |
| Application dependency map | draw.io / Structurizr C4 | Phase 1 gate |
| Migration wave plan | Markdown doc + RAID log | Phase 1 gate |
| Target landing zone (IaC) | Terraform/OpenTofu modules in client Git repo | Phase 2 |
| Per-wave cutover runbook | Markdown, version-controlled | Before each wave |
| Replication lag monitoring dashboard | Grafana / CloudWatch Dashboard | Phase 2 |
| Post-migration right-sizing report | PDF + spreadsheet | Phase 4 |
| RI/CUD purchase recommendation | PDF | Phase 4 |
| Final architecture documentation | Confluence / Notion / Markdown | Phase 4 handover |
| Decommission checklist (signed) | PDF | Phase 4 |
| Access revocation confirmation | Written record | Phase 4 |

---

## Tooling

| Category | Tool | Notes |
|----------|------|-------|
| **VM replication (AWS)** | AWS Application Migration Service (MGN) | Successor to CloudEndure Migration; block-level continuous replication; agent-based; cross-region and cross-cloud capable |
| **VM replication (Azure)** | Azure Migrate (Server Migration) | Agentless VMware discovery; integrated with Azure Arc for hybrid scenarios; 2026: Copilot Migration Agent for AI-assisted wave planning |
| **VM replication (GCP)** | GCP Migrate to Virtual Machines (M4CE) | Live migration and cold migration; Test-Clone feature for pre-cutover validation without affecting source |
| **Database migration** | AWS DMS, Azure DMS, GCP Database Migration Service | CDC (Change Data Capture) for near-zero-downtime migrations; schema conversion tools for heterogeneous migrations |
| **Infrastructure as Code** | Terraform / OpenTofu | All target infrastructure deployed as code; Infracost for pre-merge cost deltas on every PR |
| **API proxy (Strangler Fig)** | Kong Gateway / AWS API Gateway / Nginx | Proxy layer deployed in front of monolith on Day 1 of Refactor engagements; traffic shifting via weighted routing |
| **Dependency mapping** | Xtract.io / AWS Application Discovery Service / Azure Migrate dependency analysis | Network flow + agent-based dependency discovery |
| **Cost tracking** | OpenCost, Infracost | Post-migration cost allocation; pre-PR cost delta visibility |
| **Monitoring** | Prometheus + Grafana + Loki (LGTM stack) | Replication lag dashboards; post-cutover stability monitoring |

---

## Out of Scope

- **Network circuit provisioning** — AWS Direct Connect, Azure ExpressRoute, or GCP Interconnect order and negotiation is client-owned; AICloudStrategist configures the virtual gateway once the circuit is live.
- **Application code changes** (except Refactor workstreams, where code changes are explicitly in scope per workstream agreement)
- **Licensing negotiation** — Microsoft BYOL, Oracle licensing compliance on cloud, SAP HANA licensing; AICloudStrategist flags licensing risks but does not negotiate vendor contracts.
- **Data centre contract termination** — lease negotiations, colocation exit fees, hardware disposal.
- **Security incident response** — if an active breach is discovered in the source environment during the engagement, AICloudStrategist assists in scoping but formal IR is a separate engagement.
- **Post-migration managed operations** — 24/7 on-call support after handover; available as a separate Managed Retainer engagement.
- **Hyperscaler procurement programmes** — AWS MAP credit applications, Azure AMPP, or GCP MAP; AICloudStrategist assists with documentation but client must apply directly.

---

## Risk Management Framework

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Undiscovered application dependency breaks post-cutover | Medium | High | Dependency mapping in Phase 1; 72-hour parallel-run window; tested rollback on DNS and load balancer |
| Replication lag exceeds acceptable threshold at cutover | Medium | Medium | Replication lag monitoring dashboard active from Phase 2; cutover blocked if lag >5 minutes at T−1 hour |
| Licensing compliance violation in target (Oracle, Windows, SQL Server) | Medium | High | Licensing audit in Phase 1 classification; BYOL analysis for all commercial workloads before Phase 2 |
| Parallel-run costs exceed estimate | Low | Medium | Per-wave parallel-run cost estimate produced before Phase 2; 72-hour window cap enforced; client approval required to extend |
| Monolith decomposition scope creep (Strangler Fig) | High | Medium | Each extracted service has a fixed, agreed scope before extraction begins; no scope changes mid-wave |
| DNS TTL propagation delay causes extended downtime at cutover | Low | High | TTL pre-reduced to 60 seconds 48 hours before cutover; post-cutover monitoring checks both old and new endpoints for 30 minutes |
| Client-side change freeze blocks cutover window | Medium | Low | Change windows agreed 2 weeks in advance; one reschedule without cost; second reschedule at day-rate |
| Source decommission before target stability confirmed | Low | High | Source decommissioned only after written stability sign-off from client engineering lead; AICloudStrategist does not hold source billing credentials |

**Escalation threshold:** Any P1 incident (complete service unavailability) post-cutover triggers automatic rollback if not resolved within 4 hours. Wave decommission is deferred pending root-cause analysis. Client is notified within 15 minutes of any P1 trigger.

---

## Frequently Scoped Additions

These items are commonly added to the base engagement scope after Phase 1 assessment. Each is fixed-fee and priced independently:

| Add-on | Description | Indicative Fee |
|--------|-------------|----------------|
| **Disaster Recovery design** | Active-passive DR site in secondary cloud region; RTO/RPO targets defined; runbook tested | ₹2,00,000–₹3,00,000 |
| **Kubernetes platform migration** | Containerise 3–5 Replatform workloads during migration; deploy to EKS/AKS/GKE | ₹2,50,000–₹4,00,000 |
| **CI/CD pipeline rebuild** | GitOps pipelines (ArgoCD/Flux) for all migrated workloads in target environment | ₹1,50,000 |
| **Observability wiring** | LGTM stack deployed in target; migrated services instrumented with OTel; SLOs defined | ₹1,00,000–₹2,00,000 |
| **FinOps baseline** | OpenCost deployment, tagging enforcement, Reserved Instance / CUD modelling for target environment | ₹75,000 |

---

## References & Frameworks Applied

This engagement is grounded in the following public frameworks and practitioner literature:

- **AWS Migration Acceleration Program (MAP)** — Assess → Mobilize → Migrate & Modernize three-phase framework; AWS Well-Architected Migration Lens
- **AWS Application Migration Service (MGN)** documentation — block-level continuous replication, cutover workflow, test instances
- **Azure Migrate** — wave planning, agentless VMware discovery, Azure Copilot Migration Agent (March 2026)
- **GCP Migration Center** — wave grouping, M4CE live/cold/offline migration modes
- **The 7 Rs of Cloud Migration** — originally Gartner 5 Rs (2010); expanded to 7 Rs by AWS; applied per workload in Phase 1 classification
- **Martin Fowler** — *StranglerFigApplication* (martinfowler.com/bliki/StranglerFigApplication.html); façade-based incremental migration away from monoliths
- **Sam Newman** — *Monolith to Microservices* (O'Reilly, 2019); Branch by Abstraction pattern; Anticorruption Layer; incremental extraction over big-bang rewrites
- **TOGAF Cloud Migration Patterns** — Architecture Vision, Migration Planning, and Transition Architecture phases
- **Gartner** — *3 Journeys for Migrating a Data Center to Cloud IaaS*; hybrid infrastructure forecast to 2027

---

*AICloudStrategist is a founder-led cloud advisory based in Rohini, Delhi. All migration execution is delivered directly by the founding team. No offshore subcontracting. No junior engineer handoffs. No cutover proceeds without a tested rollback procedure.*

*For enquiries: connect via LinkedIn or the contact form at aicloudstrategist.com*
