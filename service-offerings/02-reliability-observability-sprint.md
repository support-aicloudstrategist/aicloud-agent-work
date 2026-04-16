# Reliability & Observability Sprint

**Service 2 of 9 — AICloudStrategist**
**Fixed Price: ₹1,00,000–₹2,00,000 | Duration: 3 weeks**

---

## Overview

Your system is running. But when it breaks at 2 AM, how fast can you answer three questions: *what* broke, *why* it broke, and *who owns the fix*? Most teams without a structured observability baseline take hours to answer all three — haemorrhaging revenue and trust.

The Reliability & Observability Sprint installs the full LGTM stack (Loki · Grafana · Tempo · Mimir/Prometheus), instruments your services with OpenTelemetry, defines SLIs and SLOs tied to actual business outcomes, and puts runbooks in your engineers' hands before the next incident. You walk out with a production-grade observability platform — not a monitoring script and a prayer.

---

## Ideal Client Profile

| Signal | Detail |
|--------|--------|
| **Infrastructure** | Kubernetes or Docker Compose workloads on AWS / Azure / GCP / bare-metal |
| **Team size** | 3–30 engineers; no dedicated SRE function yet |
| **Pain** | Incidents resolved by intuition and log-grepping; MTTR > 45 minutes; alert fatigue from threshold-only monitors |
| **Readiness** | Git-based deployments, existing CI/CD pipeline, at least one environment (staging or prod) accessible for instrumentation |
| **Not a fit** | Single-tier PHP monolith with no plans to change; pure SaaS stack with no self-hosted components |

---

## 3-Week Delivery Plan

### Week 1 — Current-State Audit & Instrumentation Blueprint

| Day | Activity | Output |
|-----|----------|--------|
| **D1** | Stakeholder kick-off; collect architecture diagram, service inventory, existing alert rules, on-call roster | Shared workspace, access checklist |
| **D2** | Current-state observability audit: existing metrics coverage, log hygiene, tracing gaps, alert noise ratio | Audit findings spreadsheet |
| **D3** | Interview key engineers and on-call leads; map top-5 incident classes from last 6 months | Incident taxonomy doc |
| **D4** | Instrumentation plan: per-service OTel SDK selection, collector topology, sampling strategy | Instrumentation blueprint (reviewed async) |
| **D5** | SLI candidate workshop: identify user-facing flows, agree on latency / availability / error-rate SLIs for each | SLI shortlist, signed off by stakeholders |

### Week 2 — Instrumentation, Stack Deployment & SLO Definition

| Day | Activity | Output |
|-----|----------|--------|
| **D6–7** | Deploy LGTM stack (Prometheus + Grafana + Loki + Tempo + Alertmanager) via Helm or Docker Compose; configure Grafana Alloy as unified telemetry pipeline | Stack live in staging |
| **D8** | Instrument priority services with OpenTelemetry SDK (auto-instrumentation where supported, manual spans for critical paths); configure structured JSON logging | Services emitting traces, logs, metrics |
| **D9** | SLO definition session: translate SLI candidates into formal SLOs with targets, error budgets, and burn-rate thresholds (1h fast-burn / 6h slow-burn / 3d trend — per Nobl9 multi-window method) | SLO spec document |
| **D10** | Alert routing design: severity tiers (P1–P3), escalation paths, PagerDuty / Opsgenie / Slack integration; silence windows; inhibition rules | Alert routing matrix |

### Week 3 — Dashboards, Alerts, Runbooks & Handover

| Day | Activity | Output |
|-----|----------|--------|
| **D11–12** | Build Grafana dashboards: (1) Executive SLO health board, (2) Service RED board (Rate / Errors / Duration), (3) Infrastructure saturation board, (4) Distributed trace explorer | 4 production dashboards, JSON exported |
| **D13** | Write runbooks for top-5 incident classes identified in Week 1; include decision trees, rollback steps, escalation contacts | 5 runbooks in Confluence / Notion / Git repo |
| **D14** | Alertmanager rules deployed to production; end-to-end fire drill: trigger synthetic incident, walk team through alert → trace → log → runbook flow | Fire drill recording + sign-off |
| **D15** | Handover session: architecture walkthrough, dashboard tour, runbook walkthrough; MTTR-reduction roadmap for next 90 days | Roadmap doc, recorded session |

