# 20-Day Sprint to First Customer — V2 (Research-Validated)

**Updated:** 2026-04-17
**Deadline:** 2026-05-07
**Status:** ACTIVE

---

## Assets Ready

- [x] Website live (redesigned — warm cream + teal, Inter font)
- [x] 11 blog posts published
- [x] 6 lead magnets (PDFs) on site
- [x] Email sending via Resend (domain verified, test sent)
- [x] Agent system on VPS (6 agents + watchdog)
- [x] 20 prospects seeded, 5 enriched with real emails
- [x] Mao on Telegram with full project context
- [x] Vikunja tracker live with API
- [x] Weekly digest with Plausible goals
- [ ] X/Twitter account created (pending verification — 1-2 days)
- [ ] WhatsApp Business created (holding to avoid blocking)
- [ ] LinkedIn — blocked (may take weeks)

---

## Strategy: Three Layers Running Simultaneously

### Layer 1 — Warm Outreach (highest probability: 20-30% close rate)

> **Research says:** 80% of first B2B customers in India come from warm networks. WhatsApp has 45-60% conversion vs email 2-5%.

| Day | Action | Owner | Status |
|-----|--------|-------|--------|
| 1-2 | Rajiv/Anushka share 10-20 warm contacts | Human (one-time, 10 min) | ⬜ Pending |
| 1-2 | Mao generates personalized WhatsApp messages per contact | Mao (automated) | ⬜ Ready when contacts shared |
| 3-7 | Anushka sends WhatsApp messages (copy-paste, 30 sec each) | Human (when safe to use) | ⬜ Waiting |
| 7-14 | Mao generates follow-ups for non-responders | Mao (automated) | ⬜ Ready |
| 7-20 | Discovery calls booked via Calendly | Anushka takes calls | ⬜ Ready |

**Expected: 10-20 warm → 6-10 replies → 3-5 calls → 1-2 customers**

---

### Layer 2 — Inbound (medium probability, fully autonomous)

> **Research says:** Content-led inbound + local listings + webinar = 5-15 inbound leads over 20 days.

| Day | Action | Owner | Status |
|-----|--------|-------|--------|
| 1-3 | Cross-post 11 blogs to Dev.to + Hashnode (API) | Mao | ⬜ Needs account signup |
| 1 | Register Google Business Profile | Rajiv (one-time, 5 min) | ⬜ Pending |
| 1 | List on Clutch.co + GoodFirms (free forms) | Rajiv (one-time, 10 min) | ⬜ Pending |
| 1-3 | Build free AWS cost calculator on website (lead capture) | Mao | ⬜ To build |
| 1-20 | Inc42 + YourStory RSS monitor — auto-detect funded companies | Agent (automated) | ⬜ To build |
| 3-20 | X/Twitter: 3 posts/day (after verification) | Agent (API) | ⬜ Pending verification |
| 8 (Apr 22) | Webinar — all infrastructure ready | Anushka hosts | ⬜ Google Meet needed |
| 1-20 | SEO compounding from blog + cross-posts + backlinks | Automated | ✅ Running |

**Expected: 5-15 inbound leads → 2-3 calls → 1 customer**

---

### Layer 3 — Cold Outreach (fully autonomous, needs domain warmup)

> **Research says:** New domains need 4-6 weeks warmup. Cold email to Indian CTOs: 5-12% reply rate best case, 0.5-2% worst. Must use verified contacts only (Apollo.io).

| Day | Action | Owner | Status |
|-----|--------|-------|--------|
| 1-7 | Domain warmup — 2-3 emails/day to known-good addresses | Agent | ⬜ To start |
| 1 | Sign up Apollo.io (100 verified contacts/month free) | Rajiv (one-time, 5 min) | ⬜ Pending |
| 2-5 | Enrich 50 prospects via Apollo API + ZeroBounce verify | Agent | ⬜ Needs Apollo key |
| 8-20 | Send 5 hyper-personalized cold emails/day (verified only) | Agent | ⬜ After warmup |
| 12-20 | Auto follow-ups at day 4/8/14 | Agent | ✅ Built |
| 15-20 | Break-up emails to non-responders | Agent | ✅ Built |

