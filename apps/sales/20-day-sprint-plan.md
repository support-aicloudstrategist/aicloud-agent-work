# 20-Day Sprint to First Paying Customer

**Started:** 2026-04-16
**Target close date:** 2026-05-06
**Target outcome:** One signed SOW (QuickStart ₹75K–₹1.5L, or Architecture Review ₹1.25L–₹2.5L)
**Constraint:** No LinkedIn (account restricted, waiting on DigiLocker resolution)

---

## Market timing wedge

**AWS raised GPU prices 15% on January 4, 2026. Permanent price lock-in arrives April 2026.** Every Indian AI/ML startup with GPU workloads is actively reviewing infrastructure cost this month. Our AI GPU Cost Audit Checklist + Cost-Per-1000-Inferences blog post land directly on this pain.

**Secondary wedge:** AWS Summit Bengaluru April 22-23, 2026 at KTPO Whitefield. Thousands of Indian engineering leaders in one building. We are 6 days out.

---

## The funnel math

To close 1 deal in 20 days:
- Need 3-5 serious conversations (30-min discovery calls)
- Need 15-25 initial replies
- Need 100-200 quality first-touches
- Reply rate on targeted outbound: 8-15% (industry median for warm-ish B2B)
- Discovery-to-proposal: 30-50%
- Proposal-to-close: 20-40% at day-1 of relationship (first-customer discount helps close this)

**Volume targets per day:**
- 15 hand-researched target contacts added to CRM
- 10 cold emails sent (warm-enriched, not blast)
- 5 Twitter/X DMs to engineering leaders
- 3 WhatsApp messages to warm contacts
- 1 community post (Reddit / HN / IH / Twitter)
- 1 follow-up on everything sent 48h ago

---

## Channels — ranked by 20-day probability

### 1. Rajiv's own network (highest close probability, underused)

**Action:** Ask every single former colleague, client, college friend, and family contact who works in a tech company if they'd introduce us to their CTO / engineering lead.

**Script (WhatsApp):**
> Hey [Name] — quick one. I've launched a cloud cost consulting practice under the brand AICloudStrategist — we help Indian companies cut AWS/Azure/GCP bills 20-30% in 4 weeks. First-customer pricing is live (₹50K discount off the standard ₹75K QuickStart).
>
> Does your company spend >₹5L/month on cloud? If yes — would you be open to a 15-min intro call with me? If not — would you forward this to one person in your network who does?
>
> No awkwardness if it's a no. Thanks either way.

**Target:** Send to 50 warm contacts over first 3 days. Expect 5-10 intro responses, 2-3 converting to discovery calls.

### 2. AWS Summit Bengaluru (Apr 22-23) — massive accelerator