---

## INR Pricing

| Tier | Price | Scope |
|------|-------|-------|
| **Starter** | ₹1,00,000 | Up to 5 services, 1 environment (staging or prod), OTel instrumentation, 2 dashboards, 3 runbooks |
| **Standard** | ₹1,50,000 | Up to 10 services, 2 environments, full LGTM stack, 4 dashboards, 5 runbooks, fire drill |
| **Growth** | ₹2,00,000 | Up to 20 services, multi-environment, Grafana Alloy pipeline, 6 dashboards, 5 runbooks, 90-day roadmap, 2 post-delivery check-in calls |

**Pricing rationale:** Engagement spans 15 consultant-days of skilled SRE work — instrumentation, architecture, facilitation, and documentation. The floor covers a lean single-environment engagement; the ceiling reflects multi-service complexity and the full delivery asset set. Both tiers are below the annual cost of one junior SRE hire. Optional gain-share model available: fixed retainer credit applied against measurable MTTR improvement milestones.

---

## Step-by-Step Implementation Guide

### Phase 1 — Current-State Audit

1. **Access provisioning:** Read-only access to AWS CloudWatch / Azure Monitor / GCP Logging (if in use), existing Prometheus/Grafana instances, CI/CD pipeline, git repos.
2. **Alert noise audit:** Export last 30 days of alerts; calculate alert-to-action ratio. Anything below 30% actionability is topping the fix list.
3. **Log hygiene check:** Sample 500 log lines per service. Score on: structured vs. unstructured, correlation IDs present, log level discipline, PII exposure risk.
4. **Trace coverage map:** Identify which services emit spans; flag cross-service calls missing propagated trace context.
5. **Incident post-mortem review:** Read last 5 post-mortems (or reconstruct from Slack/Jira). Identify recurring MTTR bottlenecks: detection lag, investigation time, escalation friction.
6. **Output:** Findings matrix scored Red / Amber / Green per domain. Prioritised fix list fed into Week 2.

### Phase 2 — Instrumentation Plan

1. **Service inventory:** List all services with language runtime, framework, deployment mechanism, and current telemetry status.
2. **OTel SDK selection:** Java/Python/Node services → auto-instrumentation agents. Go/Rust → manual SDK. Batch jobs → OTLP export at job completion.
3. **Collector topology:** Deploy OpenTelemetry Collector as a DaemonSet (Kubernetes) or sidecar (Docker Compose). Configure pipelines: receivers (OTLP gRPC/HTTP), processors (batch, memory_limiter, resource detection), exporters (Prometheus remote-write, Loki push, Tempo OTLP).
4. **Sampling strategy:** Head-based sampling at 10–20% for high-volume services; tail-based sampling via OTel Collector for error / slow-request capture. Adjust per error budget burn rate.
5. **Structured logging standard:** Mandate JSON log format; required fields: `timestamp`, `level`, `service`, `trace_id`, `span_id`, `message`. Enforce via linter in CI.
6. **Correlation IDs:** Ensure W3C TraceContext headers propagated across all HTTP/gRPC calls; validate via synthetic request through full call chain.

### Phase 3 — SLI / SLO Definition

1. **Identify user journeys:** Map top 3–5 critical user flows (login, checkout, data export, etc.).
2. **SLI candidates per journey:** Availability (success ratio = good requests / total requests), latency (p95 < threshold), error rate, freshness (for data pipelines).
3. **SLO target-setting:** Start conservative — Google SRE recommends beginning at 99% and tightening only after measuring actual baseline. Never set SLO above historical performance without a reliability investment.
4. **Error budget calculation:** `Error budget = (1 - SLO target) × request volume`. Make error budget visible to product and engineering — it is the shared currency for reliability vs. velocity trade-offs.
5. **Burn-rate alerting (multi-window, per Nobl9 guidance):**
   - Fast burn: 1h window, burn rate > 14× → page immediately (P1)
   - Slow burn: 6h window, burn rate > 6× → ticket + Slack (P2)
   - Trend: 3-day window, burn rate > 1× → weekly review agenda item
