# Cloud Cost Health Check — Call Playbook

**For:** Anushka B (founder, primary), Rajiv (secondary, optional)
**Purpose:** Run the 30-minute free Health Check calls consistently, extract the information needed to write a trust-building follow-up, and identify which prospects are serious.
**Supersedes:** Nothing. This is the first version.

---

## The math before you start

Every Health Check call is **30 minutes free work**. We can realistically do 3–5 of these a week without losing productive time for paid work. **Protect the 30-minute budget.** If prospects consistently talk past 40 minutes without approving a follow-up, your filter is too loose — tighten the qualification questions on the booking form.

---

## Before the call (5 min prep)

1. **Open their Cost & Usage Report sample in a spreadsheet or a quick notebook.** Skim for the biggest line items by cost.
2. **Note top 3 cost categories** (usually: compute, then storage, then network or database).
3. **Check LinkedIn** of the person who booked — role, tenure, company stage, recent funding.
4. **Have these four tabs open:** the CUR, AWS/Azure/GCP Cost Explorer (if they shared read-only access), aicloudstrategist.com/services.html, this playbook.

---

## The call — 30 minutes, four acts

### Act 1 — Context (first 5 minutes)

Your goal: understand *why* they booked. Ask, listen, do not pitch.

**Opening line:**
> "Thanks for making time, {{FirstName}}. Before we dig into the numbers, it helps me to understand the *why*. What made you book the call this week?"

**Follow-up questions (pick 2 of these, not all):**
- "What does your cloud bill roughly look like per month, across all providers?"
- "When did you last have a structured cost review done?"
- "Is anyone on your team currently owning cloud cost?"
- "What triggered the question — CFO asking, board meeting coming up, hitting a margin target, or something else?"
- "What does 'good' look like for you at the end of this engagement — a specific INR reduction, a reporting baseline, or both?"

**Listen for:**
- Do they own the decision, or will they need to pass this up? (CFO, founder, VP Eng — influence level)
- How urgent is it? (This week / this month / Q3)
- What have they already tried? (Cloudability, Flexera, a previous consultant)
- What is the actual pain? (Bill size, lack of visibility, engineering time lost, board pressure)

**What NOT to do:**
- Do not start explaining what FinOps is
- Do not mention your services yet
- Do not ask "how did you hear about us" — it is filler and they rarely remember

---

### Act 2 — Screen-share through their data (10 minutes)

Your goal: show competence by finding three specific leaks in their data, live. This is the trust builder.

**Transition line:**
> "Let me pull up the sample you shared. I'll walk through what I'm seeing, and you tell me what you already knew and what's new."

**The five-question sweep — hit each of these categories:**

1. **Compute (3 min)** — Biggest EC2 / VM instance types; utilisation if visible; RI coverage % if accessible; any oversized candidates
2. **Storage (2 min)** — S3 / Blob / GCS Standard tier holding old objects; EBS volumes with no GP3 migration; orphaned disks
3. **Network (2 min)** — Cross-region egress bytes; NAT Gateway cost; Data Transfer Out volume
4. **Databases (2 min)** — RDS / Azure SQL / Cloud SQL sizing; Multi-AZ on non-prod; backup retention vs actual usage
5. **Other (1 min)** — CloudWatch logs volume; Elastic IPs unattached; snapshots older than 90 days

**As you find each thing, say:**
> "This looks like {{PATTERN}}. The number I'm seeing is roughly ₹{{X}}/month. Does that match what you expected?"

**When they are surprised by a number, pause.** Do not rush past it. Write down their reaction. Those surprise moments are what the follow-up email is built around.

**What NOT to do:**
- Do not show them a dashboard full of metrics they did not ask for
- Do not say "I can save you 40%" — the math is not there yet
- Do not use acronyms without unpacking them (RI, SP, CUR, EBS — always define first time)

---

### Act 3 — The shape of the problem (10 minutes)

Your goal: translate what you just found into the three highest-impact levers, and verify with them that the list feels right.

**Transition:**
> "Based on what I'm seeing, three things stand out as the biggest levers. Let me tell you what they are, and you tell me if any of them don't make sense for your setup."

**State each lever, one at a time:**

1. **{{LEVER 1}}** — "{{Short description}}. Rough estimate: ₹{{X}}/month recoverable. Fixable in {{time}}. Risk: {{low/medium}}."
2. **{{LEVER 2}}** — Same format.
3. **{{LEVER 3}}** — Same format.

**Then ask:**
> "Of those three, which one would you want to move on first? And is there anything on your estate that I didn't see in this sample that you think is a bigger problem?"

**Listen for:**
- Which one they pick (that is their priority — use it for the follow-up)
- Anything they mention that is not in the sample (extra context to mine)
- Any pushback or scepticism ("we already tried that")

---

### Act 4 — What happens next (5 minutes)

Your goal: lock in the 24-hour follow-up and signal the three engagement options without selling.

**Transition:**
> "That's roughly what I'd expect to see. I'll write all of this up in a two-page summary and send it to you by end of day — including the specific CLI commands you can run to verify my numbers."

