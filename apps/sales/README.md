# Sales Assets — AICloudStrategist

Three reusable assets for first-contact-to-close flow:

1. **[01-discovery-call-script.md](01-discovery-call-script.md)** — 30-minute structured script for the first call with a prospect. Discovery → positioning → close with three named next steps. Includes red/green flag checklists and prepared answers to the most common questions.

2. **[02-quickstart-proposal-template.md](02-quickstart-proposal-template.md)** — FinOps QuickStart engagement proposal (₹75K–₹1.5L, 2 weeks). Handlebar-style placeholders (`{{CLIENT_NAME}}`, `{{FEE_IN_INR}}` etc.) for mail-merge or manual fill-in.

3. **[03-gainshare-retainer-proposal-template.md](03-gainshare-retainer-proposal-template.md)** — Managed FinOps Retainer proposal with optional gain-share layer. 12-month term, monthly executive reporting cadence, verified savings framework.

Each has a rendered `.pdf` counterpart styled with AICloudStrategist colours (deep navy + amber), ready to attach directly to prospect emails.

## Workflow

**After a discovery call:**
1. Pick proposal template matching the conversation (QuickStart for first-timers, Retainer for post-QuickStart renewals).
2. Replace the `{{PLACEHOLDERS}}` — takes 10 minutes for QuickStart, 15 for Retainer.
3. Regenerate PDF via `/docker/task-queue/bin/render-sales-pdf.sh <slug>` (if script exists — otherwise manual pandoc + wkhtmltopdf).
4. Send as a dedicated email with the PDF attached — never as a Google Doc link.

## Placeholder cheat sheet

| Placeholder | Typical value |
|---|---|
| `{{CLIENT_NAME}}` | Legal entity name |
| `{{SPEND_LAKH}}` | Current monthly cloud spend in lakhs |
| `{{FEE_IN_INR}}` | 75000 / 100000 / 150000 depending on complexity |
| `{{RETAINER_INR}}` | 40000–80000 typical monthly retainer |
| `{{FLOOR_INR}}` | 100000 monthly savings floor typical |
| `{{GS_PERCENT}}` | 20 default; 25 for complex multi-cloud |
| `{{CAP_MULTIPLIER}}` | 2 default |
| `{{KICKOFF_DATE}}` | 14 days from today minimum |
| `{{GSTIN}}` | Fill once GST registration completes |
| `{{SLOT_1/2/3}}` | Three mutually available kickoff slots |

## Voice

Founder-led. Enterprise-reviewed. INR-first. No hype words. Senior-architect oversight layer referenced as "22+ years of Fortune 500 weight" — **never** claimed as Anushka's personal tenure. See `apps/outreach/playbook.md` for full voice guide.