6. **SLO document format:** Service name · SLI definition · data source (Prometheus query) · SLO target · error budget period · owner · review cadence.

### Phase 4 — Dashboard Build

**Dashboard 1 — Executive SLO Health**
- SLO compliance % per service (last 30 days)
- Error budget remaining (burn gauge)
- Incident count and MTTR trend

**Dashboard 2 — Service RED Board**
- Request Rate (RPS) by service and endpoint
- Error Rate (% 5xx / error responses)
- Duration (p50 / p95 / p99 latency)
- Powered by Prometheus + Grafana; auto-linked to Tempo traces on data-point click

**Dashboard 3 — Infrastructure Saturation**
- CPU / memory / disk saturation per node and pod
- Network I/O, pod restart counts
- Alertmanager alert state panel

**Dashboard 4 — Distributed Trace Explorer**
- Grafana Tempo data source; trace search by service, operation, duration, status
- Linked from RED board latency spikes for one-click drill-down
- Service dependency map (Grafana service graph plugin)

All dashboards exported as versioned JSON; stored in git repo under `dashboards/`.

### Phase 5 — Alert Routing

1. **Severity tiers:**
   - P1: SLO fast-burn breach, full outage → PagerDuty immediate page
   - P2: SLO slow-burn, degraded performance → Slack `#incidents` + ticket
   - P3: Infrastructure saturation warnings → Slack `#ops-alerts` (business hours)
2. **Alertmanager routing tree:** group by `(alertname, service)`, 5-minute group wait, 1-hour repeat interval. Inhibit P2/P3 when P1 active for same service.
3. **Silence management:** Maintenance windows pre-registered; silence expiry enforced (no indefinite silences).
4. **Receiver configuration:** Separate receiver per team/squad with ownership matrix. On-call rotation synced from PagerDuty schedule.
5. **Dead-man's switch:** Watchdog alert ensures the alerting pipeline itself is monitored; alerts if no heartbeat received in 5 minutes.

### Phase 6 — Runbook Templates

Each runbook follows a standard structure:

```
# [Incident Class Name]

## Alert fired
<Alertmanager rule name and condition>

## Impact
<User-facing impact description>

## Severity
P1 / P2 / P3

## Initial triage (< 5 min)
1. Check SLO dashboard: [link]
2. Open trace explorer: [link]
3. Check recent deployments: `kubectl rollout history`

## Diagnosis decision tree
- If error rate spike + recent deploy → rollback (see step A)
- If latency spike, no deploy → check DB slow query log (see step B)
- If availability drop, infra saturation → check node resources (see step C)

## Remediation steps
### Step A — Rollback
### Step B — DB investigation
### Step C — Scale-out

## Escalation
If unresolved in 30 min → page [Name], [contact]

## Post-incident
Link to post-mortem template: [link]
Last reviewed: YYYY-MM-DD | Owner: [team]
```

Top-5 incident classes covered: service latency spike, error rate surge, pod OOMKill, external dependency failure, certificate / auth expiry.

---

## Deliverables

| # | Deliverable | Format |
|---|-------------|--------|
| 1 | Observability audit report | PDF + spreadsheet |
| 2 | Instrumentation blueprint | Markdown in git |
| 3 | OTel Collector config (Helm values / Docker Compose) | YAML in git |
| 4 | SLO specification document | Markdown / Notion |
| 5 | Prometheus alert rules | YAML in git |
| 6 | Alertmanager routing config | YAML in git |
| 7 | 4 Grafana dashboards (JSON, versioned) | Git + imported to Grafana |
| 8 | 5 incident runbooks | Confluence / Notion / Git |
| 9 | MTTR-reduction roadmap (90-day) | PDF |
| 10 | Fire drill recording + sign-off document | MP4 + PDF |
| 11 | Handover session recording | MP4 |

All code artifacts delivered via pull request to client's repository with inline documentation.

---

## Tooling Stack

