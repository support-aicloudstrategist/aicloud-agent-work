# Anushka — Daily Playbook, First 30 Days

**Total time per weekday:** 15–20 minutes.
**Weekends:** optional (see end). Skipping weekends is fine.
**Cadence start:** once LinkedIn profile is complete and at least one first-wave post is live.

This is the daily rhythm that turns the tooling we built into measurable pipeline. It is deliberately short. Momentum beats intensity.

---

## Every morning, in this order (15 minutes)

### 1. Open Telegram (1 min)

Look at the `@bill_15_bot` group. Three things to note:

- Any **overnight queue results** — mao may have completed drafts, audits, or research you queued the day before
- Any **scheduled-post pings** — if a LinkedIn post auto-published overnight, check engagement in a minute
- Any **failure pings** — rare, but if something broke, address it first

If there are no pings, skip this step.

### 2. Check LinkedIn notifications (3 min)

- **Connection requests accepted** — for each one, click the name → DM them → click the `LI-DM-Anushka` bookmarklet → review the Day-2 message → send. 10 seconds per person.
- **Comments on your posts** — reply within the first hour of posting the comment, thoughtfully. This dramatically increases reach.
- **New DM conversations** — reply to anyone who asks a question, links the Health Check if relevant.

**Cap: 15 accepted-connection follow-ups per day.** If you have more than 15, save the rest for tomorrow. Fatigue in your replies hurts more than missing a day.

### 3. Send today's 15 connection requests (8 min)

Today's segment depends on the day:

| Days 1–5 | Past colleagues and known professionals |
| Days 6–15 | CTOs, VPs Engineering, DevOps leads at Indian tech companies |
| Days 16–20 | Founders who raised Series A/B in last 18 months |
| Days 21–22 | FinOps Foundation members (India chapter) |
| Days 23–26 | Engineering hiring managers at target companies |
| Days 27–30 | Indian cloud community contributors + repeat segment 2 |

**Process:**

1. Open the daily target list — either from your memory (for past colleagues), or from the mao-generated `/docker/task-queue/data/drafts/linkedin-targets-YYYY-MM-DD.md` (the cron generates this automatically at 09:00 IST on weekdays)
2. For each of the 15:
   - Open their LinkedIn profile in a tab
   - Click `LI-Copy-Prospect` bookmarklet → paste to Notion/CRM
   - Click `LI-Connect-Anushka` bookmarklet → review note → personalise first sentence if needed → send
3. Total: ~30 seconds per prospect × 15 = 7.5 minutes

**Never exceed 15 per day.** LinkedIn rate-limits profiles that push it, and acceptance rate drops.

### 4. Engage with 1 target CTO's post (3 min)

Open LinkedIn feed. Find a post by someone in your target audience (CTO/VP Eng/Head of Platform at an Indian mid-market tech company). Read it properly.

Click the `LI-Comment-Draft` bookmarklet → review the draft → edit for authenticity → post as a comment.

**One thoughtful comment per day beats ten generic ones.** LinkedIn's algo notices engagement quality. The profile you commented on becomes a warm lead without any cold outreach.

---

## Twice a week (Tuesday + Thursday): publish a post (0 minutes if scheduler is live, 2 minutes if manual)

If the LinkedIn auto-publisher is set up (see `docs/linkedin-scheduler-setup.md`), posts go out automatically at 10:00 IST. Zero effort.

If not yet set up: copy the post from `apps/outreach/playbook.md` (first 4 posts) or `drafts/posts-w3-to-w6/` (next 10) → paste into LinkedIn → publish.

**Immediately after publishing:**
- For the next 60 minutes, check for early comments/reactions. Reply to every comment within those 60 minutes. Early engagement drives algorithmic reach.

---

## After every Health Check call (45 minutes, same day)

A Health Check is a serious time investment. Protect the 24-hour follow-up promise:

1. **In the 10 minutes after the call ends** — write down 3 lines from `docs/health-check-call-playbook.md`: the surprise moment, their top priority, their real pain
2. **Within 4 hours** — Use the bot: `/followup <Client Name> | <finding 1 with ₹ figure> | <finding 2 with ₹ figure> | <finding 3 with ₹ figure>`. Mao drafts the full follow-up email using the template. Saved to `/docker/task-queue/data/drafts/followup-<client>.md`.
3. **Review and polish** the draft (usually 5-10 min of edits for client-specific context)
4. **Send before end of business day.** CC support@aicloudstrategist.com.
5. **Log in Notion/CRM:** call date, findings, follow-up sent, next-action date.

---

## Weekly (Sunday evening, 20 minutes)

### Review the week's numbers

Open Plausible Analytics → check the week:

- **Unique visitors** — should climb from baseline (~10) to 50–200/week by end of month 1 if outreach is working
- **Top pages** — most visitors probably land on services, blog posts, or the lead-magnet wrappers. The ratio tells you which content is pulling
- **Referrers** — LinkedIn should be #1. If Google is appearing in the top 5 by week 4, SEO is kicking in

