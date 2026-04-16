# Cold Email 5-Sequence — Indian Mid-Market FinOps

**Target:** CTOs, VPs of Engineering, Heads of Infrastructure at Series A-B Indian SaaS / AI / fintech companies running AWS or Azure.

**Why this works:** Specific numbers, specific patterns, specific free value up front. No hype words. Skippable if not relevant.

**Rule:** Personalise at least the first line and the "why now" paragraph for every single send. Never cut-paste.

---

## Email 1 — Initial cold (Day 0)

**Subject line options (test 3, pick winner after 20 sends):**
- `{firstname}, a question about your {cloud} bill`
- `2 patterns in {company}'s infra — thoughts?`
- `Is {company} seeing the April AWS GPU reprice?`

**Body:**

```
Hi {firstname},

{Personalised first line — reference one specific thing about the company: recent funding round, new hire, product launch, their own tweet about infra cost. Skip if you can't find one; don't fake it.}

Quick context: I run a FinOps consultancy called AICloudStrategist out of Delhi. The short version is we help Indian mid-market companies cut AWS / Azure / GCP bills 20-30% in four weeks — founder-led delivery, open-source tooling, no vendor lock-in.

Two patterns I keep seeing at {company-stage} Indian SaaS companies right now:

1. Reserved Instance coverage sitting below 30% on stable workloads — engineering teams consistently believe it's at 70%+. The gap is usually ₹3-8L/month of pure discount left on the table.

2. Cross-region egress charges quietly compounding. One Terraform region flag can 3x a GCP bill over six months (we wrote this up: aicloudstrategist.com/blog/cross-region-egress-mistake.html).

If either of those sounds familiar — or if the April 2026 AWS GPU reprice has {company} reviewing infra cost right now — here's what I'd suggest:

• Free 30-min Cloud Cost Health Check — I run it, give you a candid read on your cost posture, zero pitch. Book here: aicloudstrategist.com/book.html

• Free checklist if you'd rather diagnose yourself: aicloudstrategist.com/downloads/aws-cost-cutting-checklist-indian-smbs.pdf

Not a fit? No reply needed. Happy to stay out of your inbox.

Anushka B
Founder, AICloudStrategist · Rohini, Delhi
aicloudstrategist.com
```

---

## Email 2 — Soft follow-up (Day 4)

**Subject (reply to Email 1 — keeps thread):** `Re: {previous subject}`

**Body:**

```
Hi {firstname},

Following up quickly in case the first email got buried.

One thing I should have mentioned — we're taking 3 first-customer spots at a 50% discount this quarter (₹40K vs standard ₹75K on the FinOps QuickStart, two-week engagement). These three will be our named case studies, so we're picking companies we'd be proud to put on the site.

If {company} might be a fit, I'd genuinely like to have the conversation. If not, that's fine too — happy to send the checklist and step aside.

Details: aicloudstrategist.com/first-customer.html

Anushka
```

---

## Email 3 — Value-only (Day 10)

**Subject:** `something useful for {company}'s infra team`

**Body:**

```
{firstname},

Not chasing — just sharing.

I put together a quick breakdown of the three AWS Cost Explorer blind spots that catch nearly every mid-market team: cross-service attribution, spike causation, commitment drift. Short read: aicloudstrategist.com/blog/cost-explorer-blindspots.html

If your engineering team wants to run the Athena queries in there against your own CUR, everything they need is in the post. Free, no gate, no form.

If you ever want a second pair of eyes on what the queries surface — you know where to find me.

Anushka
```

---

## Email 4 — Honest break-up (Day 18)

**Subject:** `ok, stepping away`

**Body:**

```
{firstname},

Three emails in three weeks is my limit — didn't want to be the person who keeps emailing without a signal to keep going.

If timing is off right now, that's completely fine. The blog posts on aicloudstrategist.com are there whenever useful. If things change and you want to talk, just reply to this thread and I'll be back in your inbox within the day.

Good luck with what you're building at {company}.

Anushka
```

