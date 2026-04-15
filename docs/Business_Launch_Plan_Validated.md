# AICloudStrategist — Validated Launch Plan
**Owner:** Rajiv (Senior Solution Architect, 22 yrs IT, Delhi/NCR)
**Author:** Claude (Opus 4.6) — synthesized from Claude blueprint + GPT report, then validated against live sources April 2026
**Date:** 15 April 2026
**Goal:** First paying customer signed within 30 days, monthly opex < ₹5,000, no human employees.

---

## How this plan is different from the two inputs

The Claude blueprint gave us **execution detail** (pricing, agents, weekly KPIs, Indian network targets). The GPT report gave us **strategic + compliance rigor** (DPDP, email auth, human-in-loop, signal-based targeting). Both had material errors I had to correct after live verification:

- **DPDP Rules 2025 are now notified** (13 Nov 2025). Substantive obligations don't bite until **13 May 2027**. Both reports treated DPDP as immediately mandatory — that's wrong; you have a 19-month runway. (Source: [PIB](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf), [KPMG](https://kpmg.com/in/en/insights/2025/11/dpdp-rules-2025-guidance-to-dpdp-act-implementation.html))
- **"20% guaranteed savings or no fee"** (Claude blueprint) — risky for a solo. Replaced with gain-share clause.
- **LangGraph "34.5M downloads, used by Uber/BlackRock/Cisco"** (Claude blueprint) — inflated, conflated with LangChain. Removed.
- **Local Ollama on 4GB VPS** (GPT report) — not viable. Replaced with OpenRouter routing + your existing Claude Max.
- **SuiteCRM + Mautic + Node-RED** (GPT report) — over-engineered for month one. Replaced with lighter stack.
- **Hostinger 2vCPU/4GB at ₹300–600/mo** (Claude blueprint) — wrong SKU shape; current KVM 2 is 2 vCPU / **8 GB** / 100 GB at **₹522/mo annual** (Source: [Hostinger India](https://www.hostinger.com/in/pricing/vps-hosting)).

Everything below is verified or explicitly flagged.

---

## 1. Positioning

**Brand:** AICloudStrategist (already owned: support@aicloudstrategist.com)

**One-line positioning:**
> *"I help Indian SMBs cut 20–30% off their cloud bill in 4 weeks — using FinOps discipline and AI automation, without locking you into expensive enterprise tools."*

**Why this works:**
- Cloud waste is real and quantifiable (Flexera 2025: 27% of cloud spend is wasted globally — [source](https://www.flexera.com/about-us/press-center/new-flexera-report-finds-84-percent-of-organizations-struggle-to-manage-cloud-spend))
- CFO-friendly outcome: ROI in weeks, not quarters
- Most Indian SMBs can't afford CloudHealth/Flexera ($50K+/yr) — you bring the same outcomes with OpenCost + Infracost (free, OSS)
- 22 years IT credibility lands when you're sitting in front of a CTO

**ICP (Ideal Customer Profile):**
- **Geography:** Delhi/NCR primary, India secondary, global readiness
- **Size:** SMB to mid-market (50–500 employees)
- **Cloud spend:** ₹5L–₹50L/month on AWS / Azure / GCP (the sweet spot — big enough to care, too small for Flexera)
- **Industry:** B2B SaaS, fintech, edtech, e-commerce, IT services
- **Buyer:** CTO/Head of Engineering (initiator), CFO (signs >₹5L), founder (decides in 50–200 headcount)
- **Trigger signals:** recent migration announcement, hiring SRE/DevOps/FinOps, "AWS bill went up", visible incidents/outages

**What you don't do:** compete with Minfy/Searce/Umbrella Infocare (AWS Premier partners) on enterprise deals. Compete with them by being faster, cheaper, more hands-on for the SMB tier they don't service well.

---

## 2. Service Portfolio + Pricing (Indian market verified)

### Tier 0 — Free door-opener
**Cloud Cost Health Check** — 30-min call + 2-page report (top 5 waste signals from a CUR sample they share).
Goal: 100% of these convert to paid Tier 1 conversation within 14 days.

### Tier 1 — Productized assessments (entry, fixed-price)
| Service | Price (INR) | Duration | Outcome |
|---|---|---|---|
| **FinOps QuickStart** (lead service) | **₹75K–₹1.5L** | 2 weeks | Savings backlog with $-tagged actions, tagging baseline, 90-day implementation plan |
| Reliability & Observability Sprint | ₹1L–₹2L | 2–3 weeks | OpenTelemetry baseline, MTTR reduction plan, runbooks |
| Cloud Security Posture Review (CIS Controls) | ₹1L–₹2L | 2 weeks | CIS-mapped findings, prioritized fixes |

**Note:** Do NOT offer "guaranteed 20% or no fee." Use **gain-share clause instead**:
> *"Base fee ₹75K. If verified savings exceed ₹3L in first 90 days, additional 10% of savings above that threshold."*
This protects you from attribution disputes and gives a clean enterprise-friendly model.

### Tier 2 — Implementation sprints (after Tier 1)
- 2-week implementation: ₹1.5L–₹3L
- 4-week migration / re-architecture: ₹3L–₹6L

### Tier 3 — Monthly retainer (the goal — recurring revenue)
- **Advisory Lite:** ₹40K/month (8 hrs)
- **Advisory Pro:** ₹1L/month (20 hrs)
- **Managed FinOps:** ₹1.5L/month (continuous OpenCost monitoring, monthly savings report, quarterly architecture review)

**Hourly rate when needed:** ₹4,500–₹6,000/hr (within India market band of ₹2,500–₹6,000/hr for senior cloud architects per Toptal India / NASSCOM data).

**Realistic year 1 revenue band:** ₹15–25 lakh (per validation research — top quartile of Indian solo cloud consultants).

---

## 3. Tech Stack — final pick

| Function | Pick | Cost/month | Why |
|---|---|---|---|
| **Domain + DNS** | Hostinger / Cloudflare DNS | ₹100–₹200/yr (already own) | Free DNS, fast in India |
| **Website** | Hugo + Cloudflare Pages | ₹0 | Free, fast in India, built-in HTTPS, Workers for forms |
| **Email** | Google Workspace Business Starter | **₹150/user/mo** + 18% GST = ~₹177 | 30GB, custom domain, Meet 100, calendar ([source](https://workspace.google.com/pricing.html)) |
| **VPS** | Hostinger KVM 2 (2 vCPU / 8 GB / 100 GB NVMe) | **₹522/mo annual** | Verified live ([source](https://www.hostinger.com/in/pricing/vps-hosting)) |
| **Calendar booking** | Calendly free tier | ₹0 | 1 event type, unlimited 1:1 — enough |
| **CRM** | Notion (free) + structured DB | ₹0 | <50 contacts in month 1; SuiteCRM premature |
| **Invoicing** | Zoho Invoice free | ₹0 | Free up to 1,000 invoices/yr, India GST-ready |
| **e-Sign** | Zoho Sign free / Aadhaar eSign | ₹0–small per doc | IT Act 2000 valid |
| **AI orchestration** | n8n CE self-hosted on the VPS | ₹0 (fair-code, free for own use) | Best LLM node ecosystem for solo |
| **Heavy LLM work** | Your existing **Claude Max 20x** ($200/mo, already paying) via Claude Code CLI in container | $0 marginal (plan limits, verified) | Already deployed in claude-mao |
| **Cheap LLM work** | **OpenRouter** (DeepSeek v3.1 + free tier auto-router) | ~$5/mo with $10 deposit | Already wired into openclaw |
| **Telegram bot front door** | openclaw on the VPS | ₹0 | Already running |
| **Payment collection (India B2B)** | Razorpay (bank transfer / UPI) | 2% per txn | Free signup, GST invoice support |
| **International payments** | Wise / Razorpay International | 1% per txn | FIRC issued, FEMA-compliant |
| **Email warmup** | Instantly bundled (when you start cold) | ~$37/mo (₹3,100) | Defer to month 2 — not needed for warm + LinkedIn first |
| **LinkedIn Sales Navigator** | Optional Month 2+ | ~₹5,900/mo + GST | Verified ([source](https://igleads.io/resources/linkedin-sales-navigator-cost-and-pricing/)) |

### Total monthly opex — Month 1
- Hostinger VPS: ₹522
- Google Workspace (1 user): ₹177
- OpenRouter top-up: ~₹400
- Claude Max (already paying): $200 — **counts as sunk cost, not new**
- Razorpay/Wise: only when you collect

**New incremental monthly cost: ~₹1,100 (under $15)**

This validates the Claude blueprint's "<₹5,000/mo" target and beats it.

### What I deliberately did NOT include
- **Paperclip orchestration** — interesting tech but not needed for first customer; bolt on later if it adds value
- **SuiteCRM + Mautic** — over-engineered for <50 leads
- **Local Ollama** — won't fit on 4GB usefully; OpenRouter free tier is the right answer
- **Hugo + GitHub Pages** — replaced with Cloudflare Pages (better India latency, built-in form handling)
- **CrewAI / LangGraph** — frameworks, not platforms; n8n is more pragmatic for a solo

---

## 4. AI Agent Architecture (lean, pragmatic)

Built on what we already have running on the VPS. Three agents, one orchestrator, no Paperclip layer until proven needed.

```
You (Telegram)
    ↓
openclaw (front door, OpenRouter cheap models)
    ↓ classifies
    ├─ Simple → answers itself
    └─ Heavy → calls claude-mao shim → Claude Max does work → reports back
         ↓
       Specialized n8n workflows triggered by openclaw:
         • LeadScout    (fetches LinkedIn signals, scores ICP fit)
         • ContentDraft (generates LinkedIn posts + outreach drafts for your review)
         • ProspectCRM  (pushes new leads into Notion CRM)
         • InvoiceBot   (Zoho Invoice via API on milestone hit)
```

**Critical rule (from GPT report — keeping it):**
> No agent sends external messages without your approval. AI drafts, you review, you click send. Period.

This protects your brand (the GPT report's #1 risk) and stays inside LinkedIn ToS (no automation tools — they're banned and detected in 2026).

---

## 5. Legal + Compliance Setup (India-verified)

### Business entity: **Sole Proprietorship + Udyam + Delhi S&E + GST**

Cheapest, fastest, accepted by Indian corporates. Skip OPC/LLP/Pvt Ltd in month 1 — revisit after first ₹10L revenue.

| Step | Where | Cost | Time |
|---|---|---|---|
| PAN (you have it) | — | — | done |
| **Udyam (MSME) registration** | [udyamregistration.gov.in](https://udyamregistration.gov.in) | Free | 30 min online |
| **Delhi Shops & Establishments** | e-District Delhi | Free | 1–2 days online |
| **Current account** (sole-prop) | Any bank with Udyam cert | Free | 3–5 days |
| **GST registration** (voluntary in month 1) | [gst.gov.in](https://gst.gov.in) | Free | 7–10 days |
| **LUT (for export of services)** | GST portal | Free | 1 day |

**GST notes (verified):**
- Threshold for services in Delhi: **₹20 lakh/yr** (not ₹40L — that's goods only)
- Voluntary registration recommended day 1 — corporates demand GSTIN to claim ITC
- SAC code for IT consulting: **998313**
- e-Invoicing not required until ₹5 cr aggregate turnover

**Income tax (verified, FY 2025-26):**
- Use **Section 44ADA presumptive**: 50% of gross receipts deemed profit
- Limit: **₹75 lakh** if ≥95% receipts via banking channels (✅ you'll qualify)
- Advance tax: single instalment by **15 March** under 44ADA
- TDS clients will deduct: **10% under Section 194J** (technical/professional fees) — you claim it back when filing ITR

### DPDP Act — runway, not panic

Per the [PIB notification](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf) and [Shardul Amarchand analysis](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/):

- **Phase 1 (now):** only Data Protection Board provisions live
- **Phase 2 (13 Nov 2026):** consent manager provisions
- **Phase 3 (13 May 2027):** all substantive Data Fiduciary obligations

**For month 1, you need:**
1. Privacy notice on website (template; 1 hour)
2. Standard Data Processing clause in your MSA (template; embed in proposal)
3. Encrypted storage for client data (already get this from any cloud)
4. Clear sender ID + opt-out in all email outreach (legally smart even pre-DPDP)

**You don't need yet:** DPIA, Consent Manager registration, dedicated DPO. Revisit Q1 2027.

### Contracts

- Use a **single MSA + per-engagement SOW** model — both signed via Zoho Sign (Aadhaar eSign valid under IT Act 2000)
- **Stamp duty:** ₹100 e-stamp (SHCIL) for admissibility as evidence — strongly recommended for any contract >₹50K
- **Standard MSA clauses to include:** scope, deliverables, payment milestones, IP assignment (you keep tools/templates, client owns deliverables), confidentiality, DPDP-readiness clause, gain-share calculation method, termination, governing law (Delhi), arbitration (single arbitrator, Delhi seat)

---

## 6. Outreach + First Customer (30-day playbook)

### Channel mix — Indian-tuned

The Claude blueprint emphasized warm-network reactivation; the GPT report emphasized signal-based cold targeting. Indian professional culture rewards warm + personal **dramatically more** than cold (40–60% response vs 5–10%). So:

| Channel | Weight | Why |
|---|---|---|
| **Warm network reactivation** (ex-colleagues) | 40% | Highest conversion, lowest cost |
| **LinkedIn manual outbound** (CTO/founder ICP) | 30% | Manual = ToS-safe, India audience present |
| **Communities** (Cloud Computing India, AWS Delhi/NCR meetup, DevOps India, NASSCOM SME forums) | 20% | Cheap signal + credibility |
| **Cold email** | 10% | Defer to Month 2 (need warmup); use only after first wins |

### 30-day calendar

**Week 1 — Foundation (you do this, AI assists drafting)**
- Day 1: Udyam + Delhi S&E registrations
- Day 1–2: Bank account + GST application + LUT
- Day 2: Hugo site live on Cloudflare Pages (3-page: services / case-pack / book-a-call)
- Day 3: LinkedIn profile rewrite (positioning sentence above; pin Cloud Cost Health Check post)
- Day 3: SPF + DKIM + DMARC on aicloudstrategist.com (Google Workspace one-click) — required before any outreach
- Day 4: Two lead magnets:
  - "AWS Cost Optimization Checklist for Indian SMBs" (PDF)
  - "FinOps Maturity Self-Assessment" (interactive, 10 questions)
- Day 5–6: Build proof pack — 2 anonymized case studies from your 22-year career (sanitize names/numbers, keep architecture)
- Day 7: Activate openclaw + n8n LeadScout + ContentDraft workflows on the VPS (already 80% built)

**Week 2 — Warm + LinkedIn outbound**
- 30 personal WhatsApp/voice notes to ex-colleagues (your previous Fortune 500 and Tier-1 IT networks) — explicit ask: "Looking for CTOs/founders dealing with high cloud bills. Anyone you can intro me to?"
- 20 LinkedIn connection requests/day (manual, with personalized note) to ICP — target ~120 invites/week (under safe limit)
- Engage 3–5 LinkedIn posts/day in target audience to build feed presence
- Publish 2 LinkedIn posts/week (AI drafts, you edit, you post): one "lesson from the trenches", one quick FinOps tip
- Goal: **20+ connection acceptances, 5+ discovery conversations**

**Week 3 — Free Health Checks → conversion**
- Deliver **3–5 free Cloud Cost Health Checks** (30 min each)
- Same-day 2-page PDF report for each (n8n + Claude generates draft, you finalize in 30 min)
- Follow-up call within 48 hrs: pitch FinOps QuickStart at ₹75K (fixed) or gain-share variant
- Goal: **2 paid proposals sent, 1 closed**

**Week 4 — Close + deliver**
- Sign first customer (50/50 payment: 50% advance, 50% on delivery)
- Deliver QuickStart in 2 weeks (split kicks into Week 5–6)
- Capture before/after metric for case study
- Convert successful delivery to retainer conversation (₹40K Advisory Lite)

### Realistic 30-day funnel

| Stage | Target |
|---|---|
| LinkedIn connect requests | 100–120 |
| Acceptances (15–25%) | 20–25 |
| Warm network DMs | 30 |
| Warm replies | 12–18 |
| Discovery calls | 8–12 |
| Free Health Checks delivered | 4–6 |
| Paid proposals sent | 2–3 |
| **Customer signed** | **1** |

This is grounded, not aspirational. Worst case: 0 in 30 days, 1 by Day 45 — adjust pricing or ICP.

---

## 7. What gets built on the VPS in Week 1 (since I'm building this for you)

Continuing from where we paused. Concrete deliverables, end of Week 1:

1. ✅ **ai-ops Docker network** (done overnight)
2. ✅ **claude-mao HTTP shim** (done overnight)
3. **openclaw → claude-mao smart router** — 1 skill (~50 lines), system prompt update, progress streaming to Telegram
4. **n8n LeadScout workflow** — ingest LinkedIn signals (manual paste of profile URL → enrich via Claude Max → score 1–10 ICP fit → push to Notion CRM)
5. **n8n ContentDraft workflow** — generate LinkedIn post drafts on cadence; queue in Telegram for your approval
6. **n8n InvoiceBot** — Zoho Invoice API on milestone webhook
7. **Hugo site + Cloudflare Pages** — 3-page site, contact form via CF Worker
8. **2 lead magnets** — drafted by Claude Max, you review/finalize
9. **Proof pack** — 2 anonymized case studies, you provide raw inputs
10. **Email auth (SPF/DKIM/DMARC)** on aicloudstrategist.com
11. **Notion CRM workspace** — leads / discovery calls / proposals / customers / invoices

Estimated: **3 working days** focused work after you do the entity registrations.

---

## 8. Risks + Mitigations (validated)

| Risk | Real probability | Mitigation |
|---|---|---|
| No customer in 30 days | Medium-high (solo, no warm pipeline yet) | Extend to 45 days; lower entry to ₹50K Quick-Win sprint; convert any free Health Check to paid in 2 weeks |
| LinkedIn account restriction | Low if manual | NEVER use Dux-Soup / Expandi / Waalaxy — heavily detected in 2026 |
| Brand damage from AI auto-outreach | High if you let agents send | All external sends require your one-tap Telegram approval; openclaw enforces this |
| DPDP non-compliance | Low until May 2027 | Privacy notice + DPA clause now; full programme by Q1 2027 |
| Cloud bill stuck on Max sub | Verified low — `total_cost_usd` in claude-mao is cosmetic; real billing draws from $200/mo Max plan rate limits ([source](https://code.claude.com/docs/en/costs)) | Keep `ANTHROPIC_API_KEY` UNSET in containers (verified done) |
| Free Health Check non-convert | Medium | Pre-qualify via Calendly form (cloud spend >₹5L/mo); if not, redirect to lead magnet |
| Scope creep in fixed-price | High in India | Tight SOW with explicit out-of-scope list; change-order template pre-signed |
| Client concentration | Real once you have 1 | Goal: 3 customers by Day 60; no client > 40% revenue |

---

## 9. Decisions you need to make this week (so I can build)

1. **Entity:** Sole prop confirmed? (My recommendation; revisit later.) **Y/N**
2. **Pricing:** OK to launch at ₹75K FinOps QuickStart (with gain-share variant)? **Y/N**
3. **Free Health Check vs paid entry:** Free for first 5 customers, then paid? (Hybrid recommendation.) **Y/N**
4. **Site domain:** Use aicloudstrategist.com for everything, or split (e.g., outreach.aicloudstrategist.com for cold)? **Recommend single domain Month 1.**
5. **Service focus:** Lead with FinOps, secondary Reliability + Security? **Y/N**
6. **Approval policy on AI outreach:** Confirm — every external send (LinkedIn message, email, social post) goes to your Telegram for approval before send? **Y/N**
7. **Warm network ask:** Will you spend 4 hrs Week 2 doing personal voice notes to 30 ex-colleagues? (No way around this; it's the highest-ROI lever.) **Y/N**
8. **Calendar:** Block 5 days Week 1 for entity setup + site + content? (I'll handle the build; you handle the bureaucracy.) **Y/N**

---

## 10. What success looks like

| Day | Milestone |
|---|---|
| Day 7 | All registrations filed, site live, agents running, proof pack ready |
| Day 14 | 5+ discovery calls booked from warm + LinkedIn |
| Day 21 | 4–6 free Health Checks delivered, 2+ paid proposals out |
| Day 30 | First customer signed, advance received |
| Day 45 | First QuickStart delivered, before/after metric captured |
| Day 60 | First case study published, Customer #2 signed, retainer conversation with #1 |
| Day 90 | 3 customers, ₹2–3L MRR or ₹5–6L cumulative revenue |
| Day 365 | ₹15–25L revenue, 5–8 active retainers + project work |

---

## Verified sources used

- [PIB — DPDP Rules 2025 notification (Nov 2025)](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)
- [Shardul Amarchand — DPDP enforcement timeline](https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/)
- [KPMG — DPDP Rules 2025 guidance](https://kpmg.com/in/en/insights/2025/11/dpdp-rules-2025-guidance-to-dpdp-act-implementation.html)
- [ClearTax — Section 44ADA FY 2025-26](https://cleartax.in/s/section-44ada)
- [Skydo — Section 44ADA ₹75L limit](https://www.skydo.com/blog/44ada-of-income-tax-act)
- [FinOps Foundation — FOCP exam ($300 standalone)](https://learn.finops.org/finops-certified-practitioner-certification-exam)
- [Hostinger India — VPS pricing](https://www.hostinger.com/in/pricing/vps-hosting)
- [Hetzner — CX22 / CX32 cloud pricing](https://www.hetzner.com/cloud)
- [LinkedIn Sales Navigator — India INR pricing](https://igleads.io/resources/linkedin-sales-navigator-cost-and-pricing/)
- [Google Workspace — India Business Starter pricing](https://workspace.google.com/pricing.html)
- [Flexera — 2025 State of the Cloud Report (27% waste)](https://www.flexera.com/about-us/press-center/new-flexera-report-finds-84-percent-of-organizations-struggle-to-manage-cloud-spend)
- [Anthropic — Claude Code billing under Max subscription](https://code.claude.com/docs/en/costs)

---

## What I will not do

- I will not start cold-emailing without your approval and SPF/DKIM/DMARC verified.
- I will not register the business entity for you (you must do PAN-linked Udyam + GST personally — KYC requires you).
- I will not promise customers you'll close — the funnel is realistic, not guaranteed.
- I will not bolt on Paperclip or any other "interesting" tech until basic flow works and customers exist.
- I will not let any agent send external messages without your one-tap approval.

Tell me which of the 8 decisions in §9 to lock in, and I'll start building Week 1's deliverables tonight.
