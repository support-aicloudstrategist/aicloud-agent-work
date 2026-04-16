# Webinar Registration Flow + Reminder Emails

**Purpose:** convert /webinar.html visitors → registered attendees → call bookings.

**Event:** *Is Your AWS Bill 2x Your Projection?* — Tuesday 22 April 2026, 16:00 IST, 45 minutes via Google Meet.

**Target:** 20 registrants, 10 actual attendees, 2-3 post-event discovery calls.

---

## Registration form (Google Form, free, 15 min setup)

**Form title:** *Is Your AWS Bill 2x Your Projection? — Free Webinar Registration*

**Form description:**
> Tuesday 22 April 2026, 16:00 IST. Google Meet. 15 min content + 30 min open Q&A. Limited to 50 attendees so Q&A stays useful. We'll send the recording + slides within 24 hours of the session.

**Fields (minimum, to maximise signup conversion):**

1. **Full name** *(required, short answer)*
2. **Work email** *(required, short answer, email validation)*
3. **Company name** *(required, short answer)*
4. **Your role** *(required, dropdown):*
   - CTO / VP Engineering / Head of Infrastructure
   - Engineering Manager / Platform Lead
   - SRE / DevOps Engineer
   - CFO / Finance Lead
   - Founder / CEO
   - Other (specify)
5. **Rough monthly cloud spend** *(required, dropdown):*
   - Under ₹2 lakh
   - ₹2-5 lakh
   - ₹5-10 lakh
   - ₹10-25 lakh
   - ₹25-50 lakh
   - Over ₹50 lakh
   - Not sure
6. **Your top cost concern right now** *(optional, long answer):*
   - *Placeholder: "What's the specific cost question you'd want Anushka to tackle in the Q&A?"*