**Three things to cover, in this order:**

1. **Confirm what's in the follow-up:**
> "You'll get: the three findings with exact rupee figures, the likely cause for each, and three options for what to do next — DIY, a four-week fixed-price engagement, or a gain-share alternative. No pressure on any of them."

2. **Set the next touchpoint:**
> "If anything in the summary raises questions, reply to the email or book a 15-minute follow-up slot. If you're considering the four-week engagement, the proposal goes out within 48 hours of you saying yes."

3. **Close on trust, not close on sale:**
> "Either way, you keep the written summary. That's yours. Good luck with the quarter."

**What NOT to do:**
- Do not ask "when can you start?" — that's a sales move and it feels pushy
- Do not discount on the call — that signals pricing isn't real
- Do not promise a specific percentage ("I can definitely get you 25%") — you cannot yet

---

## After the call (30 min work)

1. **Immediately** write three single-line notes:
   - "The surprise moment was: ___"
   - "Their top priority is: ___"
   - "Their real pain is: ___ (not the pain they came in describing)"
2. **Within the next 4 hours** — draft the follow-up using `docs/health-check-followup-template.md`.
3. **Before end of business day** — send it, CC support@aicloudstrategist.com.
4. **Log in Notion** (or whatever CRM is in place) — status: "HC completed, follow-up sent", next action, follow-up-by date.

---

## Objection handling

### "You are just one person. What if something happens to you?"

> "Fair question. Every engagement carries a senior-architect review layer — the same person reviews every deliverable before you see it. If I were hit by a bus, that advisor plus the delivery runbook we build during an engagement means continuity. I'm also happy to structure the contract so that deliverables move to your team's ownership on completion rather than staying dependent on us."

### "Your rates are lower than Big-4. What are you cutting?"

> "Three things. No layered margin across five account managers. No junior team doing the actual analysis. No proprietary-tool licence I need to renew. The work is the same quality — the overhead is different."

### "Can you guarantee 30% savings?"

> "No one can guarantee a specific percentage without the full account data and a contract in place — and anyone who does guarantee it before looking is bluffing. What I can tell you is the conservative band across accounts like yours is 15–30%, and our gain-share option means we only take the upside if the verified savings actually land."

### "We use AWS support / a TAM already. Why do we need you?"

> "Your TAM is excellent at the AWS-specific conversations, and they're free — definitely use them. What we add is account-independent cost review, multi-cloud perspective if any of your workloads aren't on AWS, and an incentive structure aligned to your cost, not to AWS's. A TAM recommendation to buy an RI is still an AWS sale. Our recommendation might be 'downsize before you commit.'"

### "Send me a proposal and we'll review internally."

> "Absolutely. What I'm going to send by end of day is a two-page written summary of the three leaks, which is what your team needs to decide internally. A formal proposal follows once you say you want to move forward. That way you aren't reviewing a 12-page doc for a decision you haven't made yet."

### "We bought {{Cloudability / Flexera / CloudHealth}}. Aren't we covered?"

> "Tools surface data. Someone still has to act on them. The companies we work with usually already have one of those dashboards — nobody has the 30 hours a month to interpret it and run purchases. That's the gap we fill. Happy to take a look at what's already in your Cloudability account during a QuickStart — we often find actions their existing tool has been flagging for months."

---

## Red flags that mean "not a good fit"

If you see more than two of these on the call, do not push for the engagement — send a polite follow-up and move on.

- **Monthly cloud spend below ₹2L** — savings ceiling is too low to justify our fee
- **Pre-seed startup** — they don't have budget and don't actually have a cost problem yet
- **Asked you to "also help with a migration and a security review and set up Terraform"** on the first call — scope creep, not ready to engage
- **Keeps comparing you to Big-4 firms by price** — they are not your customer, they want a vendor
- **Unable to share a CUR sample before the follow-up** — no commitment signal
- **Decision-maker not on the call** — conversion rate drops by 60%+ without them
- **"We'll get back to you" without a specific date** — dead lead; log for a 90-day re-touch

---

## What "good" looks like after the first 10 calls

After 10 Health Check calls, look at these numbers:

| Metric | Good | Warning | Bad |
|---|---|---|---|
| % that convert to paid engagement | 20–35% | 10–20% | <10% |
| Avg time from call to decision | <14 days | 14–30 days | >30 days |
| Avg follow-up-email → reply rate | 60%+ | 30–60% | <30% |
| % who choose Option B over A | 50%+ | 30–50% | <30% |

Low reply rate → your follow-up email is too long or too pitchy. Low B/C choice → your findings aren't specific enough in the summary. Slow decisions → decision-maker isn't in the room or the three options aren't clear enough.

---

## One thing to remember

**Every Health Check call is a gift we are giving the prospect.** If they don't buy, that is fine — the relationship is stored in their head and they will recommend us to three people over the next two years. The math on a solo consulting practice is that referrals become the majority of deal flow by month 6. Treat every call that way — including the ones that obviously won't buy.

---

*AICloudStrategist · Anushka B · Founder-led. Enterprise-reviewed.*