Open LinkedIn analytics (on Anushka's profile):

- Impressions per post
- Profile views this week
- Search appearances

**If profile views went up but no Health Checks booked:** the booking link in Featured / About is fine, but the value prop isn't landing. Adjust the next post's hook.

**If posts are getting >1000 impressions:** double down on that angle for the next two posts.

### Plan next week's targets

From `/docker/task-queue/data/drafts/linkedin-targets-*.md` (auto-generated daily by cron), pick the 75 prospects for next week. Block them out by day in a simple Google Sheet or Notion database:

| Day | Segment | 15 names |
|---|---|---|
| Mon | Segment X | ... |
| Tue | ... | ... |

This takes 10 minutes and makes every weekday morning trivial.

### Clear the bot queue

- `/qlist` in Telegram — see any pending tasks
- `/qresults` — review last results
- `/qclear` only if the queue has stale tasks you no longer want executed

---

## Monthly (last Sunday of month, 45 minutes)

1. **Update CRM** — mark every prospect as: interested / later / not interested / converted / dead. Log the next follow-up date.
2. **Health Check pipeline review** — how many calls booked? How many converted to engagements? If conversion is below 20%, the Health Check quality (follow-up email + call playbook discipline) needs attention.
3. **Content performance** — top 3 posts of the month by engagement. Study why. Plan the next 8 posts around that angle.
4. **Update metrics in the Notion ops dashboard** — visitors / posts / connections / calls / engagements / revenue.

---

## What NOT to do

### Do not exceed 15 connection requests per day

LinkedIn flags profiles that do. Acceptance rate plummets. You cannot speed this up — it is a 30-day plan for a reason.

### Do not post more than twice a week in month 1

LinkedIn's algorithm deprioritises rapid-fire posting. Quality + cadence beats quantity.

### Do not DM everyone who accepts your connection request with a pitch

Day-2 DM is the checklist with a useful PDF link. Not a pitch. If they want to talk, they will reply. The Health Check booking link is in your profile's Featured section — prospects can find it themselves when ready.

### Do not respond to Health Check requests in bulk

Every Health Check call is a real commitment — 30 min call + 45 min follow-up writeup. Cap at 5 per week. Three serious prospects treated well beats ten rushed ones.

### Do not skip the Sunday review

The weekly 20 min review is where you notice patterns you would miss in the daily grind. Skipping it turns this into a hamster wheel instead of a compounding system.

---

## First-week specific actions

### Day 0 (before Day 1 starts)

- [ ] LinkedIn profile complete (done ✓)
- [ ] 4 bookmarklets installed (10 min — see `docs/linkedin-bookmarklets.md` + `-v2.md`)
- [ ] LinkedIn Developer App + auth.py complete (Raj, 15 min — see `docs/linkedin-scheduler-setup.md`)
- [ ] First-wave Post 1 (launch story) published — either automatically via scheduler on Apr 22 OR manually today
- [ ] CRM (Notion database or simple Google Sheet) ready with columns: Name, Role, Company, LinkedIn URL, Connection Status, Day-2 DM Sent, Reply, Next Action, Health Check Booked

### Day 1

- [ ] Send 15 connection requests to past colleagues (Segment 1, easiest, ~70–90% acceptance)
- [ ] No pressure on engagement yet — the launch post just went out, people are noticing

### Day 2–5

- [ ] Daily: 15 connection requests (Segment 1 continues)
- [ ] Daily: reply to every accepted connection with Day-2 DM
- [ ] Tuesday: Post 2 (RI coverage tip) publishes
- [ ] Thursday: no post scheduled — take the day off from content, focus on connection acceptance replies

### Day 6–15 (the core of the 30-day plan)

- [ ] Daily: 15 connection requests to CTOs/VPs (Segment 2, ~20–35% acceptance, cold)
- [ ] Daily: one thoughtful comment on a target's post
- [ ] Tue + Thu: posts publish (War story → Market observation → AI/GPU)
- [ ] First Health Checks should start booking around Day 10–14 if content + outreach is working

### Day 16–30

- [ ] Continue the rhythm. Connection segments rotate per the plan.
- [ ] Weekly review on Sundays is non-negotiable.
- [ ] End of Day 30: measure against first-month benchmarks.

---

## First-month benchmarks

If the plan is working as expected:

- **~300 connection requests sent** (15/day × 20 business days)
- **~100 acceptances** (blended 35% across segments)
- **~25 Day-2 DMs that got a reply** (~25% of accepts)
- **~5 Health Check calls booked** (~20% of engaged DMs)
- **1–2 paid engagements closing** (20–40% of Health Checks, typical Month 1 close rate)

**If you hit 1 paid engagement in month 1:** you are on a viable trajectory. Month 2–3 compound.

**If you hit 0:** the outreach mechanics are working but the Health Check → paid engagement step isn't landing. Review the 5 call recordings and follow-up emails with Raj for what to adjust.

---

## Escape valves

**Sick day / busy day:** skip connection requests. Day-2 DMs still go out (they are time-sensitive). Resume the next day.

**Weekend:** optional. Reply to DMs if any are pending, otherwise offline.

**Holiday week:** drop to 5 connection requests per day. Do not publish new posts. Auto-replies on email.

The plan compounds over weeks, not days. A 5% skip rate has no material impact.

---

*AICloudStrategist · Anushka B · Founder-led. Enterprise-reviewed.*
