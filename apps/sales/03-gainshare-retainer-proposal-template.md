# Managed FinOps Retainer with Gain-Share — Engagement Proposal

**Prepared for:** {{CLIENT_NAME}}
**Prepared by:** Anushka B, Founder — AICloudStrategist
**Date:** {{PROPOSAL_DATE}}
**Valid until:** {{PROPOSAL_DATE + 14 days}}
**Proposal reference:** AICS-RET-{{YY}}{{MM}}-{{###}}

---

## Summary

This proposal covers a **12-month Managed FinOps Retainer** for {{CLIENT_NAME}}, structured as a fixed monthly fee plus an optional gain-share layer tied to verified cloud cost reduction.

**Why this structure exists:** One-time cost optimisations erode. Without continuous oversight, most organisations return to within 80% of pre-engagement spend within six months of a completed FinOps sprint. A retainer replaces the expensive cycle of periodic consultant re-engagements with a structured, month-to-month operating rhythm.

**What makes this commercially different:** We take on partial risk through the gain-share structure. The fixed fee is set below the loaded cost of hiring a full-time FinOps engineer (typically ₹40–80 lakh/year in India); the gain-share aligns our incentive to actually move the bill, not just publish a dashboard.

**Commercial envelope:**
- Fixed monthly retainer: **₹{{RETAINER_INR}}/month** (GST extra)
- Gain-share: **{{GS_PERCENT}}% of verified monthly savings above ₹{{FLOOR_INR}}/month floor**
- Gain-share cap: **{{CAP_MULTIPLIER}}× the annual retainer fee**
- Term: **12 months** with mutual 60-day opt-out after month 6

---

## 1. Engagement Context

Based on the preceding {{PRIOR_ENGAGEMENT}} (e.g., "FinOps QuickStart delivered on {{DATE}}") and discovery conversations on {{DISCOVERY_DATES}}, this retainer is scoped against:

- **Current monthly cloud spend:** ₹{{CURRENT_SPEND_LAKH}} lakh across {{CLOUDS}}
- **Established baseline from prior engagement:** ₹{{BASELINE_INR}}/month (as of {{BASELINE_DATE}})
- **Ranked backlog handed over:** {{N_ITEMS}} opportunities totalling ₹{{BACKLOG_TOTAL_LAKH}} lakh/month in estimated addressable savings
- **Primary engagement objective:** {{OBJECTIVE — e.g., "execute the top-10 backlog items and sustain cost discipline for 12 months"}}
- **Internal capacity:** {{CAPACITY — e.g., "no dedicated FinOps engineer; 0.25 FTE from DevOps lead"}}

---

## 2. Scope of Service

### Weekly Cost Review (every Monday, delivered by 10:00 IST)

- **Anomaly digest** — any day-over-day spike >15% or service-level anomaly, flagged with root-cause hypothesis and recommended action
- **Commitment coverage pulse** — current RI/SP coverage vs. target, expiring commitments in the next 30 days, portfolio drift alerts
- **Untagged resource delta** — net new untagged spend since prior week, responsible team identified where attributable
- **Action item tracker** — open items from prior weeks, owner, due date

*Client review time: ~10 minutes per week. Delivered async via Slack/email — no meeting unless you want one.*

### Monthly Executive Summary (delivered by the 5th of each month)

Structured, board-ready report covering prior calendar month:
1. **Cost Performance** — total spend vs. prior month, vs. budget, top 5 drivers, commitment coverage rate, verified waste inventory
2. **Optimisation Activity** — actions taken, verified savings realised, new opportunities identified
3. **Governance Health** — tagging coverage, budget alert status, new services/regions flagged
4. **Next Month Outlook** — forecast by service and business unit, planned actions, requests to engineering

### Quarterly Strategic Deep-Dive (90 minutes, scheduled)

Not a readout — a decision meeting. Covers:
- FinOps maturity assessment against FinOps Foundation Crawl/Walk/Run model
- Commitment portfolio rebalancing: 12-month consumption trend, model next tranche
- Architecture cost patterns: emerging trends worth addressing now vs. accepting
- Budget and forecast recalibration for the next quarter
- Strategic recommendations for CFO/CTO review

### On-demand cost response (up to {{HOURS}}/month)

Embedded availability to engineering and finance for:
- Pre-deployment cost estimation (Infracost / Terraform plan review before major changes)
- Bill investigation (any surprise spike, traced within 24 hours)
- Commitment purchase decisions (every RI/SP purchase reviewed before commitment)
- Vendor negotiation support (cloud-provider renewal conversations, enterprise agreement reviews)

### Open-source tooling operation and maintenance

- Infracost, OpenCost, FOCUS-aligned cost export remain maintained throughout the engagement
- Any tool upgrades, configuration changes, or integrations handled by AICloudStrategist
- Documentation kept current; your team can pick up operation at any time with zero switching cost

---

## 3. Pricing Structure

### 3.1 Fixed monthly retainer

| Line item | Amount (INR) |
|---|---|
| Managed FinOps Retainer — monthly fee | ₹{{RETAINER_INR}} |
| GST @ 18% | ₹{{RETAINER_GST}} |
| **Monthly total** | **₹{{RETAINER_TOTAL}}** |

**Annual commitment:** ₹{{ANNUAL_TOTAL_INR}} + GST (12 months)

**What this fixed fee covers:**
- Weekly cost reviews, monthly executive reports, quarterly strategic deep-dives
- Up to {{HOURS}} hours/month of on-demand cost response
- Full operation of open-source FinOps tooling stack
- Named primary contact (Anushka B, Founder) + senior-architect oversight on every report

**Payment terms:** Net 7 from invoice date, monthly in advance. Quarterly payment (3 months advance) offered at 5% discount.

### 3.2 Gain-share layer

Aligned to verified savings against the baseline established in your prior QuickStart / Implementation Sprint:

| Parameter | Value |
|---|---|
| **Savings floor** | ₹{{FLOOR_INR}}/month |
| **Gain-share percentage** | {{GS_PERCENT}}% of verified monthly savings above the floor |
| **Measurement window** | 12 months from the date each saving is realised |
| **Annual cap** | {{CAP_MULTIPLIER}}× the annual retainer fee (₹{{CAP_INR}}) |
| **Verification method** | Monthly FOCUS-aligned billing export comparison against baseline, reviewed and signed jointly |
| **Baseline adjustments** | Workload growth, new product launches, and scope expansions adjust the baseline upward proportionally — gain-share only applies to *unit-level* efficiency gains, not "we cancelled the project" savings |

**Example calculation:**

- Baseline (from QuickStart): ₹18,00,000/month
- Month 3 actual: ₹14,50,000/month (after implementation of top-10 backlog items)
- Verified savings: ₹3,50,000/month
- Floor: ₹1,00,000/month
- Savings above floor: ₹2,50,000/month
- Gain-share due to AICloudStrategist: 20% of ₹2,50,000 = ₹50,000/month
- **Your net cash savings after gain-share: ₹3,00,000/month** (vs. ₹3,50,000 gross)

**If verified savings do not exceed the floor in any given month, no gain-share is due for that month — only the fixed retainer applies.**

### 3.3 What determines if the gain-share structure is a fit

**Good fit for gain-share:**
- Spend is stable or growing; cost reduction is the primary objective
- Prior QuickStart has surfaced a concrete ranked backlog
- Engineering team has capacity to implement recommendations
- Both parties want aligned incentives

**Not a fit for gain-share (skip this layer; retainer alone):**
- Workload is rapidly changing; baseline can't be reliably established
- Primary objective is governance, compliance, or board reporting (not cost reduction)
- Finance team prefers predictable fee structure without variable components

You choose. The retainer stands alone; the gain-share is opt-in.

---

## 4. Why Most Consultancies Do Not Offer This

Gain-share is structurally incompatible with the operating model of Big-4 and mid-tier consultancies because:

1. **Revenue recognition** — consulting firms must book revenue against hours. Gain-share ties revenue to realised outcomes on the client's billing cycle, which doesn't fit quarterly partner revenue targets.
2. **Practice sizing** — firms with 50+ consultants need predictable utilisation. Gain-share requires waiting 3–6 months to be paid, which doesn't fit bench economics.
3. **Partner incentives** — partners are measured on bookings, not outcomes. A smaller fixed fee with upside is penalised even when the total comp is higher.
4. **Due diligence overhead** — measuring verified savings requires clean baseline data, which requires engagements too small for Big-4 to staff efficiently.

AICloudStrategist is structured around the opposite constraints: founder-led delivery means gain-share is a feature, not an accounting nightmare. The smaller we are, the more we care about outcomes — because we don't get paid if outcomes don't happen.

For the detailed reasoning, see: [aicloudstrategist.com/blog/gainshare-structure.html](https://aicloudstrategist.com/blog/gainshare-structure.html)

---

## 5. Governance and Reporting

### Monthly gain-share verification cycle

1. **Day 1 of month:** FOCUS-aligned cost export pulled for prior month
2. **Day 2:** AICloudStrategist runs verification analysis against baseline, adjusts for workload growth per the baseline-adjustment rules
3. **Day 3:** Draft savings calculation shared with your finance contact via the monthly executive summary
4. **Day 4:** Joint review call (30 min) to confirm or adjust numbers
5. **Day 5:** Signed verification memo; gain-share invoice issued against the confirmed amount
6. **Day 12:** Payment due (Net 7 from invoice)

### Dispute resolution

If there's disagreement on verification:
- First escalation: joint working session with your finance + engineering lead + AICloudStrategist senior-architect oversight
- If unresolved: external FinOps Foundation-certified reviewer brought in (cost split 50/50), decision binding
- Historical rate of disputes: zero on engagements completed to date

### Termination for cause

Either party may terminate with 30 days' written notice for material breach. In the event of termination:
- Retainer fees pro-rated to termination date
- Gain-share on savings already realised remains payable through the original 12-month measurement window
- Gain-share on savings realised after termination is **not** payable (the clock stops)

### Termination for convenience

Either party may terminate without cause after month 6 with 60 days' written notice. Same post-termination gain-share treatment applies.

---

## 6. Working Agreement

**Communication:**
- Dedicated Slack/WhatsApp channel, SLA-backed response times (4 business hours for standard, 1 hour for anomalies flagged as urgent)
- Weekly digest Monday by 10:00 IST
- Monthly report by 5th of month
- Quarterly deep-dive on a mutually agreed date

**Named contacts:**
- Your side: {{CLIENT_PRIMARY}} (primary), {{CLIENT_FINANCE}} (finance contact), {{CLIENT_ENGINEERING}} (engineering lead)
- Our side: Anushka B (founder, primary delivery), senior-architect oversight on all reports

**Data handling:**
- Read-only IAM access maintained throughout engagement
- No data extracted from your environment; all analysis runs against your own billing exports
- Monthly reports delivered via your preferred secure channel (1Password share, Drive with granular permissions, encrypted email)
- Mid-engagement and post-termination data handling per the DPA (attached)

**Insurance:**
- Professional indemnity cover confirmed at ₹{{INSURANCE_INR}}
- Certificate available on request

---

## 7. Acceptance

To accept this proposal:

1. **Sign and return this proposal** via email to support@aicloudstrategist.com
2. **Return a signed DPA** (attached separately)
3. **Confirm commencement date** from the available slots: {{SLOT_1}}, {{SLOT_2}}, {{SLOT_3}}
4. **Provide updated read-only IAM credentials** (if access expired from prior engagement) via your preferred secure channel

On receipt we'll send a signed counterpart, the first invoice (month 1 retainer in advance), and a commencement calendar invite with the onboarding checklist.

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

---

## Appendix A — Sample Monthly Executive Summary

*A redacted sample of the monthly report is included with this proposal as a separate PDF. It is representative of the report you will receive on the 5th of each month during the engagement.*

## Appendix B — FOCUS Billing Export Configuration

*Included as a separate technical memo. Describes the exact cost-export configuration we will stand up in your AWS / Azure / GCP environment, which provides the verification data for gain-share calculations.*

## Appendix C — Data Protection Agreement (DPA)

*Included as a separate document. Covers data handling, retention, deletion, breach-notification SLAs, and sub-processor disclosures.*