**After submission:**
- Redirect to confirmation URL: `https://aicloudstrategist.com/webinar-confirmed.html` (we'll build this in 5 min)
- OR show standard "Thank you" screen with Meet link included

**Response settings:**
- Collect email addresses: ON
- Send respondents a copy of their response: ON (this serves as automatic first confirmation)
- Limit to 1 response per account: OFF (allow multiple for team registrations)

**Link placement:** update `/webinar.html` to replace `REPLACE_WITH_GOOGLE_FORM_URL` with the real Google Form URL.

---

## Email reminder sequence (5 emails, fully drafted)

Anushka can set these up either manually in Gmail (5 scheduled emails) OR via a Google Apps Script attached to the form. Manual is fastest for 20 registrants.

### Email 1 — Immediate on registration (auto-sent by Google Form)

Google Form's built-in "send respondents a copy" handles this. No additional work needed.

### Email 2 — Day of registration (within 1 hour)

**Subject:** `[Confirmed] Webinar Tue 22 Apr — Google Meet link inside`

**Body:**

```
Hi {firstname},

Thanks for registering for the webinar on Tuesday 22 April.

Here is everything you need:

• Date/time: Tuesday 22 April 2026, 16:00 IST
• Duration: 45 minutes (15 min content + 30 min Q&A)
• Google Meet link: {PASTE_MEET_LINK}
• Calendar invite: attached (.ics)

Quick ask: if there's a specific cost question you want answered in the Q&A, reply to this email with it. I pre-plan the Q&A order so questions from registrants go first.

Bonus: attaching our AWS Cost Cutting Checklist PDF. Useful either way — whether you attend live or watch the recording later.

See you Tuesday.

Anushka B
Founder, AICloudStrategist
aicloudstrategist.com
```

**Attach:** aws-cost-cutting-checklist-indian-smbs.pdf (already on our VPS at /var/www/aicloudstrategist/downloads/)
**Attach:** calendar.ics file for the event (generate via Google Calendar → Add event → Get shareable link → Export ICS)

### Email 3 — 24 hours before (Monday 21 April, 16:00 IST)

**Subject:** `Tomorrow 16:00 IST — the webinar we're running + a preview`

**Body:**

```
Hi {firstname},

Quick reminder: the webinar is tomorrow (Tuesday 22 April) at 16:00 IST.

Meet link: {PASTE_MEET_LINK}

Preview of what we'll cover in the 15 minutes of content:

1. Reserved Instance coverage — why 70% of Indian mid-market accounts are under 30%
2. Cross-region egress — the one Terraform flag that quietly 3x'd a GCP bill
3. Orphaned EBS volumes — 38 volumes, ₹4.2 lakh/year, in accounts nobody had reviewed
4. Tagging coverage gaps — 20-35% of spend sitting in untagged resources
5. GPU over-provisioning — given the April 2026 AWS price hike

The full 30 minutes after that is your questions. If you have a specific cost question you'd like tackled first, reply now — I batch them in advance.

See you tomorrow.

Anushka
```

### Email 4 — 2 hours before (Tuesday 22 April, 14:00 IST)

**Subject:** `Starting in 2 hours — webinar meet link`

**Body:**

```
{firstname}, webinar starts at 16:00 IST (in 2 hours).

Meet link: {PASTE_MEET_LINK}

Pre-call tip: have your AWS Cost Explorer open in another tab. The first diagnostic we'll discuss can be run in 10 seconds against your own account.

See you shortly.

Anushka
```

### Email 5 — Same day, 1 hour after end (Tuesday 22 April, 18:00 IST)

**Subject:** `Thanks for attending — recording, slides, and the next step`

**Body (for attendees):**

```
Hi {firstname},

Thanks for joining the webinar. Three things in this email:

1. Recording: {PASTE_RECORDING_LINK}
2. Slides (PDF): attached
3. Follow-up

On the follow-up: for the first 3 companies who sign a FinOps QuickStart engagement with us before 15 May 2026, we are running a first-customer offer — 50% off standard pricing (₹40K vs ₹75K) in exchange for named case study rights. Two weeks, ranked backlog, open-source tooling, founder-led.

Details: https://aicloudstrategist.com/first-customer.html

If you'd like to talk specifics for your account, book a free 30-min Cloud Cost Health Check:
https://aicloudstrategist.com/book.html

Either way — your attendance was valuable, and I hope the session surfaced at least one pattern worth checking on your own bill.

Anushka B
```

**Email 5 variant — for no-shows (subject: `Missed the webinar — here's everything`):**

```
Hi {firstname},

Sorry we missed you on the webinar earlier today. Things happen.

Everything's here:

• Recording: {PASTE_RECORDING_LINK}
• Slides (PDF): attached
• AWS Cost Cutting Checklist (PDF): attached

If anything in the recording resonates and you'd like a direct 30-minute conversation about your own account, book here: https://aicloudstrategist.com/book.html — no pitch, just patterns and priorities.

Also heads up: we're running a first-customer offer for the first 3 companies to sign a QuickStart engagement by 15 May — 50% off standard pricing. Details at https://aicloudstrategist.com/first-customer.html if useful.

Anushka B
```

### Email 6 (optional) — 7 days after (Tuesday 29 April)

**Subject:** `One pattern from last week's webinar — worth a 10-min check`

**Body:**

```
Hi {firstname},

Following up one week later on the webinar with a single specific ask: have you had a chance to run the Cost Explorer RI coverage check?

Takes 10 minutes:
1. AWS Cost Explorer → Reservations → Utilization report
2. Filter last 30 days
3. Read the "Net RI savings" number against total compute spend
4. Below 40% → worth a conversation

If yours is below 40%, the gap is typically ₹2-8 lakh/month for Indian mid-market accounts. If you want to walk through what it is for your specific stack, I have 30 min slots open this week: https://aicloudstrategist.com/book.html

No pressure if not — just checking in.

Anushka
```

---

## Promotion checklist (get registrations IN)

**Week before webinar (Apr 15-21):**

- [ ] Post /webinar.html link on Anushka's Twitter/X — 3 times across the week
- [ ] WhatsApp message to 50 warm contacts (use the webinar as a lower-commitment entry point than a sales call)
- [ ] Include webinar registration CTA in the Sunday Reddit r/aws post body
- [ ] Email the 100-target list (2nd email in sequence, adapted for webinar invitation)
- [ ] Post in AWS User Group Delhi meetup group (once joined)
- [ ] Post in FinOps Connect channel (once joined)

**Day of webinar:**
- [ ] Rajiv posts on /book.html booking confirmations redirect → webinar reminder
- [ ] Twitter post 2 hours before

---

## Post-webinar assets to generate

1. **Recording** — Google Meet records to Drive automatically if host enables. Download, trim, upload to a public Drive link or YouTube (unlisted).
2. **Slides PDF** — export from whatever deck tool Anushka uses (Google Slides / Canva).
3. **Summary blog post** — 2 days after webinar, publish blog post summarising the 5 patterns + linking recording. Extends the content's lifetime from 45 minutes to permanent.
4. **Attendee list** — export from Google Form, import to Vikunja as a task each: `Lead: {name} at {company} attended webinar`.

---

## Success metrics

**Registrations:**
- Floor: 20
- Target: 35
- Stretch: 50

**Attendance rate (typical for free webinars):** 40-55%

**Post-webinar conversion (attendee → discovery call):**
- Floor: 1-2 calls booked
- Target: 3-5 calls
- If we hit target: this single webinar pays for the whole week of outbound work

---

## If it flops (fewer than 10 registrants by day 5)

1. Don't cancel — run it anyway for whoever signed up, record it, use the recording as a repurposable asset
2. Double the Twitter/WhatsApp promotion push for the final 48 hours
3. Offer 1:1 calls to any registered attendee who can't make the time slot
4. Learn: was the angle too generic? Too specific? Time slot wrong? Revise for next webinar in 30 days.

---

## Next webinar (after Apr 22)

Run one per month for the first 3 months of the sprint. Topics:

- **May:** *The RI Coverage Governance Framework — An Afternoon Meeting That Recovers ₹2-8L/month*
- **June:** *DORA Metrics Translated for Your CFO — Getting DevOps Funded in 2026*
- **July:** *Cost-Per-1000-Inferences — The One Number Every Indian AI Team Should Know*

Each webinar = 20-50 registrants = 3-5 new top-of-funnel conversations per month.