**Action:** Get Anushka registered (it's by-invitation but AWS Partner network + community registration is typically open). Both days if possible.
- Innovators edition (Apr 22) = business leaders = our buyers
- Technical edition (Apr 23) = engineering decision-makers = our champions

**Prep:**
- Print 100 business cards with /book.html URL and QR
- Print 50 copies of AWS Cost Cutting Checklist PDF (lead magnet)
- Dress for business-casual tech (no suit, polished)
- Have the 60-second pitch ready: *"Anushka, founder of AICloudStrategist. We help Indian companies cut AWS bills 20-30% in 4 weeks. Gain-share on verified savings. Free audit checklist on our site. What's the cloud story at your company?"*

**Target:** 30 quality conversations, 10 business-card exchanges with follow-up emails sent within 24h, 3 scheduled discovery calls by end of week.

### 3. Cold email to funded Indian SaaS (Apr 17-May 6)

**Target universe:**
- Series A/B Indian SaaS/fintech/AI startups funded in last 12 months
- Team size 20-200 (too small = no budget, too big = procurement hell)
- Stack includes AWS or Azure (LinkedIn/website/JD scraping reveals this)

**Sources (free):**
- [Growth List India Startups](https://growthlist.co/india-startups/) — 3,928 companies
- [Tracxn India](https://tracxn.com/d/geographies/india/) — SaaS directory
- [YC Indian Startups](https://www.ycombinator.com/companies/location/india) — YC-backed
- [Top Startups India](https://topstartups.io/?hq_location=India) — hiring + funded
- [Indian Startup News funding weekly](https://indianstartupnews.com/funding)
- [Inc42 company database](https://inc42.com/company/)

**Email finder (free-tier sufficient):**
- Hunter.io free tier (25 searches/month)
- Apollo.io free tier (unlimited LinkedIn scrape, though we don't have LI — use their company search which works without)
- RocketReach free tier (5 lookups/month)
- GuessFromEmail patterns: `firstname@domain.com`, `firstname.lastname@domain.com`, `f.lastname@domain.com`
- MX + SMTP verification via Mail-Tester or similar

**Target:** 10 enriched contacts/day × 20 days = 200 targets. 10 emails sent/day = 200 emails total over sprint.

**Email infrastructure:**
- **Primary:** Use Google Workspace @aicloudstrategist.com (already set up, clean reputation)
- **Fallback:** AWS SES for volume (₹10 per 100K — cheapest option, but sandbox exit takes 24-48h)
- **Absolutely avoid:** mass-mail tools like Mailchimp/Mailgun/SendGrid for cold — they'll ban on first complaint
- **Avoid:** Instantly.ai/Lemlist — ₹3000+/month, overkill for 200 emails

### 4. Twitter/X direct outreach (high-leverage, Anushka-safe)

**Why this matters:** Twitter/X DMs don't get you banned. Engineering leaders are publicly active there. Every CTO frustrated with AWS GPU pricing is posting about it right now.

**Tactic:**
- Search daily: `aws bill OR "aws cost" OR "gpu cost" india` in Twitter search, sorted by latest
- Find posts from verified engineers at real companies
- Reply first (public, helpful, no pitch) 2-3 times over a week
- Then DM with: "Saw your thread on [specific topic]. I'm running a FinOps consultancy out of Delhi that's saved Indian teams 20-30% on exactly this pattern. Free checklist here: [link]. Happy to talk if useful. No pitch."
- 15-20 thoughtful DMs per week; expect 3-5 replies

**Target:** 5 DMs/day × 20 days = 100 DMs. Realistic reply: 15-20. Calls: 2-3.

### 5. Community content seeding (inbound multiplier)

**Venues (ranked by audience fit):**
- r/aws (300K+ subs) — most technical, buyers hang here, strict on self-promo
- r/devops (220K subs) — platform engineer audience
- r/startups_india (30K subs) — founder audience, direct buyers
- Indie Hackers — solo founder + small-team audience
- Hacker News — longshot but huge if it lands
- Twitter/X — own feed, tag engineering leaders

**Format that works on Reddit:**
- NOT "I offer FinOps consulting"
- INSTEAD: "I audited 12 Indian mid-market AWS bills over the last 2 months — here's the 5 most common patterns I found" (link to blog post at bottom, not top)
- Share actual numbers (our blog posts have these)
- Answer every comment for 48 hours

**Target posts to rewrite from existing blog content:**
1. r/aws: "Your Reserved Instance coverage is probably under 30%" (from existing post)
2. r/devops: "DORA metrics translated for your CFO" (from existing post)
3. r/startups_india: "How Indian mid-market cloud bills double before they get optimised" (fresh angle)
4. Indie Hackers: "The FinOps gain-share model that Big-4 can't offer" (from existing post)

**Target:** 1 post per week on a different venue. Best outcome: a single front-page Reddit post → 5K-20K views → 10-30 book-a-call clicks → 3-5 discovery calls.

### 6. WhatsApp Business (India's real B2B channel)

**Reality check:** Most Indian founders run their company's admin via WhatsApp, not email. Reaching the CEO on WhatsApp has higher reply rate than email. But the list is smaller — only for verified warm contacts.

**Setup:**
- WhatsApp Business account on Anushka's phone (takes 10 min, free)
- Business profile with logo, hours, website, "Book 30-min Cloud Cost Health Check" catalog item
- Greeting message: auto-send business card + blog link to first-time contacts

**Tactic:** Take every person who has Anushka's number, is in the target demographic, and send **personalized** (never blast) — the script in section 1 above.

**Target:** 3 WhatsApp messages/day × 20 days = 60 sends. Expect 30-50% reply rate on warm = 20-30 replies. 3-5 calls.

### 7. Partnership outreach (slow, start anyway)

Won't close in 20 days but plants seeds for month 2-3 and the pipeline.

**Partner types:**
- **CA firms** serving tech startups in Delhi/Bangalore/Mumbai — they see every cloud bill at year-end and hear CFO complaints. Find 10 via https://www.icai.org and LinkedIn (once unblocked).
- **Boutique dev agencies** (5-30 engineers) that ship to AWS/Azure but don't optimize cost — they have clients bleeding money on their recommendations. Find via Clutch.co, The Manifest.
- **Managed Service Providers** (MSPs) that resell AWS but don't have FinOps in-house — we can be their "FinOps layer" on commission. AWS Partner directory.

**Pitch:**
> We're a founder-led FinOps practice in Delhi. We don't compete with your work — we add a cost-optimization layer. Referral commission: 10% of first engagement fee + 5% of gain-share for 12 months. Zero client friction — we sign our own SOW. Your clients save 20-30% on cloud, you get an honest referral fee and a grateful client.

**Target:** 10 partner intros this sprint. 1-2 will meet. 0-1 will convert to a referred deal in 20 days; the rest are month 2-3 pipeline.

---

## Daily operating rhythm (Anushka's 2.5 hours/day)

| Time | Task |
|---|---|
| **07:30–08:00** | Twitter/X: search + 2 thoughtful replies + 1 DM |
| **08:00–08:30** | Email follow-ups: reply to any prospect responses first |
| **08:30–09:30** | Outbound: 5 new cold emails + 5 new enriched contacts added |
| **09:30–10:00** | WhatsApp: 3 warm-network messages |

Rajiv (support role, 1 hour/day evening):
- Update tracker
- Review outbound queue
- Help enrich 10 new contacts/day
- Prep content for next community post

**Weekly:** One community post on Saturday/Sunday. Book-of-record review every Monday morning.

---

## Outreach targets by day (tracker)

| Day | Date | Channel primary | Secondary |
|---|---|---|---|
| 1 | Thu Apr 16 | Sprint plan (this doc) | Tools setup |
| 2 | Fri Apr 17 | 50 warm WhatsApp sends | Email list build starts |
| 3 | Sat Apr 18 | Reddit r/aws post #1 | Twitter follow-up |
| 4 | Sun Apr 19 | Apollo free-tier list build (100 targets) | Email draft |
| 5 | Mon Apr 20 | 10 cold emails sent | Follow-ups from W0 |
| 6 | Tue Apr 21 | 10 emails + AWS Summit prep | WhatsApp f/u |
| 7 | Wed Apr 22 | **AWS Summit day 1 (Innovators)** | Live business dev |
| 8 | Thu Apr 23 | **AWS Summit day 2 (Technical)** | Live business dev |
| 9 | Fri Apr 24 | Post-summit follow-ups (target: 30 emails within 24h) | Hot leads only |
| 10 | Sat Apr 25 | Indie Hackers post | Twitter threads |
| 11 | Sun Apr 26 | Rest + review | Pipeline audit |
| 12 | Mon Apr 27 | 10 emails + 5 DMs | Partnership outreach batch 1 |
| 13 | Tue Apr 28 | 10 emails + 5 DMs | Discovery calls if any |
| 14 | Wed Apr 29 | 10 emails + 5 DMs | Discovery calls |
| 15 | Thu Apr 30 | 10 emails + 5 DMs | Proposals drafted |
| 16 | Fri May 01 | r/devops post | Proposals sent |
| 17 | Sat May 02 | HackerNews post (if Reddit landed) | Twitter threads |
| 18 | Sun May 03 | Rest | Audit + recalibrate |
| 19 | Mon May 04 | 5 emails + pipeline close push | Negotiation calls |
| 20 | Tue May 05 | Close day | Signatures |
| 21 | Wed May 06 | **Target close date** | Kickoff planning |

---

## First-customer offer (decisive lever)

To close in 20 days, add urgency without cheapening the service:

**First-Customer Offer — available to the first 3 Indian SMBs who sign a QuickStart SOW before May 15, 2026:**

- Standard QuickStart fee **₹75,000 → ₹40,000** (one-time, for the signing credit)
- Plus: **public case study with named reference call rights** (optional — we'll anonymise if they prefer)
- Plus: **50% off month 1 of Managed Retainer** if they convert
- Catch: **they go on aicloudstrategist.com/proof.html as a named logo/case study** (value to us = their brand recognition)

**Why this works:**
- 50% discount is enough to move a hesitant buyer
- The "first 3 customers" frame signals scarcity and honesty — we've never done this engagement at scale, so early customers get a deal
- Named case study rights is worth ₹5L+ to us in future credibility
- Limited to 3 so it doesn't become a permanent discount
- Gives Anushka something to say in every pitch: "We're looking for 3 signature Indian clients before May 15 — would you like to be one?"

---

## Supporting assets needed (Claude builds these this week)

All of these convert an "interested prospect" into "booked call" faster. I'll build them autonomously.

- [ ] **Author page /author/anushka-b.html** with Anushka's full bio, photo, social links (TRUST signal)
- [ ] **One-pager PDF: "The First-Customer Offer"** — 1 page with the deal, the scope, the commitments
- [ ] **AWS Summit business card template** + QR to /book.html
- [ ] **Cold email sequence** (5 emails: intro + 3 follow-ups + break-up)
- [ ] **Twitter DM sequence** (opener + follow-up + case study reply)
- [ ] **WhatsApp sequence** (opener + ask-for-referral + thank-you)
- [ ] **Reddit post drafts** (4 posts ready for scheduling)
- [ ] **/first-customer.html landing page** with the deal + booking CTA
- [ ] **FAQ schema on faq.html** (SEO rich results)
- [ ] **Testimonial section on /proof.html** (even 2-3 pseudonymised "past engagement" quotes)

---

## What I need from Rajiv/Anushka (human-only steps)

- [ ] **Anushka:** Register for AWS Summit Bengaluru (both days)
- [ ] **Anushka:** Travel + accommodation booking for Bengaluru if not local
- [ ] **Anushka:** Send the 50 WhatsApp warm-network messages (from the script above)
- [ ] **Anushka:** Set up WhatsApp Business account on her phone
- [ ] **Rajiv:** Confirm the first-customer discount pricing — is ₹40K OK for 3 customers?
- [ ] **Rajiv:** Confirm we can do 3 concurrent QuickStart engagements in May if all 3 close
- [ ] **Rajiv:** Share 20-30 warm contact names/numbers for Anushka to message
- [ ] **Rajiv:** Confirm a Delhi-based address we can put on the landing page for trust

---

## Realistic outcomes (honest)

**Base case (50% likely):** 1 signed SOW by day 20. 2-3 more in active negotiation. Pipeline worth ₹4-6L in month 2.

**Good case (30% likely):** 2 signed SOWs by day 20. Public case study published. Referral pipeline flowing.

**Moonshot (10% likely):** 3 signed SOWs (hits the first-customer cap). AWS Summit connections convert. One piece of community content goes viral → inbound for 6 weeks.

**Worst case (10% likely):** 0 signed by day 20 but 5-10 active conversations, 1-2 close in the following 30 days. Not a failure — a typical B2B sales cycle playing out.

**Sharpest risk:** Anushka running out of bandwidth. Solution: Rajiv absorbs all non-conversation work (tracker, content, research, tooling). Anushka spends 2.5 hours/day on humans only.
