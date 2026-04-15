# Cloud Security Posture Review

**Service 3 of 6 — AICloudStrategist**
**Fixed Price: ₹2,50,000–₹5,00,000 | Duration: 2 weeks**

---

## Overview

Most organisations running workloads in AWS, Azure, or GCP have never had a systematic answer to the question: *how exposed are we, right now?* Engineers provision resources under delivery pressure. Configurations drift. IAM permissions accumulate. S3 buckets get misconfigured. Default security groups stay open. Nobody notices until a breach, a compliance audit, or a penetration test surfaces a two-year-old finding that was always hiding in plain sight.

The Cloud Security Posture Review is a structured, read-only diagnostic engagement that gives Indian SMBs and mid-market technology companies a complete, ranked picture of their cloud security exposure — aligned to CIS Benchmarks v8, the AWS Well-Architected Security Pillar, Microsoft Cloud Security Benchmark, NIST CSF 2.0, and the OWASP Cloud-Native Application Security Top 10. The engagement is entirely non-destructive: no changes are made to the client's environment without explicit approval.

At the end of two weeks, the client holds a prioritised remediation backlog with effort estimates, a boardroom-ready executive summary, and a DPDP Act 2023 / DPDP Rules 2025 gap assessment — all produced using open-source tooling with zero ongoing licence fees.

> **Positioning:** Founder-led delivery by Anushka B (7+ years in cloud/DevOps/automation), with senior architect oversight carrying 22+ years of Fortune 500 security and infrastructure experience. Findings are reviewed by a human who has seen real breaches — not just a CSPM dashboard alert.

---

## Ideal Client Profile

| Signal | Typical Pattern |
|---|---|
| **Cloud footprint** | AWS, Azure, GCP (single or multi-cloud); 20–500 cloud resources in scope |
| **Spend range** | Monthly cloud bill INR 3 lakh – 50 lakh+ |
| **Security maturity** | No formal CSPM practice; security reviews are ad hoc or done as part of a penetration test |
| **Compliance pressure** | Preparing for ISO 27001, SOC 2, RBI/SEBI IT guidelines, or DPDP Act 2023 compliance |
| **IAM hygiene** | Root account or equivalent used operationally; no MFA enforcement; unused service accounts accumulating |
| **Incident history** | One or more cloud misconfigurations discovered by external parties (pen testers, bug hunters, auditors) |
| **Data classification** | Personal data or sensitive customer data stored in cloud with no formal access controls review |
| **Regulatory sector** | BFSI, healthtech, edtech, SaaS serving Indian consumers — all face DPDP Act obligations |

**Who this is not for:** Organisations with an active SOC or a dedicated cloud security team running continuous CSPM tooling (they need a different engagement). Companies in the middle of a major cloud migration (wait until the target architecture stabilises). Pure on-premises environments.

---

## 2-Week Delivery Plan

### Week 1 — Access, Automated Scanning, and Triage

| Day | Activity | Output |
|-----|----------|--------|
| **D1** | Kick-off call: define scope (accounts, subscriptions, projects, regions), agree on read-only access provisioning method, collect architecture context, data classification inventory | Signed scope document, access checklist |
| **D2** | Provision read-only audit roles: AWS Security Audit IAM policy, Azure Security Reader + Entra Reader, GCP Viewer role — via CloudFormation StackSet / Bicep / Terraform (read-only) | Access verified, no production changes |
| **D3** | Execute automated CSPM scan: Prowler (AWS primary, 584 checks, CIS v3.0, NIST CSF 2.0 mappings), Cloud Custodian policy runs, AWS Security Hub aggregated findings pull, Azure Defender for Cloud secure score export, GCP Security Command Center (SCC) export | Raw findings JSON + CSV, ~2,000–10,000 raw checks |
| **D4** | De-duplicate, normalise, and triage raw findings: false-positive suppression, severity re-scoring using business context (internet-facing vs. internal, data sensitivity, blast radius), tag unresolvable waivers | Normalised findings register (Google Sheet / Excel) |
| **D5** | Select top-10 highest-risk findings for manual deep-dive; brief client security lead on preliminary findings; schedule D6–D9 technical sessions | Preliminary findings briefing, deep-dive agenda |

### Week 2 — Manual Deep-Dive, Remediation Planning, and Reporting