| Layer | Tool | Role |
|-------|------|------|
| **Instrumentation** | OpenTelemetry SDK + Collector | Vendor-neutral telemetry collection; auto + manual instrumentation |
| **Telemetry pipeline** | Grafana Alloy | Unified collection of metrics, logs, traces, profiling |
| **Metrics** | Prometheus | Time-series metrics store; PromQL alerting |
| **Logs** | Loki | Label-indexed log aggregation (lighter and cheaper than Elasticsearch) |
| **Traces** | Tempo | Distributed trace backend; no indexing cost |
| **Dashboards** | Grafana | Unified visualisation; correlates all three telemetry types |
| **Alerting** | Alertmanager | Routing, grouping, silencing, inhibition |
| **SLO tracking** | Grafana SLO plugin / Sloth | Error budget dashboards, burn-rate rules generation |
| **Incident routing** | PagerDuty / Opsgenie | On-call scheduling, escalation policies |
| **Runbooks** | Git / Confluence / Notion | Version-controlled, linked from alert annotations |

All primary tools are open-source with no per-seat licensing cost. Grafana Cloud free tier sufficient for teams < 10k series / 50GB logs.

---

## Explicit Out of Scope

- Application code refactoring or bug fixing
- Building new CI/CD pipelines (instrumentation hooks only)
- Ongoing alert management or 24/7 on-call coverage
- Custom OpenTelemetry Collector plugins or proprietary exporters
- Security information and event management (SIEM) — see Service 3: Cloud Security Posture Review
- FinOps cost tagging or budget alerts — see Service 1: FinOps QuickStart
- SaaS tools with no self-hosted telemetry data (Shopify, Salesforce, etc.)
- Performance load testing or chaos engineering exercises
- Post-delivery SLO reviews or runbook updates (available via Managed FinOps Retainer or bespoke SOW)

---

## Why This Matters: The Business Case

**MTTR is a revenue metric.** An e-commerce platform at ₹10 lakh/hour revenue losing 2 hours to a fumbled incident loses ₹20 lakh — more than the cost of this entire sprint. Top-performing engineering organisations in the 2025 DORA Report achieved MTTRs under 7 minutes by combining distributed tracing, automated alerting, and pre-written runbooks — exactly what this sprint delivers.

**Error budgets align product and engineering.** Without a visible error budget, every reliability investment is a political fight. With one, teams make data-driven decisions: spend budget on velocity or invest in reliability.

**OpenTelemetry is the industry standard.** As of 2026, OpenTelemetry is the second-highest-velocity CNCF project (after Kubernetes). Instrumenting once with OTel preserves optionality — switch backends without re-instrumenting.

---

## References

- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Google SRE Workbook: Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [Google Cloud: SRE Fundamentals — SLIs, SLOs, SLAs](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos)
- [OpenTelemetry: LGTM Stack Integration (2026)](https://oneuptime.com/blog/post/2026-02-06-lgtm-stack-opentelemetry/view)
- [Grafana Labs: Cloud-Native Observability Stack 2026](https://johal.in/cloud-native-observability-stack-prometheus-grafana-loki-and-tempo-integration-for-full-stack-monitoring-2026-3/)
- [Honeycomb: Observability and the DORA Metrics](https://www.honeycomb.io/blog/observability-dora-metrics)
- [Honeycomb: What the 2025 DORA Report Teaches Us About Observability](https://www.honeycomb.io/blog/what-2025-dora-report-teaches-us-about-observability-platform-quality)
- [Nobl9: SLO Best Practices](https://www.nobl9.com/service-level-objectives/slo-best-practices)
- [Nobl9: Multi-Burn Rate Alerting](https://docs.nobl9.com/slocademy/manage-slo/create-alerts/)
- [Nobl9: Runbook Best Practices](https://www.nobl9.com/it-incident-management/runbook-example)
- [CNCF: OpenTelemetry Unified Observability (2025)](https://www.cncf.io/blog/2025/11/27/from-chaos-to-clarity-how-opentelemetry-unified-observability-across-clouds/)
- [CNCF: Observability Trends 2025](https://www.cncf.io/blog/2025/03/05/observability-trends-in-2025-whats-driving-change/)
- [Datadog + AWS: Observability Maturity Model 2026](https://dev.to/aws-builders/datadog-aws-observability-maturity-model-2026-210m)

---

*AICloudStrategist · Fixed-price, outcome-driven cloud consulting for Indian SMBs and global engineering teams*
*Contact: [aicloudstrategist.com](https://aicloudstrategist.com)*
