# Health Check Follow-Up Template

**Purpose:** The 24-hour written summary we promised during the Cloud Cost Health Check call.
**Audience:** Whoever joined the call — usually CTO, Head of Engineering, or Founder.
**Length target:** 1.5 to 2 pages (A4).
**Tone:** Confident, specific, helpful, not pitchy. This is a trust deposit, not a close.
**Delivered:** By end of the same business day as the call, or first thing next morning latest.

---

*Subject line template:* `Cloud Cost Health Check — written summary for {{Company}}`

---

Hi {{FirstName}},

Thanks for the 30 minutes earlier today — here is the written summary we promised.

Based on the 7-day Cost & Usage Report sample you shared and the areas we walked through on the call, these are the three highest-impact levers we would attack first. Every figure traces back to a specific line item in the sample. The math is conservative and excludes anything we could not directly verify from the data you provided.

---

## 1. {{FINDING_1_HEADLINE}}

**What we see in your data:**
{{2-3 sentences citing specific line items, usage types, or resource IDs from the CUR. Example: "Four m5.4xlarge instances in ap-south-1 running 168 hours a week at an average 8% CPU utilisation. This is a $616/month line item ($7,392/year) that is likely 3–4× the correct instance size for the workload pattern."}}

**Why it is probably happening:**
{{1-2 sentences on the most likely root cause. Example: "This looks like a Diwali-season scale-up from late 2024 that was never reversed. The utilisation pattern is flat at a low level — no autoscaling behaviour visible."}}

**Recoverable, conservative estimate:**
**₹{{AMOUNT}} / month** (₹{{ANNUALISED}} / year)

**Effort to close:**
{{Hours/days/weeks. Be honest. Example: "1–2 days of engineering time. Straightforward instance-type swap with a 30-minute maintenance window per instance."}}

**Risk level:**
{{Low / Medium / High — with one sentence explaining why.}}

---

## 2. {{FINDING_2_HEADLINE}}

**What we see in your data:**
{{...}}

**Why it is probably happening:**
{{...}}

**Recoverable, conservative estimate:**
**₹{{AMOUNT}} / month** (₹{{ANNUALISED}} / year)

**Effort to close:**
{{...}}

**Risk level:**
{{...}}

---

## 3. {{FINDING_3_HEADLINE}}

**What we see in your data:**
{{...}}

**Why it is probably happening:**
{{...}}

**Recoverable, conservative estimate:**
**₹{{AMOUNT}} / month** (₹{{ANNUALISED}} / year)

**Effort to close:**
{{...}}

**Risk level:**
{{...}}

---

## Combined picture

| | Monthly | Annualised |
|---|---|---|
| Finding 1 | ₹{{A1}} | ₹{{A1_YEAR}} |
| Finding 2 | ₹{{A2}} | ₹{{A2_YEAR}} |
| Finding 3 | ₹{{A3}} | ₹{{A3_YEAR}} |
| **Total** | **₹{{TOTAL_MONTHLY}}** | **₹{{TOTAL_ANNUAL}}** |

Your current monthly cloud spend is approximately ₹{{CURRENT_SPEND}}. The above represents roughly **{{PERCENT}}% of your current bill** — recoverable without re-architecture, without migrating workloads, and without purchasing any new licensed software.

---

## What we did NOT analyse in this free check

A 30-minute call with a 7-day sample surfaces patterns but cannot surface everything. The following require either a deeper sample or a paid engagement:

- **Reserved Instance / Savings Plan strategy** — needs 30+ days of usage history to model correctly
- **Cross-service cost-attribution and tagging hygiene** — requires reviewing your tagging policy and multi-month attribution data
- **Cross-region egress patterns** — requires VPC flow logs, not just the billing export
- **Application-layer cost drivers** — inefficient queries, over-fetching, cache misses — out of scope for a billing-data review
- **Architecture-level risks** — Multi-AZ gaps, DR posture, IAM sprawl — covered by our separate Cloud Architecture Review service

---

## If you want to close any of this

You have three options. Pick whichever fits your team's bandwidth right now.

**Option A — DIY from here.**
This summary is yours to keep. The findings above are specific enough that a competent cloud engineer on your team can execute any of them. If you want, I can send the relevant AWS / Azure / GCP CLI commands for the top finding, no charge. Reply to this email.

**Option B — Four-week FinOps QuickStart.**
₹75,000–₹1,50,000 depending on account complexity. In four weeks we execute all three findings above plus a full account review (not just the 7-day sample), implement ongoing cost visibility (OpenCost + tagging baseline), and hand you a 90-day continuous-improvement plan. Typical outcome at your spend band is a **20–30% verified monthly reduction**, which based on your bill is roughly ₹{{LOW_END}}–₹{{HIGH_END}}/month.

**Option C — Gain-share.**
For cost-focused engagements where the savings are clearly measurable, we can structure an alternative commercial: a lower fixed fee plus a share of verified savings above an agreed floor. Worth a 20-minute conversation if your bill is over ₹15L/month and you prefer the risk-shifted model. Reply and we can scope it.

---

## A note on our delivery

Founder-led work. Every engagement is delivered by me directly (Anushka B, seven-plus years independent cloud and DevOps practice), with senior-architect oversight reviewing every finding — 22+ years of Fortune 500 and global-consulting experience in the review layer. Founder-level responsiveness, enterprise-grade rigour. Open-source tooling only — OpenCost, Infracost, OpenTelemetry, Terraform. You own everything we deploy.

If any of the findings above need clarification, or if you want me to dig deeper on any specific line item, reply to this email and we can do a 15-minute follow-up call this week. No obligation either way.

Whatever you decide, good luck with the optimisation. The numbers above compound quickly once the first one ships.

— Anushka B
Founder, AICloudStrategist
support@aicloudstrategist.com · aicloudstrategist.com · Rohini, Delhi
*Founder-led. Enterprise-reviewed.*

---

## Usage Notes (for Anushka — not sent to client)

- **Send within 24 hours.** The promise made on the call is the trust signal that converts. Late delivery signals that fee-paid clients will also wait.
- **Never inflate estimates.** Every INR figure must trace back to a CUR line item we can point to. Conservative > optimistic. Over-deliver on implementation.
- **Use actual percentages from their data.** "23% of bill recoverable" beats "up to 30%" because it's specific to them.
- **The three options at the end matter.** Option A (DIY help) is the trust move — most people choose B or C after, because they realise they don't actually have bandwidth to DIY. But offering A honestly signals that we are not here to lock them in.
- **Response tracking:** log which option the client picks in Notion. Option A → follow up in 30 days asking how it went; if they did it, they are a candidate for QuickStart as a second engagement. Option B or C → send proposal using `engagement-proposal-template.md`.
- **Email format:** send as HTML email with this content as the body. Do NOT attach as a PDF — PDFs get left in inboxes. An inline email is read.
- **CC:** support@aicloudstrategist.com on every send so both Anushka and Rajiv see the thread.
