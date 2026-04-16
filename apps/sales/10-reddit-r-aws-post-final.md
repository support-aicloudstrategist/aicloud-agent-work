# Reddit r/aws post — FINAL, ready to ship

**Scheduled:** Sunday 19 April 2026, 08:00 IST (= 22:30 ET Saturday, best time for both US and India engagement)
**Account:** Rajiv's existing Reddit account (30+ days old, has prior activity in r/aws)
**Post type:** Text post, no link in title
**Expected length:** 4 minute read, ~700 words — long enough to look substantive, short enough to read in full

---

## Title (120 chars max, 70 used)

```
The 28% problem: engineering teams think their RI coverage is 70%, the billing data says otherwise
```

**Why this title works:**
- Specific number in the hook (28%, 70%)
- Implies a counterintuitive finding (good for curiosity)
- "Engineering teams" = exact target audience
- No clickbait, no all-caps, no emojis
- Avoids triggering automod

---

## Body (exact text to paste)

```
TL;DR: I've been auditing Indian mid-market AWS accounts for the last six months. In every single account, the engineering lead confidently states RI coverage is above 70%. The Cost Explorer report has never once agreed. Sharing the pattern because it's the single most expensive blind spot I keep running into.

The conversation goes almost word-for-word identical every time:

Me: "What's your RI coverage?"
Eng lead: "High — most of the fleet. Probably 70%+."
Me: [pulls the Cost Explorer Utilization report]
AWS: "28%."

On a $30K/month account going from 28% → 70% RI coverage on stable workloads is typically $8K–$12K/month of pure discount. For the year that's north of $100K. No architectural change, no migration, just a commitment portfolio rebalance.

Why the gap keeps happening — three patterns I see:

1. The "we bought reservations" memory is from 2-3 years ago. Those RIs expired. Nobody tracked the expiry. The fleet grew; the commitment didn't.

2. Savings Plan coverage gets mentally mixed up with Reserved Instance coverage. Savings Plans cover compute broadly. RIs are instance-family-specific. An account can have high SP coverage AND low RI coverage simultaneously, and the "what's our effective discount rate" question gets answered wrong because the two numbers get conflated.

3. Reporting is split between engineering and finance. Engineering looks at instance fleet stability. Finance looks at the bill. Nobody owns the intersection: "what's stable × what's committed × at what effective rate." When I ask "who owns RI coverage as a metric," the answer is usually a shrug.

How to diagnose in 10 minutes, no tooling purchase required:

1. AWS Cost Explorer → Reservations → Utilization report
2. Filter last 30 days
3. Look at "Net RI savings" vs total compute spend
4. Below 40% → governance problem, not a technical one

The fix is almost always a one-afternoon meeting between engineering and finance on who signs off on commitment purchases. Not an architectural change. Not a tooling install. A role-clarity conversation.

What's worked in practice:

- Appoint a single owner of commitment coverage as a metric (usually SRE lead or platform lead, not finance — because finance doesn't know the instance family mix)
- Monthly 30-minute review: current coverage, 90-day expiry forecast, recommended purchase action, signoff from both engineering and finance
- Quarterly deeper review: modify / extend / let-expire decisions on existing portfolio
- Set a target rate (70% is reasonable for most teams) and track it alongside SLO dashboards

One pattern that surprised me: the teams that struggle the most are the ones that bought RIs in 2022-2023 and never rebalanced when Graviton became production-ready. The old x86 RI commits lock them into a portfolio that doesn't match where compute actually wants to go.

Happy to answer specific questions in comments — especially if your team is in the middle of this conversation right now. The full governance framework with the monthly review template is on our site (fair warning: company blog, but no gate / form / email capture): https://aicloudstrategist.com/blog/ri-coverage-india-governance.html

Context on me: I run a FinOps consultancy focused on Indian mid-market. Not here to pitch — just this pattern keeps showing up and the governance fix is cheap enough that every team reading this can do it themselves without hiring anyone.
```

**Word count:** ~680 words
**Character count:** ~4200 (well under the 40K limit)
**Link placement:** One link, near the bottom, clearly labeled as company blog with honest disclosure
**Self-promo ratio:** Context disclosure in the last line only, no CTA, no "book a call"

---

## Pre-flight checks before posting

Do all of these 15 minutes before posting:

- [ ] Rajiv's Reddit account has posted or commented in r/aws at least once in the last 30 days (check via `/user/<username>/comments`)
- [ ] Account karma is >100 total (r/aws automod may filter below this — check their pinned rules)
- [ ] Not violating current r/aws rules: https://reddit.com/r/aws/about/rules — check that "self-promotion" isn't banned outright this week
- [ ] Post Title capitalisation matches subreddit norm (r/aws is sentence case)
- [ ] Body uses plain paragraphs — no markdown headers, no bold/italic (r/aws auto-renders poorly)
- [ ] No AWS service trademarks in unnecessary caps (EC2 fine, but don't SCREAM)
- [ ] Schedule via Reddit-native scheduling if possible; otherwise post manually Sunday 08:00 IST
- [ ] Tab open: Reddit inbox, so replies get answered within 60 minutes of receipt

---

## Engagement plan for the first 24 hours

**Hour 0-1:** Post goes live. Do nothing except refresh.
**Hour 1-2:** First comments usually show up. Reply to every comment, even one-line agreements ("good point, thanks for reading" is fine for sparse ones).
**Hour 2-4:** Peak engagement window. Reply substantively to any question. If anyone argues, engage politely — argumentative threads drive up rankings.
**Hour 4-8:** Post will either be rising or not. If not rising (under 20 upvotes), don't panic — it happens. If rising, keep replying.
**Hour 8-24:** US daytime kicks in. Expect a second surge of comments.
**Day 2:** Reply to late comments. Update the post with a "Edit:" line addressing the most common question if patterns emerged.

**What NOT to do:**
- Do NOT link to `/book.html`, `/services.html`, or `/first-customer.html` anywhere — even in replies
- Do NOT ping the OP's team from our own accounts to upvote (vote manipulation → instant ban)
- Do NOT cross-post to r/devops / r/startups within the same 7 days — different story for different audience
- Do NOT edit the post to add a CTA after it starts ranking

---

## Success criteria

- **Floor (acceptable):** 50+ upvotes, 10+ comments, 1-2 DMs to Rajiv's Reddit
- **Good:** 200+ upvotes, 40+ comments, 5+ DMs
- **Home run:** 800+ upvotes, 100+ comments, front page of r/aws, blog traffic spike lasting 7 days

Track via:
- Reddit post URL (upvotes + comments)
- Plausible Analytics: pageviews on `/blog/ri-coverage-india-governance.html` over the next 72 hours
- Vikunja tracker: each DM or Reddit reply becomes a new task

---

## Fallback if it doesn't land

If 6 hours in, <10 upvotes:

1. Don't delete the post — looks desperate
2. Don't bump it artificially
3. Wait 3 weeks, try a different angle on same subreddit
4. Try r/devops with the DORA-for-CFO angle next weekend

If 24 hours in, still flat: the title didn't work. Review in retrospect — the content should carry the post if it's a strong angle. Silent post = title problem, not content problem.
