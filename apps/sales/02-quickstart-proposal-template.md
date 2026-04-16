# FinOps QuickStart — Engagement Proposal

**Prepared for:** {{CLIENT_NAME}}
**Prepared by:** Anushka B, Founder — AICloudStrategist
**Date:** {{PROPOSAL_DATE}}
**Valid until:** {{PROPOSAL_DATE + 14 days}}
**Proposal reference:** AICS-QS-{{YY}}{{MM}}-{{###}}

---

## Summary

{{CLIENT_NAME}} is evaluating a structured FinOps engagement to establish a verified baseline of cloud spend, identify ranked savings opportunities, and equip the internal team with the tools to sustain cost discipline after our engagement ends.

This proposal covers a **two-week FinOps QuickStart** engagement against your {{AWS / Azure / GCP / multi-cloud}} environment with an approximate monthly spend of **₹{{SPEND_LAKH}} lakh**. The outcome is a ranked savings backlog with verified INR figures, a tagging and cost-allocation baseline, a 90-day implementation plan with named owners, and an open-source tooling foundation you keep.

**Commercial terms:** Fixed fee of **₹{{FEE_IN_INR}}** (GST extra), payable 50% at kickoff and 50% on delivery. No hourly billing, no scope-creep surcharges, no vendor licensing passed through.

**Optional gain-share layer:** If the engagement transitions to an Implementation Sprint or Managed Retainer, a gain-share clause aligned to verified savings can be added — see Section 7.

---

## 1. Engagement Context

Based on our discovery call on {{DISCOVERY_DATE}}, the following context frames this engagement:

- **Current monthly cloud spend:** Approximately ₹{{SPEND_LAKH}} lakh across {{CLOUDS}}.
- **Growth trajectory:** {{SPEND_GROWTH}} year-over-year.
- **Primary trigger:** {{TRIGGER — e.g., "CFO questioned Q4 bill growth," "board wants a cloud cost line-item owner," "recent surprise spike of ₹X lakh in month Y"}}.
- **Current FinOps posture:** {{POSTURE — e.g., "no dedicated ownership," "tagging coverage below 50%," "RI/SP coverage unknown"}}.
- **Expected internal stakeholders:** {{NAMES/ROLES}}.

This QuickStart is scoped as a **diagnostic sprint, not a transformation programme**. The objective is speed to insight: a ranked backlog in your inbox within 14 days, actionable by your own team or convertible to a follow-on engagement.

---

## 2. Scope of Work

### In scope

1. **Spend baseline across all in-scope accounts** — six months of cost history pulled from AWS Cost & Usage Report / Azure Cost Management / GCP Billing Export, with anomaly and trend analysis.
2. **Commitment coverage audit** — Reserved Instances, Savings Plans, Committed Use Discounts: current coverage rate, expiry profile, and recommended portfolio action.
3. **Waste and idle resource audit** — unattached EBS/managed-disk volumes, idle load balancers, orphaned snapshots, low-utilization compute, non-lifecycle-managed object storage.
4. **Tagging and allocation review** — coverage heatmap by service/region/account, recommended taxonomy, enforcement mechanism.
5. **Architecture cost patterns** — data transfer and egress charges, NAT Gateway patterns, cross-region/cross-AZ patterns, database right-sizing.
6. **Ranked savings backlog** — every identified opportunity quantified in INR, classified by implementation effort (≤1 day / 1–5 days / architectural), risk-rated, and sequenced.
7. **90-day implementation plan** — named engineering and finance owners for each action, target completion dates, measurement approach.
8. **Open-source tooling foundation** — Infracost (pre-deployment cost estimation), OpenCost (Kubernetes cost allocation, if applicable), a FOCUS-aligned cost export configuration you own.
9. **Final readout** — 90-minute working session with your engineering lead, finance contact, and any executive stakeholder invited. Not a slide deck — a decision meeting.

### Out of scope

- Implementation of the recommended actions (covered under a follow-on Implementation Sprint if desired)
- Migration work, re-architecture, or workload refactoring
- Vendor negotiations with AWS/Azure/GCP sales representatives (we'll brief you; we won't be a party)
- Cloud security posture review (separate service — see aicloudstrategist.com/services.html)
- 24/7 operational monitoring or incident response

### Assumptions

- Read-only IAM role / service principal / service account provided by Day 1 of Week 1
- Engineering lead available for the Day 1 kickoff (90 min) and Day 10 readout (90 min), plus ~2 hours async through the sprint
- Finance contact available for one 45-minute session in Week 1 to confirm chargeback structure (if applicable)
- Access to Terraform/Pulumi repositories for pre-deployment cost analysis (optional but recommended)

---

## 3. Delivery Timeline

| Week | Days | Activity | Deliverable |
|---|---|---|---|
| **Week 1 — Discover** | Day 1 | Kickoff, access setup, environment walk-through | Kickoff notes, data-access confirmation |
|  | Days 2–3 | Cost baseline pull, commitment coverage analysis | Baseline cost model (6-month trend) |
|  | Day 4 | Waste and idle audit | Waste inventory with INR/month |
|  | Day 5 | Tagging and allocation review | Tagging heatmap, taxonomy draft |
| **Week 2 — Quantify** | Day 6 | Architecture cost patterns (egress, NAT, DB) | Architecture findings memo |
|  | Day 7 | Savings backlog ranking and quantification | Ranked backlog (draft) |
|  | Day 8 | 90-day implementation plan drafting | Implementation plan (draft) |
|  | Day 9 | Client review session, refine backlog and plan | Final backlog + plan |
|  | Day 10 | Final readout, handover of open-source tooling | Final package: backlog + plan + tooling |

**Kickoff date:** {{KICKOFF_DATE}} (14 days from signed SOW, to accommodate access setup)
**Delivery date:** {{DELIVERY_DATE}} (14 calendar days after kickoff)

---

## 4. Deliverables

1. **Ranked Savings Backlog** (spreadsheet + PDF executive summary)
   Every opportunity with: savings estimate in ₹ per month, implementation effort, risk rating, dependency on other actions, recommended owner.

2. **Tagging & Cost Allocation Baseline** (spreadsheet + recommended taxonomy)
   Current coverage heatmap, recommended tag structure aligned to your cost-centre and product taxonomy, enforcement mechanism recommendation.

3. **90-Day Implementation Plan** (PDF)
   Sequenced action plan with named engineering and finance owners, target dates, measurement approach, dependencies called out.

4. **Open-Source Tooling Foundation** (repository handover)
   Configured Infracost pipeline (if applicable), OpenCost deployment manifests (if Kubernetes is in scope), FOCUS-aligned billing export setup, CI/CD integration recommendations.

5. **Final Readout Session** (90 minutes, recorded)
   Presented to your engineering lead, finance contact, and any executive stakeholder. Includes recording, slide deck, and Q&A captured as an addendum.

---

## 5. Pricing

| Line item | Amount (INR) |
|---|---|
| FinOps QuickStart — fixed engagement fee | ₹{{FEE_IN_INR}} |
| GST @ 18% | ₹{{GST_AMOUNT}} |
| **Total** | **₹{{TOTAL_AMOUNT}}** |

**Payment milestones:**
- 50% at signed SOW (₹{{50_PERCENT}} + GST)
- 50% on delivery of the final readout (₹{{50_PERCENT}} + GST)

**Payment terms:** Net 7 from invoice date. Wire transfer or UPI preferred; cheque accepted.

**What this fee does NOT include:**
- Cloud provider costs (AWS/Azure/GCP charges remain your responsibility)
- Third-party tool licences (our open-source approach means none required; if you prefer a commercial FinOps platform we can scope that separately)
- Travel or on-site presence (engagement is fully remote; on-site available on request at cost)

**What happens if we go over scope or time:**
- Scope change requests are logged and reviewed at the Day 9 client review
- If additional effort is agreed, it's priced at a separate fixed fee with your written approval — never billed hourly, never surprise
- If we're slow on our side, the delivery date moves but the fee does not

---

## 6. What You Get That You Don't Get Elsewhere

| Standard consultancy pattern | AICloudStrategist pattern |
|---|---|
| Junior analyst runs a dashboard export | Founder-led delivery with senior-architect review |
| Report delivered in PDF, tooling kept by consultant | Open-source tooling handover, you own it forever |
| Hourly billing, scope creep = bill creep | Fixed fee, fixed scope, surprise-free |
| Recommendations tied to their partner tools | Vendor-neutral; we don't resell AWS/Azure/GCP credits |
| Gain-share conversation avoided | Gain-share layer available and structured transparently |
| Work subcontracted to offshore delivery | Delivered by the founder who signed the SOW |
| Reports written for internal consumption | Deliverables written for board-ready review |

**Founder-led. Enterprise-reviewed.** That's the tagline because it's the operating model.

---

## 7. Optional Gain-Share Addendum

If this engagement converts to a follow-on Implementation Sprint or Managed FinOps Retainer, we offer a gain-share structure that aligns our incentives with verified savings:

- **Savings floor:** Defined as ₹{{FLOOR_INR}}/month of verified cost reduction vs. the baseline established in this QuickStart
- **Gain-share percentage:** 20% of verified monthly savings above the floor
- **Measurement window:** 12 months from the date savings are realised
- **Cap:** Gain-share payments capped at 2× the fixed engagement fee of the follow-on engagement
- **Verification:** Measured against the FOCUS-aligned billing export baseline, reviewed monthly, signed off by both parties

**If verified savings do not exceed the floor, no gain-share is due — only the fixed fee applies to the follow-on engagement.**

This structure is optional. The QuickStart fee above stands alone regardless of whether a follow-on engagement is contracted.

---

## 8. Working Agreement

**Communication cadence:**
- Daily async update in a shared Slack or WhatsApp channel (whichever your team prefers)
- Two scheduled calls: kickoff (Day 1, 90 min) and readout (Day 10, 90 min)
- Optional mid-sprint check-in on Day 5 if requested

**Data handling:**
- Read-only access only; no write operations without explicit written approval
- No data leaves your environment without your explicit written sign-off
- Analysis artifacts (spreadsheets, cost exports, screenshots) delivered to you at engagement close; our copies deleted 30 days post-delivery
- NDA available on request; we're happy to sign yours or provide ours

**Confidentiality:**
- Case studies published on aicloudstrategist.com/proof.html anonymise client identity by default
- With your written approval, named case studies available at no additional cost (helps you too if you want the credit)

**Escalation path:**
- Day-to-day: Anushka B (founder, direct delivery)
- Technical escalation: senior-architect oversight layer reviews every major finding
- Commercial escalation: any payment or scope questions come to Anushka directly

---

## 9. Acceptance

This proposal is valid for 14 calendar days from the date above. To accept:

1. **Sign and return this proposal** via email to support@aicloudstrategist.com
2. **Provide the read-only IAM/service-principal credentials** via your preferred secure channel (we accept AWS Cross-Account roles, Azure service principals, GCP service accounts, or 1Password-style secure share)
3. **Confirm kickoff date** from the available slots: {{SLOT_1}}, {{SLOT_2}}, {{SLOT_3}}

On receipt, we'll send a signed counterpart, the first invoice (50%), and a kickoff calendar invite with the pre-read checklist.

---

**Signed on behalf of AICloudStrategist:**

Anushka B
Founder
AICloudStrategist · Rohini, Delhi 110085 · India
support@aicloudstrategist.com
GSTIN: {{GSTIN}}

Date: ___________________

---

**Accepted on behalf of {{CLIENT_NAME}}:**

Name: ___________________
Title: ___________________
Signature: ___________________
Date: ___________________