**Expected: 60 verified cold emails → 3-6 replies → 1-2 calls → 0-1 customer**

---

### Layer 4 — Partnerships (compounds over months 2-3)

| Day | Action | Owner | Status |
|-----|--------|-------|--------|
| 5-10 | Email 5 fractional CTOs with free RI Governance Pack | Agent | ⬜ Ready |
| 5-10 | Email 10 CA firms with referral partnership (10% commission) | Agent | ⬜ Ready |
| 10-15 | Email 10 YC India CTO targets | Agent | ⬜ Ready |
| 15-20 | Follow up on partnership responses | Agent | ✅ Built |

**Expected: 25 emails → 3-5 replies → 1 signed partner → warm intros in month 2-3**

---

## Expected 20-Day Outcome

| Source | Calls | Customers |
|--------|-------|-----------|
| Warm WhatsApp | 3-5 | 1-2 |
| Inbound (content + listings + webinar) | 2-3 | 0-1 |
| Cold email (verified) | 1-2 | 0-1 |
| Partnerships | 0-1 | 0 (month 2) |
| **Total** | **6-11 calls** | **1-3 customers** |

---

## One-Time Setup Required (Rajiv — 45 min total, then fully autonomous)

| Task | Time | Unlocks |
|------|------|---------|
| Share 10-20 warm contacts | 10 min | Layer 1 (highest probability) |
| Sign up Apollo.io | 5 min | Verified cold email contacts |
| Sign up Dev.to + Hashnode | 5 min | Content syndication |
| Google Business Profile | 10 min | Local search inbound |
| Clutch.co + GoodFirms listing | 10 min | B2B directory inbound |
| Share API keys with Mao | 5 min | Connects everything |

After setup: **zero human dependency except Anushka taking discovery calls.**

---

## Autonomous Agent System (running on VPS)

| Agent | Schedule | Function |
|-------|----------|----------|
| Orchestrator | 2x daily (09:00 + 15:00 IST) | Coordinates all agents, sends pipeline report |
| Prospector | 10/day | Enriches prospects via web search + Apollo API |
| Outreach | 5-10/day | Generates + sends personalized cold emails |
| Follow-up | Auto at day 4/8/14 | Follow-up sequences |
| Content | Bi-weekly | Drafts blog posts |
| Social | 3 tweets/day + 1 Reddit/week | Community engagement |
| Watchdog | Every 5 min | Health check, auto-restart on failure |

**Pipeline DB:** SQLite at `/docker/agents/shared/db/pipeline.db`
**Daily reports:** Telegram group automatically

---

## Research Sources (validated)

- Cold email India reply rate: 0.5-12% (source: Instantly.ai benchmark 2026, SalesCaptain 2025)
- WhatsApp vs email India: 45-60% vs 2-5% conversion (source: Rasayel, respond.io)
- First customers from warm network: 80% (source: Inc42 founder case studies, SRepublic)
- Domain warmup: 4-6 weeks for new domains (source: Mailtrap)
- Apollo.io free tier: 100 credits/month verified contacts
- CloudKeeper (competitor): $200M ARR proves market exists
- India public cloud market: $29.5B (2024) → $232.8B (2033) at 25.8% CAGR

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| No warm contacts shared | Layer 1 dies (highest probability path) | Push via Telegram daily reminder |
| Domain flagged as spam | Cold email stops | Warmup slowly, max 5/day, verified only |
| Webinar < 10 registrants | Low conversion event | Run anyway, use recording as asset |
| LinkedIn stays blocked | No social proof channel | X/Twitter + Dev.to + community fill gap |
| WhatsApp gets blocked too | Warm outreach channel lost | Fall back to email for warm contacts |
| Zero replies by day 15 | No pipeline | Double down on partnerships + community |

---

## Daily Tracking

Pipeline status via Telegram: send "pipeline status" to Mao bot
Full dashboard: https://tracker.srv1562252.hstgr.cloud
Analytics: https://analytics.aicloudstrategist.com

---

*This plan is maintained by Mao (autonomous AI agent) and updated daily based on pipeline data.*