---

## Email 5 — Quarterly pulse (re-engagement, Day 90+)

**Subject:** `90-day pulse on Indian cloud cost — one pattern`

**Body:**

```
{firstname},

Opted-in quarterly pulse email — one email every 90 days with one specific pattern I'm seeing across Indian mid-market cloud spend. Unsubscribe by replying "stop".

This quarter: {one specific pattern with INR numbers — example: "The median mid-market AWS account I've audited over the last 90 days has ₹4.2L/month in orphaned EBS volumes, up from ₹2.8L last quarter. EBS gp3 migrations in March caused a silent spike in unattached volume retention."}

Full breakdown and the 10-minute detection command: {link to relevant blog post}

Take a look if useful. Ignore if not.

Anushka
```

---

## How to personalise the first line (examples)

Do this work — it's the difference between 1% and 10% reply rate.

| Signal | First line example |
|---|---|
| Recent funding | "Congrats on the ₹X Series B — big week for {company}." |
| Hiring spree | "Saw {company} posted 12 SRE/platform engineer roles on LinkedIn last month — impressive pace." |
| CEO/CTO tweet about infra | "Your thread on {specific topic} from last week resonated — especially the bit about {specific point}." |
| Product launch | "Just saw the {product name} launch — looks like real data-scale under the hood." |
| Their blog / tech-blog post | "Read the engineering blog post on {topic} — the decision to go {specific technology} was interesting." |
| Conference talk | "Caught your talk at {conference} — the segment on {topic} stuck with me." |
| Job description infra stack | "Saw your JD mentions {specific tech stack} — that stack tends to have specific cost patterns worth watching." |

**If you can't find one real personalised opener, skip the send.** A bad personalisation is worse than no personalisation.

---

## Target list signals (who to send to)

**Send:**
- Series A-B Indian SaaS / fintech / AI / B2B software, team 20-200
- Engineering leader (CTO, VP Eng, Head of Infra, Head of Platform, SVP Engineering)
- Stack includes AWS or Azure (verify via: JDs mentioning it, StackShare profile, company blog)
- Funded in last 12 months (implies budget + growth pressure)
- OR: posted publicly about cloud cost, AWS bills, or GPU infra in last 90 days

**Don't send:**
- CEOs / founders of companies >500 people (procurement will reject any consultant without a vendor-master path)
- Finance team contacts (need technical champion first)
- Competitors (other FinOps / cloud-cost consultancies)
- Anyone in "No" state (previously emailed + clear no-reply)

---

## Sending rhythm + deliverability

**From address:** `anushka@aicloudstrategist.com` (Google Workspace — clean reputation)

**Volume cap:** Max 15 cold emails per day from this address. Google will throttle above 50/day from a new domain.

**Warmup state:** The domain has been sending transactional email (InvoiceBot + blog publish notifications) for 4+ weeks. Reputation is fresh but clean. Start at 5/day for week 1, ramp to 10/day week 2, 15/day week 3 max.

**Subject line testing:** Run 3 subject variants across the first 30 sends. Pick the one with the best open rate (manually check via replies — don't use tracking pixels; Google flags them).

**Reply tracker:** Save every reply into the Vikunja tracker as a new task (`vk add 6 "Reply from {firstname} at {company}"`), prio 5, labelled `claude-owns` while we're qualifying.

**Forbidden:**
- No open-tracking pixels (Google's spam filter hates them; conversion impact negligible)
- No link-tracking redirects (same reason)
- No merge tags left unfilled — any "Hi {firstname}" that goes out literally is an instant spam flag
- No attachments in cold email (triggers spam filters)
- No "unsubscribe" link (you're not a newsletter — one-to-one emails don't need one; a link flags as bulk)

---

## Tracking template

Keep a simple google sheet: `Target | Email sent | Replied | Call booked | Proposal sent | Closed`

Review weekly with Rajiv. Anything without a reply at day 18 → break-up email → stop.
