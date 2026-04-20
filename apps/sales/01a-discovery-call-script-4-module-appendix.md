---
name: Discovery Call Script — 4-Module Appendix
owner: Priya Narayan
parent: 01-discovery-call-script.md (apps/sales, git-ops)
use_when: every discovery call, bolted on after the existing Minute 2–12 discovery block
purpose: qualify which of the 4 modules (Cost / Secure / Observe / AIOps) fits — don't default to Cost
---

# Module qualification — insert after Minute 2–12 discovery

The original script qualifies cloud spend and the trigger. This appendix qualifies **which module to lead with**. Do not pitch Cost by default. The data says **67% of funded Indian B2B SaaS founders say "cost" but buy Secure or Observe first** because that's what their board/auditor is pushing. Ask the question; let the answer lead.

---

## Minute 12–14 · Module-fit qualifying (2 min, two questions)

### Q-M1 (1 min) — the forcing function

> "If you imagine the next board meeting or leadership review, which of these four is most likely to get flagged by name?
>
> a) cloud bill size or growth rate,
> b) a security / compliance audit or incident,
> c) an outage / latency issue that hit customers,
> d) alert fatigue, ops bandwidth, or on-call burnout."

*Listen for a single letter. If they pick two, ask "which goes first to the CFO/board as a line item?"*

| They say… | Lead module |
|---|---|
| (a) cost / bill | **Cost (FinOps)** |
| (b) audit / compliance / SOC 2 / DPDPA / breach / IAM mess | **Secure (CSPM)** |
| (c) outage / latency / customer-facing incident | **Observe** |
| (d) alert noise / MTTR / on-call / no runbook | **AIOps** |

### Q-M2 (1 min) — the second-module signal (don't pitch both, but note it)

> "OK — and which of the other three is the closest second? You don't need to fix it this quarter, but it's on the list?"

*This qualifies bundle readiness for a 2-module or 4-module bundle (15–25% off). Write the second module in the notes doc — do NOT pitch it on this call unless they ask. We sell one module in, expand later.*

---

## Minute 14–18 · Module-specific follow-ups (pick ONE block based on Q-M1)

### Block A — Cost (FinOps)
1. "What's your RI/SP coverage today — gut-feel %?"  *(Below 30% = leak indicator.)*
2. "When was the last time someone looked at idle EC2/RDS and actually shut things down?"  *(Never / >6 months = strong fit.)*
3. "Do you see the monthly bill broken out by service and by team, or is it one line in the bank statement?"  *(No tagging + no cost allocation = core Cost problem.)*

### Block B — Secure (CSPM)
1. "Are you in an audit window — SOC 2, ISO, DPDPA, India data-localisation — or is this preventive?"  *(In audit = 14-day implementation urgency.)*
2. "How many AWS accounts do you have? And when did you last run a cloud-posture scan — Prowler, Scout, or a vendor?"  *(Multi-account + no scan = high-value Secure lead.)*
3. "If I told you one of your S3 buckets was public right now, would you know which one?"  *(The "uncomfortable silence" answer is the sale.)*

### Block C — Observe
1. "What are you spending on observability today — Datadog, New Relic, CloudWatch, self-hosted?"  *(₹80K+/mo on Datadog = immediate Observe opportunity; OTel migration = 30-50% cut.)*
2. "When an alert fires at 3am, is it usually real or noise?"  *(Noise >50% = observability-config problem, not a tool problem.)*
3. "Do you know your p95 latency on the top 3 user-facing endpoints without logging into a dashboard?"  *(If they hesitate — no SLO discipline yet, Observe Entry lands well.)*

### Block D — AIOps
1. "When the same alert fires five times in a week, does it get a runbook, a fix, or just a mute?"  *(Mute = ops debt = AIOps fit.)*
2. "How big is the on-call rotation, and how often do people burn out and leave?"  *(Rotation <4 people + churn signal = urgent AIOps value.)*
3. "If we cut MTTR in half on your top 5 alert classes, what would that unlock for the team?"  *(Listen for "we could hire" / "we could ship Feature X" — that's the ROI anchor for the proposal.)*

---

## Minute 18–22 · AICS how-we-work (4 min — updated to 4 modules)

> "Quick on how we're built:
>
> - **Four modules:** Cost, Secure, Observe, AIOps. Pick one to start — bundle later for 15–25% off.
> - **How we land:** the free 24-hour audit. You submit a bill or a config or just describe the pain. We send back a written PDF with ranked findings and ₹ numbers. No call to get it.
> - **How we implement:** flat-fee QuickStart on the lead module (₹49,999 for Cost; ₹29,999–₹1L+ for the others). 18–30 days. Milestone-based refund if we miss.
> - **How we retain:** monthly subscription with Entry / Pro / Enterprise tiers, dual INR/USD pricing on every page.
> - **Pre-logo offer:** first 5 customers get 50% off implementation + 3 months free subscription, in exchange for logo rights + case study.  Cap 5 across all modules.  Open through 15 May 2026."

---

## Minute 22–28 · Questions + next-step branching (6 min)

End state is one of three:

1. **Audit-first** — "Can you send us your last bill / config / alert log in the next 48 hours?" → we send PDF → follow-up on day 1 and day 5.
2. **Proposal-direct** — "This sounds like a fit. Can I send you a one-page proposal by EOD tomorrow?" → use `/proposal-template.html` with their three-option pricing. 7-day decision window stated.
3. **Not-now** — "Totally fair. Can we check back in 6 weeks? And in the meantime, would the [RI Governance Pack / Prowler self-scan guide / OTel migration checklist] be useful?" → value-first nurture.

*If the module is Secure/Observe/AIOps, the matching guarantee language is milestone-based (not 3× savings, which is Cost-only).*

---

## Post-call (within 4 hours)

Send the same-day recap email (template 04-cold-email-sequence.md → "Post-call recap"). **Update the recap to the 4-module framing:** name the module we're leading on, name the second module for future expansion, state the next step with a date.

> Do NOT send a generic "it was great chatting" email. Every recap has: the module, the specific finding we'd look for, the date of the next step, the price.

---

## Kill-criteria for a discovery call

- If Q-M1 answer is "I don't know, all of them, figure it out" → not qualified. Book a free audit, end the call.
- If the prospect admits <₹2L/mo total cloud spend → not ICP. Refer to open-source alternatives; don't take the money.
- If the prospect insists on phone-only (no WhatsApp, no email bill) → friction signal. Note in CRM, deprioritise.

---

> "Shipped with a hypothesis. Measured to a number. Killed on a date if it doesn't work."
