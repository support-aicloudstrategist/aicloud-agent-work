# WhatsApp Outreach Sequence — Warm-Network First, Then 2nd Degree

**Core principle:** WhatsApp is India's real B2B channel. Higher reply rate than email, lower latency, higher trust — **but only with people who already have your number**. Never cold-blast; only message people who have reason to recognise the sender.

**Rule:** Every WhatsApp message is personalised, from Anushka's own phone, via WhatsApp Business. Never use bulk broadcast tools (violates ToS, account gets banned).

---

## Setup checklist (5 minutes)

1. On Anushka's phone, download WhatsApp Business (free, separate from personal WhatsApp)
2. Register with her business number (could be same as personal, but recommended: get a dedicated SIM for business if feasible)
3. Fill business profile:
   - Name: **Anushka B — AICloudStrategist**
   - Description: *"Cloud cost optimisation for Indian mid-market. Free 30-min Cloud Cost Health Check. Rohini, Delhi."*
   - Website: aicloudstrategist.com
   - Address: Rohini, Delhi 110085
   - Business hours: 10am–6pm IST, Mon–Fri
   - Business category: IT services
4. Set greeting message (auto-sent to first-time contacts):

```
Hi — thanks for reaching out. Anushka here from AICloudStrategist.

Quick context: I run a founder-led cloud cost consultancy out of Delhi. We help Indian companies cut AWS / Azure / GCP bills 20-30% in four weeks.

Happy to chat whenever works for you. If you want to skip ahead and book a free 30-min Cloud Cost Health Check, it's at aicloudstrategist.com/book.html.

I reply to all messages within the business day. — A
```

5. Set quick replies for common questions (saves typing):
   - `/pricing` → pricing link
   - `/checklist` → AWS Cost Cutting Checklist PDF
   - `/book` → booking link
   - `/about` → 3-line positioning

---

## Message 1 — Warm-Network Opener (Day 1-3 push)

Send to every single person in Anushka's phone contacts who works in tech. Target 50 sends across 3 days.

```
Hey {firstname} — Anushka here.

Quick update: I've officially launched my cloud cost consultancy under the brand AICloudStrategist. We help Indian companies cut their AWS / Azure / GCP bills 20-30% in about four weeks. Founder-led delivery, senior-architect reviewed.

Two asks, no obligation either way:

1. Does your company (or any company you know) spend over ₹5 lakh/month on cloud? If yes, I'd love a 15-min intro call — I'm offering a free 30-min Cloud Cost Health Check to first-time contacts.

2. If it's not you — would you forward this to one person in your network who might care?

Either way, good to reconnect. Site's at aicloudstrategist.com if you want to have a look.
```

**Customisation rules:**
- Replace {firstname} always
- Add ONE specific personal note before this — how you know them / last time you met / shared context
- If you can't remember how you know them, skip the send. Don't fake warmth.

---

## Message 2 — Referral Ask (5 days after Message 1 if they replied warmly)

Send only if they replied positively but their own company isn't a fit.

```
Appreciate the note {firstname} — genuinely.

Can I make one more ask: if you think of even one person in your network who fits (Indian SaaS/AI/fintech, engineering leader, running AWS or Azure, spending >₹5L/month) — would you pass my details on?

I'll make sure they have a good experience either way. And I owe you one.
```

---

## Message 3 — Introduction Accepted (when they introduce you)

When {referrer} introduces Anushka to {newcontact} in a group chat:

```
Thanks for the intro {referrer} — taking this off the group so we don't clog it up.

Hi {newcontact}, Anushka here from AICloudStrategist. {referrer} thought you'd be worth a conversation — really appreciate that.

Quick question so I can tailor the conversation: is {newcontact's company} on AWS, Azure, GCP, or a mix? And is there a specific cost pressure happening right now, or is it more a general audit?

I have some time Wed / Thu afternoon IST — would a 30-min call work? You can grab a slot directly: aicloudstrategist.com/book.html — or just reply with what works.
```

**Then immediately DM {referrer} separately:**

```
{referrer} — genuinely grateful for the intro. I'll keep you posted on how it goes. If it converts, I'd like to send a small thank-you (not awkward — an honest referral fee or a gift, your preference).
```

---

## Message 4 — Post-Call Follow-up (within 2 hours of discovery call)

```
Hey {firstname} — great chatting.

Quick summary of what I heard:
• {one-line recap of their current cloud stack}
• {one-line recap of their cost pressure / trigger}
• {what they said they wanted next}

Based on that, I'd suggest we do a FinOps QuickStart — 2 weeks, ₹75K flat (or ₹40K if we close within our first-customer window — details: aicloudstrategist.com/first-customer.html).

Proposal coming to your email in the next 2 hours. Any questions before you see it, drop them here.
```

---

## Message 5 — Gentle Nudge (Day 3 after proposal, if no reply)

```
Hey {firstname} — quick nudge on the proposal from {day}. Any questions I can clear up? Happy to walk through any section on a 10-min call if useful.

No pressure on timing.
```

---

## Message 6 — Honest Close (Day 14 after proposal, if still no reply)

```
{firstname} — going to stop nudging, don't want to overstay.

If {company} decides to move forward any time this quarter, the ₹40K first-customer pricing is good through May 15. After that it's back to ₹75K, which is still a reasonable deal but just heads up.

Thanks for the conversation regardless — means a lot as we're getting off the ground.
```

---

## What NOT to send via WhatsApp

- PDFs or large files (goes to "Document" view which people ignore — use a link instead)
- Multiple messages in quick succession (comes across as spammy)
- Voice notes unless specifically requested (many Indian professionals find unrequested voice notes presumptuous in business contexts)
- Messages after 8pm or before 9am IST
- Messages on Sundays
- Any automation (bulk-send, auto-reply beyond greeting, scheduled blasts)

---

## Reply handling

- **Within 2 hours during business hours:** reply with substantive text, not just emoji
- **Outside business hours:** greeting message auto-handles it; reply manually next business morning
- **If they ask for pricing without a call first:** quote standard public pricing + offer a 15-min call to scope. Never negotiate over text.
- **If they're clearly cold/not interested:** thank them graciously, ask if you can follow up in 6 months, don't keep pushing
- **If they're a clear competitor:** polite acknowledgement, no more detail. "Appreciate the note — we're all solving this in our own way. Let me know if there's ever an angle where we'd both win."

---

## Tracking

Every new WhatsApp conversation → create a task in Vikunja tracker:
```
vk add 7 "WhatsApp lead: {firstname} at {company}" "First message: {date}. Status: {warm/cold/replied/booked/proposal}."
vk label <task_id> waiting-on-anushka
vk prio <task_id> 4
```

Weekly review with Rajiv — which conversations need a nudge, which are stalled, which should be marked dead.

---

## Forbidden (account-safety)

- **Don't use WhatsApp Web bulk broadcast** — against ToS, gets accounts flagged
- **Don't send to numbers you pulled from web scraping / lead-gen tools** — WhatsApp treats unsolicited business messages as spam, reports by recipients ban accounts
- **Don't use any 3rd-party WhatsApp automation tools** — same risk profile as LinkedIn Comet situation; learned that lesson already
- **Only message people who have a reason to recognise you** — the number must exist in their contacts from prior interaction, OR they just gave it to you via a mutual intro
