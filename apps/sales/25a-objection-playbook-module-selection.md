---
name: Objection Playbook — "Why Secure/Observe/AIOps before Cost?"
owner: Priya Narayan
parent: 25-objection-playbook.md (or its latest numbering — merge on next edit)
use_when: prospect pushes back on module sequencing or says "just do cost, skip the rest"
---

# Module-sequencing objection patterns

## Pattern 1 — "We only care about cost right now. Skip Secure/Observe/AIOps."

**What you hear:** "We're a 20-person startup, we don't have a compliance problem, just cut the bill."

**What they mean (90% of the time):**
- Board/CFO pressure is on cost, so that's what's verbalised.
- Security/observability issues exist but haven't blown up *yet* — they're invisible until they cost money.

**Reply (short-form, email):**
> Totally fair — we'd lead on Cost for you. The reason we offer four modules is that the *reason* bills balloon is usually a second-order problem: over-provisioning hides alert-fatigue; a SOC 2 rush forces emergency Datadog spend; S3 lifecycle policies never get written because tagging is 30%. Cost is the symptom, the others are the cause. We fix the symptom first and point at the causes. If only Cost sticks, that's still a great outcome.

**Reply (long-form, call):**
> Three things I see again and again: (1) teams that skip observability end up over-provisioning "just in case" — Cost savings land, then revert in 6 months. (2) Teams that skip Secure end up with an audit-emergency that blows the cost savings. (3) Teams that skip AIOps burn out the on-call people, who leave, and then the cost discipline goes with them. We can still lead on Cost — that's the most common entry point. I just want you to know the other three are sitting there, and if we bundle even two at a time, you get 15% off the subscription. The pre-logo offer is good through 15 May if you want both locked in.

**Kill signal:** If they double down after both replies, lead on Cost, note the other modules as second-year expansion in the CRM. Don't push a bundle they haven't asked for.

---

## Pattern 2 — "Show me cost savings first, *then* we'll talk about Secure."

**What you hear:** "Prove ROI on Cost, then maybe we buy more."

**What they mean:** Rational sequencing. Want to minimize downside risk on module 2.

**Reply:**
> That's exactly how we land most customers. Here's what works: we run the free 24-hour audit on Cost. You'll see specific ₹ savings. If those materialise in 30 days post-QuickStart, we have a conversation about Secure in month 2 — by then you know our pattern and we know yours. The bundle discount is still available if you add module 2 within 90 days of module 1 go-live.

**Kill signal:** None — this is a healthy objection. Sign Cost, deliver, win the expansion.

---

## Pattern 3 — "Why should I pay for Observe? CloudWatch is free."

**What they mean:** They haven't priced Datadog / New Relic at scale, or they have and are using raw CloudWatch + ad-hoc Grafana.

**Reply:**
> CloudWatch is great for infrastructure signals — less great when you need app-level traces across 40 microservices, custom SLOs, and alert routing that doesn't wake 4 people at 3am. Observe lands when you're either (a) paying ₹80K+/mo for Datadog and looking for a 40% cut, or (b) stuck in CloudWatch and realise your engineers spend 6 hours/week gluing it together. If neither is true, honestly — don't buy Observe. Stay on CloudWatch until it breaks, then call us.

**Kill signal:** If they're <₹40K/mo observability spend AND <20 engineers, recommend they stay self-hosted. Don't sell them Observe they don't need. (Lost deal >> churned customer.)

---

## Pattern 4 — "AIOps sounds like hype. What does it actually *do*?"

**What they mean:** Healthy skepticism. Give a concrete answer or lose trust.

**Reply (concrete example):**
> Fair. Here's what AIOps means for us — no LLM-this-LLM-that. We do three things: (1) auto-remediation for the top 5-10 alert classes you define (cert expiry, RDS connection exhaustion, CloudFront 5xx, disk full, OOM kills). (2) Alert-deduplication so PagerDuty doesn't wake the team 20× when one thing breaks. (3) A weekly "what's drifting" report so the AIOps tier improves its own suggestions. We measure it on MTTR and on-call pages per week. If those numbers don't move in 30 days, the milestone isn't hit and you get partial refund. That's it. No black box.

**Kill signal:** If their team is <10 engineers and they have no on-call rotation, AIOps is premature. Recommend Secure or Cost first.

---

## Pattern 5 — "Can't we just bundle all 4 on day one?"

**What they mean:** Buying enthusiasm. 10% of prospects — honor it.

**Reply:**
> Yes — 25% off on the 4-module bundle. Pro-tier bundle is ₹1,98,747/mo (saves ₹66K/mo vs individual modules), annual prepay = 2 months free, total landed cost ≈₹19.87L/year. We do need a sequenced implementation — Cost and Secure in month 1, Observe in month 2, AIOps in month 3 — because running all four in parallel burns your team. Same contract, staged delivery, single price.

**Kill signal:** None. This is a win. Route to Arjun for final contract review.

---

## Pattern 6 — "I want Secure first, not Cost. Isn't that backwards?"

**What they mean:** Audit pressure, breach scare, or compliance deadline.

**Reply:**
> Not at all — roughly 30% of our pipeline leads with Secure, usually because of an audit window or a post-incident review. The Secure QuickStart is 14–21 days, milestone-based refund, and covers CSPM baseline + top-10 finding remediation. If you tell me the audit date and the framework (SOC 2 / ISO / DPDPA / India data-loc), I can build the exact milestone plan by EOD tomorrow.

**Kill signal:** If they name a date <10 working days away, we cannot deliver Secure in time. Be honest: "We can't hit 10 days credibly. Option A: extend the audit by 2 weeks. Option B: we refer you to a partner we trust for the sprint, then we pick up month 2 for ongoing." Never over-promise on compliance timelines — one missed audit = reputation loss for the brand.

---

## Meta-rule (standing)

**When a prospect asks a module-ordering question, the answer is almost never "lead with Cost." It's "lead with the module that's causing the pain verbalised in the first 10 minutes of the discovery call." Cost is the most common — ~55% of our leads. Secure is ~25%. Observe ~12%. AIOps ~8%. Check Q-M1 answer in the discovery script; don't override the prospect's own framing.**

> "Shipped with a hypothesis. Measured to a number. Killed on a date if it doesn't work."
