---
title: "DevOps Maturity Self-Assessment"
subtitle: "A 12-question diagnostic based on DORA metrics · For Indian engineering leaders"
author: "AICloudStrategist · Anushka B, Founder"
date: "April 2026"
geometry: "margin=18mm"
fontsize: 11pt
papersize: a4
---

# DevOps Maturity Self-Assessment

*A 12-question diagnostic based on the DORA (DevOps Research & Assessment) framework. Designed to be completed in 15 minutes by a CTO, VP of Engineering, or Head of Platform in under an hour with input from one or two team leads.*

> Built by [AICloudStrategist](https://aicloudstrategist.com) · Founder-led. Enterprise-reviewed. · support@aicloudstrategist.com

---

## How to use this assessment

Answer each of the 12 questions honestly. Score your team against the four maturity tiers — Low, Medium, High, Elite — based on the DORA 2024 State of DevOps research. Calculate the aggregate tier at the end. The action plan section tells you what to do at each tier.

There is no prize for a high score you have not earned. The value of this document is honest assessment.

---

## Part 1 — The Four DORA Keys (Questions 1–4)

These four metrics are the single most validated measure of software delivery performance, across 33,000+ surveyed organisations over 10 years of research.

### Q1. Lead time for changes

*How long does it take from a developer committing code to that code running safely in production?*

| Score | Tier | Answer |
|---|---|---|
| 4 | Elite | Under 1 hour |
| 3 | High | Between 1 day and 1 week |
| 2 | Medium | Between 1 week and 1 month |
| 1 | Low | More than 1 month |

**Your score: _____**

### Q2. Deployment frequency

*How often does your organisation deploy code to production?*

| Score | Tier | Answer |
|---|---|---|
| 4 | Elite | On-demand, multiple times per day |
| 3 | High | Between once per day and once per week |
| 2 | Medium | Between once per week and once per month |
| 1 | Low | Less than once per month |

**Your score: _____**

### Q3. Change failure rate

*What percentage of deployments to production cause a degraded service, hotfix, or rollback?*

| Score | Tier | Answer |
|---|---|---|
| 4 | Elite | 0–15% |
| 3 | High | 16–30% |
| 2 | Medium | 16–30% |
| 1 | Low | Over 30% |

**Your score: _____**

### Q4. Mean time to recover (MTTR)

*When a production incident occurs, how long does it take on average to restore service?*

| Score | Tier | Answer |
|---|---|---|
| 4 | Elite | Under 1 hour |
| 3 | High | Under 1 day |
| 2 | Medium | 1 day to 1 week |
| 1 | Low | More than 1 week |

**Your score: _____**

---

## Part 2 — Enabling Practices (Questions 5–12)

These questions probe the practices that produce high DORA scores.

### Q5. Infrastructure as Code coverage

*What percentage of your production infrastructure is defined and provisioned through code (Terraform, OpenTofu, Pulumi, CloudFormation, ARM, Bicep)?*

| Score | Answer |
|---|---|
| 4 | 95–100% (every production resource is in IaC; manual changes are detected and rolled back automatically) |
| 3 | 70–95% (most resources in IaC; some drift tolerated) |
| 2 | 40–70% (some IaC, significant console / manual changes) |
| 1 | Under 40% (IaC is aspirational) |

**Your score: _____**

### Q6. Deployment automation

*How are production deployments executed?*

| Score | Answer |
|---|---|
| 4 | Fully automated on merge to main; no human button-click required |
| 3 | One-click deploy via CI/CD pipeline; rollback is one-click |
| 2 | Pipeline exists, but requires coordination, handholding, or specific people |
| 1 | SSH into a server, run a script, or manually copy files |

**Your score: _____**

### Q7. Test automation

*What percentage of changes are covered by automated tests that run before production deploy?*

| Score | Answer |
|---|---|
| 4 | Unit + integration + smoke tests run automatically; coverage >70%; flaky tests are a priority |
| 3 | Unit tests are automated and reliable; integration tests run but are sometimes skipped |
| 2 | Some unit tests; integration tests are manual; test flake is a known problem |
| 1 | Testing is manual, or automated tests exist but are routinely ignored |

**Your score: _____**

### Q8. Monitoring and observability

*Can your team answer these three questions during a production incident, within five minutes? (1) What broke? (2) Why did it break? (3) Who is on-call to fix it?*

| Score | Answer |
|---|---|
| 4 | All three, in under 2 minutes, via a single dashboard plus on-call rotation |
| 3 | All three, in under 10 minutes, across 2–3 tools |
| 2 | We can usually figure it out within 30 minutes with some log-grepping |
| 1 | Incidents start with "does anyone know what's going on?" in Slack |

**Your score: _____**

### Q9. Trunk-based development

*How does your team manage branches?*

| Score | Answer |
|---|---|
| 4 | Trunk-based: short-lived branches (<1 day), continuous integration to main, feature flags for unfinished work |
| 3 | Feature branches <3 days typical; main is always deployable |
| 2 | Feature branches >1 week; merge conflicts are common |
| 1 | Long-lived feature branches, release branches, merge wars, "integration week" |

**Your score: _____**

### Q10. Security in the pipeline (DevSecOps)

*How are security checks integrated into your delivery pipeline?*

| Score | Answer |
|---|---|
| 4 | SAST, SCA, secrets scanning, container scanning, IaC scanning (tfsec / Checkov) all run in CI; high-severity findings block merge |
| 3 | SAST + SCA running in CI; findings reviewed in PR |
| 2 | Periodic manual security reviews; no pipeline enforcement |
| 1 | Security is addressed post-incident or during audit season |

**Your score: _____**

### Q11. Documentation and runbooks

*When an engineer gets paged at 2am for a service they've never worked on, can they find a runbook that lets them resolve the common failure modes?*

| Score | Answer |
|---|---|
| 4 | Yes — every production service has a runbook, tested quarterly |
| 3 | Most services have runbooks; some are stale |
| 2 | Some services have runbooks; most rely on tribal knowledge |
| 1 | Runbooks are aspirational; on-call means "call the original engineer" |

**Your score: _____**

### Q12. Psychological safety and blameless culture

*When a production incident occurs caused by a team member's mistake, what happens?*

| Score | Answer |
|---|---|
| 4 | Blameless postmortem documents the systemic weakness; the individual is not named or singled out; action items focus on detection and prevention |
| 3 | Postmortems are blameless in principle; some uncomfortable moments for individuals |
| 2 | Postmortems happen; blame is subtle but present |
| 1 | The person who caused the outage is talked about for weeks |

**Your score: _____**

---

## Scoring

**Total score: _____ / 48**

| Score Range | Maturity Tier |
|---|---|
| 40–48 | **Elite** — You are in the top 18% of software organisations (DORA 2024). |
| 30–39 | **High** — Strong practices. Focused improvement in 2–3 areas closes the gap to Elite. |
| 18–29 | **Medium** — Solid foundations. Several high-leverage improvements available. |
| 12–17 | **Low** — Delivery is happening but it is slow, risky, and dependent on heroics. |

---

## What to do at each tier

### If you are Low (12–17)

You have a delivery problem, and it is costing the business more than you think. Common symptoms:

- Releases are scary events requiring senior engineers
- New hires take 4+ weeks to deploy their first production change
- "We can't ship on Fridays" is a cultural norm
- Most production incidents are resolved by the engineer who wrote the code

The single highest-leverage move: **invest in a 3–4 week DevOps sprint focused on CI/CD automation, IaC governance, and one live rollback rehearsal**. Expected outcome: tier movement from Low to Medium within 60 days, measurable in DORA metrics.

### If you are Medium (18–29)

You have the basics. The next tier of maturity requires investment in enabling practices, not just tooling:

- Improve test automation coverage and reliability
- Adopt trunk-based development if still on long-lived branches
- Install proper observability (OpenTelemetry + LGTM stack) and define SLOs
- Policy-as-code in the pipeline (OPA Gatekeeper, Checkov, tfsec)

### If you are High (30–39)

You are doing most things right. The gap to Elite is usually in:

- Elite deployment frequency (multiple per day) requires feature flags and progressive rollout
- Elite MTTR (under 1 hour) requires automated rollback and observability-driven remediation
- Elite lead time (under 1 hour) requires aggressive CI optimisation (parallelism, caching, test sharding)

### If you are Elite (40–48)

You are in the top 18% globally. Your challenge is maintaining the standard as you scale: preserving deployment velocity through a period of team growth, maintaining SLO discipline under feature pressure, and ensuring that organic growth does not silently erode the enabling practices.

---

## How we can help

**AICloudStrategist's DevOps & Platform Engineering service** (Service 09) is a 3–4 week engagement that targets measurable DORA tier movement.

We audit your current DORA baseline, design the target platform, and ship working CI/CD, GitOps, IaC module library, policy-as-code, release dashboard, and enablement sessions — aligned to the specific gaps this assessment surfaced in your answers.

Fixed price ₹1.5L–₹3.5L depending on scope. DORA-linked gain-share option available.

**Start with a free 30-minute Cloud Cost Health Check** or email support@aicloudstrategist.com with your DORA scores and we will reply with a scoped suggestion within 24 hours.

**[aicloudstrategist.com/book.html](https://aicloudstrategist.com/book.html)**

---

## References

- DORA (DevOps Research & Assessment): https://dora.dev/research/
- Accelerate: The Science of Lean Software and DevOps — Nicole Forsgren, Jez Humble, Gene Kim (IT Revolution, 2018)
- Team Topologies — Matthew Skelton & Manuel Pais: https://teamtopologies.com/
- Google Cloud — Four Keys: https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance

---

*AICloudStrategist · Anushka B, Founder · Rohini, Delhi 110085 · support@aicloudstrategist.com*
*Founder-led. Enterprise-reviewed.*

— Anushka B, Founder · AICloudStrategist