| Day | Activity | Output |
|-----|----------|--------|
| **D6** | Manual review of IAM posture: cross-account trust policies, overly permissive roles, unused credentials, service account key age, MFA enforcement, privilege escalation paths | IAM risk inventory |
| **D7** | Manual review of network exposure: security groups and NACLs with 0.0.0.0/0, publicly exposed storage (S3 public-access block, Azure Blob public access, GCS uniform bucket-level access), exposed management ports (22/3389), VPC peering and Transit Gateway exposure | Network exposure map |
| **D8** | Manual review of data protection: encryption-at-rest coverage (EBS, RDS, S3, Azure Disk, GCS), KMS/CMK vs. provider-managed key usage, secrets stored in environment variables or parameter store plaintext, CloudTrail / Azure Monitor / GCP Audit Logs completeness | Data protection gap list |
| **D9** | DPDP Act 2023 and DPDP Rules 2025 overlay: map findings to Section 8 (reasonable security safeguards), breach notification obligations, Significant Data Fiduciary (SDF) applicability; identify personal data stores lacking encryption or access controls | DPDP gap register |
| **D10** | Report writing, boardroom-ready executive summary, client review call, handover | Full report + executive summary delivered |

---

## INR Pricing and Rationale

| Tier | Scope | Price (INR) |
|------|-------|-------------|
| **Essential** | Single cloud (AWS or Azure or GCP), up to 2 accounts/subscriptions, up to 150 resources | ₹2,50,000 |
| **Standard** | Single cloud, up to 5 accounts/subscriptions, up to 400 resources | ₹3,75,000 |
| **Multi-Cloud** | Two or three clouds (AWS + Azure, AWS + GCP, or all three), up to 10 accounts total | ₹5,00,000 |

**What justifies this pricing:**

Commercial CSPM platforms (Wiz, Orca Security, Prisma Cloud) start at USD 30,000–50,000 per year for a licence alone — roughly INR 25–42 lakh annually — and require internal staff to action findings. The AICloudStrategist engagement delivers the complete scan-to-remediation-backlog workflow for a one-time fixed fee, with zero ongoing licence cost, using open-source tooling the client retains.

An undetected S3 misconfiguration, open RDP port, or unencrypted PII database carries remediation costs and regulatory penalties that far exceed the engagement fee. Under DPDP Rules 2025, failure to maintain reasonable security safeguards attracts penalties up to ₹250 crore.

Engagements are priced on scope (accounts, resources, clouds) — not on findings count. Complex Kubernetes or serverless-heavy workloads may require a scoping call before final pricing.

---

## Step-by-Step Implementation Guide

### Phase 1 — Read-Only Access Provisioning

**AWS:** Create a CloudFormation stack deploying an IAM role named `AICSTAuditRole` with the AWS-managed `SecurityAudit` policy and an optional `ReadOnlyAccess` policy attached. Cross-account trust policy restricts assumption to the AICloudStrategist audit account. No console access required — CLI/API only. For multi-account environments, deploy via StackSets across the AWS Organisation.

**Azure:** Create a custom Reader + Security Reader role assignment scoped to the target subscription(s) using a Bicep template. Microsoft Entra ID (formerly Azure AD) Reader role assigned for identity analysis. No Owner or Contributor permissions used.

**GCP:** Grant `roles/viewer` and `roles/iam.securityReviewer` to the AICloudStrategist service account on each target project. Org-level binding used only if client consents; otherwise, project-level binding per in-scope project.

Access is revoked immediately after report delivery. Revocation procedure is documented in the scope agreement and executed on D10.

### Phase 2 — Automated CSPM Scan

Run **Prowler v4** for AWS (584 checks across CIS AWS Foundations v3.0, NIST CSF 2.0, AWS Well-Architected Security Pillar, PCI DSS 3.2.1, ISO 27001):

```bash
prowler aws --profile audit-profile \
  --compliance cis_aws_foundations_benchmark_3_0 \
  --output-formats json csv html \
  --output-directory ./prowler-output
```

Run **Cloud Custodian** policies for targeted checks not covered by Prowler (resource tagging, encryption-at-rest on specific resource types, lifecycle policies).

Pull **AWS Security Hub** aggregated findings via AWS CLI for any pre-existing CSPM findings.

Export **Azure Defender for Cloud** secure score and recommendations via `az security assessment list`.

