# Plausible Analytics Goals Setup

**Current state:** Plausible self-hosted at analytics.aicloudstrategist.com tracks pageviews + engagement (time-based). No conversion goals configured yet.

**What we want:** 5 conversion goals that tell us which pages drive what actions, so we can measure the sprint ruthlessly.

---

## Goal 1 — Webinar registration (page-view goal)

**Name:** `Webinar Registration`
**Type:** Pageview
**Page URL pattern:** `/webinar-confirmed.html`
**Why this works:** Google Form redirects the user here after successful submission. Pageview on this URL = confirmed registration. Clean conversion event, no JavaScript wiring needed.

**Expected volume:** 20-50 registrations per webinar × 1 webinar/month = 20-50 goal completions/month

---

## Goal 2 — Discovery call booking started (page-view goal)

**Name:** `Discovery Call Booking Started`
**Type:** Pageview
**Page URL pattern:** `/book.html`
**Why:** Anyone who lands on /book.html is high-intent. Even if they don't complete the Calendly booking, landing on this page is a stronger conversion signal than landing on /services.html.

**Expected volume:** 30-100 visits/month as traffic scales

---

## Goal 3 — First-customer offer viewed (page-view goal)

**Name:** `First-Customer Offer Viewed`
**Type:** Pageview
**Page URL pattern:** `/first-customer.html`
**Why:** Tracks whether our scarcity landing is getting eyeballs. High-intent visitors who read this page are much more likely to book than general traffic.

**Expected volume:** 20-80 visits/month

---

## Goal 4 — Download lead magnet (outbound link goal)

**Name:** `Lead Magnet Download`
**Type:** Custom event — outbound link click
**Trigger:** Any click on `/downloads/*.pdf` (captured automatically by plausible-outbound-links.js script which is already loaded on our pages)

**Why:** Lead-magnet PDFs downloaded = top-of-funnel signal even without form-fill. Combined with referrer data, tells us which marketing channel produces real engagement.

**Setup in Plausible admin UI:**
- Goal type: "Custom event"
- Event name: `File Download` (default Plausible outbound-file event name)
- Optional filter: `URL contains "/downloads/"`

**Expected volume:** 10-50 downloads/month

---

## Goal 5 — Author page view (page-view goal, proxy for E-E-A-T interest)

**Name:** `Author Page Viewed`
**Type:** Pageview
**Page URL pattern:** `/author/anushka-b.html`
**Why:** Visitors who click through to read about Anushka = evaluating credibility. Correlates to conversion intent. Low volume but every visit is meaningful.

**Expected volume:** 5-20 visits/month

---

## How to configure these goals (5 min in Plausible admin)

Rajiv does this ONCE in the Plausible admin UI:

1. Log in to https://analytics.aicloudstrategist.com (admin account)
2. Go to site settings for `aicloudstrategist.com`
3. Click "Goals" tab
4. For each goal above:
   - Click "Add Goal"
   - Select type (Pageview for URL goals, Custom event for file downloads)
   - Paste the path (for URL goals) or event name (for custom)
   - Save
5. Verify by visiting each URL manually → refresh the Goals panel → count should increment

**Total time:** 5 minutes for all 5 goals.

---

## How to use the goals once configured

### Weekly review (Monday mornings)

- Check Goals panel for last 7 days
- Answer three questions:
  1. Which traffic source produced the most goal completions?
  2. Which page had the highest conversion rate to goal?
  3. Any anomalies (10x spike or drop vs. prior week)?

### Tracking sprint success

Minimum sprint targets (through 6 May 2026):

| Goal | Floor | Target | Stretch |
|---|---|---|---|
| Webinar Registration | 15 | 30 | 50 |
| Discovery Call Booking Started | 20 | 40 | 80 |
| First-Customer Offer Viewed | 30 | 75 | 150 |
| Lead Magnet Download | 30 | 80 | 200 |
| Author Page Viewed | 10 | 25 | 50 |

Hitting Floor on every goal = sprint is working. Hitting Target on 3+ = on track for first customer. Hitting Stretch on 2+ = signed SOW almost certain.

---

## Weekly digest integration

Update `/docker/task-queue/bin/weekly-digest.sh` (already runs every Monday 09:00 IST) to include goal completions in the weekly Telegram summary.

Add this ClickHouse query to the existing script:

```bash
GOAL_EVENTS=$(query_db "
SELECT name, count() AS c
FROM plausible_events_db.events_v2
WHERE site_id = 1
  AND name != 'pageview'
  AND timestamp >= '${SINCE}'
  AND timestamp <= '${NOW}'
GROUP BY name
ORDER BY c DESC
FORMAT TabSeparated
")
```

Include in the Telegram message block:

```bash
MSG="${MSG}

Conversions this week:
${GOAL_EVENTS:-none}
"
```

(Optional — I'll update weekly-digest.sh next if useful.)

---

## Tracker task

```bash
vk add 7 "Configure 5 Plausible goals in admin UI (5 min)" "See 16-plausible-goals-setup.md. Goals: Webinar Reg, Discovery Booking, First-Customer View, Lead Magnet Download, Author Page View."
vk label <id> rajiv-owns
vk prio <id> 3
```
