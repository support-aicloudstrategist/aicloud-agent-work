# Twitter/X DM Sequence — Engineering Leader Outreach

**Target:** Verified engineers (CTOs, senior engineers, engineering managers, SRE leads) at Indian SaaS/AI companies who publicly post about AWS, cloud cost, infra, or GPU spend.

**Why Twitter instead of LinkedIn:** LinkedIn is restricted for Anushka. Twitter/X has a smaller but more active Indian engineering crowd. DMs work when preceded by thoughtful public engagement. No anti-automation filters for human interaction.

**Rule:** Engage publicly 2-3 times *before* DMing. Cold DMs from accounts that never interacted first are ignored or reported.

---

## Pre-DM engagement (essential — not skippable)

Anushka's Twitter/X account needs to be active for this to work.

**Daily routine (15 min):**
1. Search latest: `aws bill OR "aws cost" OR "gpu cost" India`
2. Search latest: `finops OR "cloud cost"` filter: from India (via geo filters or account bio)
3. Reply to 2-3 posts with genuine, specific insight (not self-promo). Example:

Post: "Our AWS bill tripled this quarter with no usage growth."
Reply: "This pattern is almost always one of three things — cross-region egress, NAT Gateway routing or lifecycle-less S3. Happy to share the BigQuery query that diagnoses it in about 10 min if useful: [link to our blog post]"

4. Like + retweet 2-3 more posts from engineering leaders
5. Build up ~10 engagements before DMing any specific person

**Account hygiene:**
- Bio: "Founder · AICloudStrategist · FinOps for Indian mid-market · Founder-led, enterprise-reviewed · Rohini, Delhi"
- Pinned tweet: a case-study or insight thread (NOT a product pitch)
- Header image: same brand as aicloudstrategist.com
- Follow 50 engineering leaders at target companies (slow, 5-10/day for 2 weeks)

---

## DM 1 — Opener (after 2+ public interactions)

```
Hey {firstname} — Anushka here.

I liked your thread last week on {specific topic}. The point about {specific point} matched a pattern we see in almost every mid-market AWS account we audit.

Short context: I run a FinOps consultancy in Delhi called AICloudStrategist. We help Indian companies cut cloud bills 20-30% in about four weeks. Nothing to sell you here — just wanted to send over our AWS cost-cutting checklist since it's directly related to what you were describing:

aicloudstrategist.com/downloads/aws-cost-cutting-checklist-indian-smbs.pdf

If it saves you even one meeting with the CFO, it's done its job. Happy to talk shop anytime.
```

**Length target:** Under 400 characters. Twitter DM format is casual — long formal emails feel wrong here.

---

## DM 2 — Soft follow-up (Day 5, only if they read DM 1 but didn't reply)

```
Hey {firstname} — one more thing that might be useful.

We've been testing a "first customer" offer for three Indian mid-market companies — 50% off our standard ₹75K FinOps engagement in exchange for a named case study. Rolls out through May.

If {company} is looking at cloud cost right now, might be worth a 20-min call? No obligation. Details: aicloudstrategist.com/first-customer.html

Either way — good luck with the ship.
```

---

## DM 3 — Case study reply (if they said something like "cool, maybe later")

```
Totally get it — timing's everything.

If you want to keep an eye on what we do without committing anything: quarterly pulse email, one pattern per quarter, INR numbers. Just reply with "pulse" and I'll add you. Otherwise the blog's at aicloudstrategist.com/blog.html.

Back to the timeline whenever you're ready.
```

---

## DM 4 — Hard reply (if they asked a specific technical question in reply)

Respond with a *specific, substantive answer* — no pitch, no CTA. This is the moment to build trust.

**Example:**

They ask: "What's the right cadence for reviewing Reserved Instances?"

```
Depends on stack stability. For teams adding >10% new compute per quarter, monthly review is right — otherwise you're buying against workloads that'll be gone before expiry. For steady-state teams it's quarterly. 

Two specifics that matter more than cadence:
1. Review expiring reservations at 90 days out, not 30 — gives time for a tranche decision
2. Always buy Savings Plans for baseline compute, RIs only for steady workload pinned to a specific family

Full framework: aicloudstrategist.com/blog/ri-coverage-india-governance.html — the governance piece is what most teams miss.
```

Wait for them to move the conversation. Don't push.

---

## DM 5 — Public thread hook (if they start engaging publicly more)

If they start replying to your public posts regularly, you now have warm lead status. Move the conversation off Twitter to email/call:

```
Hey — since we've been going back and forth here, might be easier over email or a quick call? 

No pitch, promise — just easier to share specific numbers outside DMs. 15 min: aicloudstrategist.com/book.html

Or drop me a line at anushka@aicloudstrategist.com if you prefer async.
```

---

## Target account list (build over 2 weeks)

**How to find them:**
- Twitter/X search: `from:indian_ceo_account` from accounts we know
- Indian YC batch Twitter lists
- AWS Heroes / AWS Community Builders — India region
- Known Indian startup CTO accounts (follow chains from there)
- Conference speaker lists from previous AWS Summits

**Minimum engagement before DM:**
- Following them for at least 7 days
- Liked 3+ of their posts
- Replied thoughtfully to 2+ of their posts
- They haven't blocked or muted you (check by viewing their profile from your account)

---

## Forbidden

- Cold DM with no prior interaction (instant ignore or block)
- Link-heavy DM (Twitter flags as spam)
- Same DM copy-pasted across 10 people in one day (pattern detection)
- Asking for an intro to their CEO (burns the relationship)
- Follow-unfollow games (damages account reputation)
- Automation tools (same risk as LinkedIn — use human hands only)

---

## Target volume

**Per week:**
- 30 minutes/day public engagement (likes, replies, retweets)
- 5 thoughtful DMs/week (Mon/Wed/Fri — never more than 1/day to same company cluster)
- 3-4 reply conversations active at any time

**Per month:**
- ~20 DMs sent
- ~4-6 real conversations
- ~1-2 discovery calls booked

**Conversion expectation:** Twitter is slower but higher-quality than cold email. Expect first Twitter-sourced customer in month 2, not month 1.