Export **GCP Security Command Center** findings via `gcloud scc findings list`.

All scan output is stored locally; no client data is transmitted to third-party cloud services.

### Phase 3 — Manual Deep-Dive on Top 10 Findings

Automated scanners produce volume, not judgment. The manual deep-dive applies human review to the 10 highest-risk findings, validating:

- Exploitability in the client's specific architecture (internet-facing vs. VPC-internal)
- Actual data sensitivity of affected resources
- Presence of compensating controls that a scanner cannot detect
- Privilege escalation paths linking low-severity misconfigurations into a critical attack chain

Example: an S3 bucket with public-read enabled is P1 if it contains PII, waivable if it intentionally hosts a public website. A scanner cannot make that call. A human reviewer can.

### Phase 4 — Remediation Prioritisation

Findings are scored using a modified CVSS-influenced model:

| Score | Criteria | Typical Action |
|-------|----------|----------------|
| **Critical** | Internet-exposed, data at risk, exploitable without authentication | Fix within 24–48 hours |
| **High** | Significant exposure with potential data loss or lateral movement | Fix within 1–2 weeks |
| **Medium** | Configuration drift from best practice, low immediate impact | Fix within 30 days |
| **Low / Informational** | Hardening recommendation, defence-in-depth improvement | Fix within 90 days or accept with waiver |

The remediation backlog is delivered as a prioritised spreadsheet with: finding ID, affected resource ARN/ID, severity, recommended fix, estimated engineer effort (hours), Terraform/CLI remediation snippet where applicable, and DPDP Act mapping where relevant.

### Phase 5 — Report and Boardroom-Ready Summary

The full technical report covers all findings, evidence screenshots, tool output references, and remediation steps.

The boardroom executive summary (3–5 slides or pages) presents:
- Overall security posture score (% of CIS checks passing)
- Top 5 risks in plain language with business impact
- DPDP Act 2023 readiness status
- Recommended 30/60/90-day remediation roadmap
- Investment vs. risk-reduction narrative

---

## Deliverables

1. **Scope agreement and access provisioning guide** (Day 1)
2. **Normalised findings register** — all automated scan findings, de-duplicated, severity-scored, business-context annotated (Day 4)
3. **Top-10 manual deep-dive findings** — detailed write-up per finding with evidence, attack narrative, and recommended fix (Day 9)
4. **DPDP Act 2023 / DPDP Rules 2025 gap register** — findings mapped to statutory obligations, penalty exposure quantified (Day 9)
5. **Full technical security report** — all findings, tooling methodology, raw evidence, remediation guidance, effort estimates (Day 10)
6. **Boardroom executive summary** — 3–5 page/slide non-technical summary with risk narrative and remediation roadmap (Day 10)
7. **Remediation backlog spreadsheet** — prioritised, effort-estimated, with Terraform/CLI snippets (Day 10)
8. **Access revocation confirmation** — written confirmation of audit role removal post-engagement (Day 10)

---

## Tooling Stack

| Tool | Purpose | Licence |
|------|---------|---------|
| **Prowler v4** | Primary CSPM engine; 584 AWS checks, Azure and GCP support; CIS, NIST CSF 2.0, ISO 27001 mappings | Apache 2.0 / Open Source |
| **AWS Security Hub** | Aggregated findings from GuardDuty, Inspector, Macie; CSPM baseline | AWS-native (client pays data volume) |
| **Microsoft Defender for Cloud** | Azure secure score, CSPM recommendations, regulatory compliance dashboard | Azure-native (Free/Standard tier) |
| **GCP Security Command Center (SCC)** | GCP-native misconfiguration and threat detection | GCP-native (Standard free, Premium billed) |
| **Cloud Custodian** | Policy-as-code for targeted checks, gap-fill from Prowler | Apache 2.0 / Open Source |
| **Steampipe** | SQL-based cloud asset inventory and compliance query engine | AGPLv3 / Open Source |
| **ScoutSuite** | Supplementary multi-cloud audit (note: last updated May 2024; used for legacy checks only) | GPL-2.0 / Open Source |
| **Trivy** | Container image and IaC (Terraform, CloudFormation) misconfiguration scanning | Apache 2.0 / Open Source |
| **Checkov** | Static analysis of Terraform, CloudFormation, Kubernetes YAML | Apache 2.0 / Open Source |

No commercial CSPM licences are required. All tooling remains available to the client post-engagement.

---

## Out of Scope

- Penetration testing or active exploitation attempts
- Code-level application security review (covered by separate service)
- Kubernetes cluster runtime security (covered by separate service)
- Remediation implementation (available as a follow-on Implementation Sprint)
- On-premises or data centre infrastructure
- Third-party SaaS application security (Salesforce, Workday, etc.)
- Network penetration testing or physical security
- Changes to any client systems during the engagement

---

## DPDP Compliance Angle for Indian Clients

The Digital Personal Data Protection Act 2023 and the DPDP Rules 2025 (notified November 2025, with most substantive provisions effective May 2027) impose direct obligations on any organisation processing personal data of Indian data principals — including cloud-hosted databases, analytics pipelines, customer-facing applications, and data lakes.

**Section 8 — Reasonable Security Safeguards:** Data fiduciaries must implement "reasonable security safeguards" to prevent personal data breaches. The DPDP Rules 2025 specify that encryption at rest and in transit is mandatory for personal data. A cloud misconfiguration that exposes an unencrypted database of customer records is a direct Section 8 violation.

**Breach Notification:** The Rules require immediate notification to both data principals and the Data Protection Board upon a personal data breach. Cloud environments without CloudTrail/Audit Logs enabled cannot meet this obligation — they cannot detect a breach, let alone report it.

**Significant Data Fiduciaries (SDFs):** Organisations designated as SDFs (based on volume/sensitivity of data processed) must conduct an annual Data Protection Impact Assessment (DPIA) and audit. A cloud security posture review provides the technical evidence base for the security section of the DPIA.

**Penalty Exposure:** Failure to maintain reasonable security safeguards attracts penalties up to ₹250 crore per incident. For mid-market organisations, a single regulatory action could be existential. The engagement directly reduces this exposure by identifying and prioritising the misconfigurations most likely to result in a notifiable breach.

Every finding in the remediation backlog is tagged to its DPDP Act obligation where applicable, giving the client's legal and compliance team audit-ready evidence of due diligence.

---

## References

- [CIS Benchmarks — Cloud Security Hardening](https://www.cisecurity.org/cis-benchmarks) — CIS Foundations Benchmarks for AWS, Azure, GCP (v3.0+)
- [CIS Benchmarks March 2026 Update: Zero Trust and Passwordless Authentication](https://iplogger.org/blog/cis-benchmarks-march-2026-update/)
- [NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) — Six-function framework including new Govern function
- [NIST CSF 2.0 Complete Guide 2026](https://www.saltycloud.com/blog/nist-csf-2-0-complete-guide-2026/)
- [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) — Seven best-practice areas
- [AWS Well-Architected Review Checklist 2026](https://towardsthecloud.com/blog/aws-well-architected-review-checklist)
- [Microsoft Cloud Security Benchmark — Posture and Vulnerability Management](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-posture-vulnerability-management)
- [Cloud Security Posture Management in 2026 — Security Boulevard](https://securityboulevard.com/2026/03/cloud-security-posture-management-in-2026/)
- [OWASP Cloud-Native Application Security Top 10](https://nest.owasp.org/projects/cloud-native-application-security-top-10)
- [Prowler vs ScoutSuite vs cloud-audit 2026](https://haitmg.pl/blog/aws-security-scanners-compared/)
- [Top 9 Open Source CSPM Tools 2026 — SentinelOne](https://www.sentinelone.com/cybersecurity-101/cloud-security/open-source-cspm/)
- [Wiz Pricing 2026: $50K–$300K+ Per Year](https://www.wizpricing.com/)
- [DPDP Act 2023 and DPDP Rules 2025 — EY India](https://www.ey.com/en_in/insights/cybersecurity/decoding-the-digital-personal-data-protection-act-2023)
- [India's DPDP Rules 2025 — Deloitte](https://www.deloitte.com/in/en/services/consulting/about/indias-dpdp-rules-2025-leading-digital-privacy-compliance.html)
- [DPDP Rules 2025 Notified — PIB India](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)
- [Prowler CSPM Use Cases](https://prowler.com/use-cases/cloud-security-posture-management)
- [Orca Security: What are CIS Benchmarks in Cloud Security?](https://orca.security/resources/blog/what-are-cis-benchmarks-in-cloud-security/)
