# aicloud-foundation

Source of truth for the AICloudStrategist business — Anushka B's cloud consulting practice. Founder-led. Enterprise-reviewed.

This folder is the **local dev mirror** of the GitHub repo at
https://github.com/support-aicloudstrategist/aicloud-agent-work.

## Layout

```
aicloud-foundation/
├── apps/                       per-container source + configs
│   ├── claude-mao/             Claude Code CLI + HTTP shim (the brain)
│   ├── tg-bot/                 Telegram front door; patch files for bot.py
│   ├── git-ops/                Tiny git-ops container
│   ├── linkedin-scheduler/     Hourly cron that auto-publishes scheduled posts
│   ├── n8n/                    Workflow exports + patch scripts
│   ├── openclaw-skills/        Legacy (reference only)
│   ├── health-check/           Cloud Cost Health Check prompt + samples
│   └── outreach/               Outreach playbook (LinkedIn, email, posts)
├── web/                        Live website (deployed to aicloudstrategist.com)
│   └── blog/                   Blog posts (HTML)
├── lead-magnets/               Public downloadable PDFs (5 published)
├── service-offerings/          Detailed per-service documents for all 9 services
├── docs/                       Strategic docs, templates, playbooks, LinkedIn assets
├── drafts/                     Content drafts (LinkedIn posts, emails, assessments)
│   └── posts-w3-to-w6/         Pre-drafted 10 posts for week 3-6 cadence
├── sessions/                   Work-log transcripts
└── archive/                    Older material kept for reference
```

## Services

Nine service offerings, all documented in `service-offerings/` with INR pricing, timelines, and step-by-step delivery plans. Summary at `service-offerings/README.md`. One-pager PDF for client-facing use at `docs/services-one-pager.pdf`.

## Related but separate

- `d:/dockers/hostinger/` — the VPS docker-compose files + backup archives for ALL containers running on the Hostinger VPS (plausible, n8n, traefik, webtop, etc.). This is infrastructure, not business source. Not part of this folder.

## How to deploy

Each `apps/<name>/` folder has its own README with deploy commands. In practice, changes flow:

1. Edit locally in `d:/aicloud-foundation/apps/<name>/`
2. Upload to VPS at `/docker/<name>/`
3. `docker compose up -d --build` for that service

## Cost model (Apr 2026)

| Line item | Monthly |
|---|---|
| Hostinger VPS | ₹522 |
| Google Workspace Business Starter (1 user) | ₹177 |
| Claude Max 20x subscription | $200 |
| OpenRouter (not in active use) | ₹0 |
| **New incremental spend** | **~₹700/mo** |

## Live endpoints

- Website: https://aicloudstrategist.com
- Services: https://aicloudstrategist.com/services.html
- Proof / Pattern Studies: https://aicloudstrategist.com/proof.html
- Writing / Blog: https://aicloudstrategist.com/blog.html
- Booking: https://aicloudstrategist.com/book.html (Calendly inline)
- Analytics: https://analytics.aicloudstrategist.com (Plausible, self-hosted)
- Telegram bot: @bill_15_bot
- n8n: https://n8n-solq.srv1562252.hstgr.cloud (internal)
- Paperclip: https://paperclip-1jd6.srv1562252.hstgr.cloud (reserved, not in use)

## Bot commands (Telegram @bill_15_bot)

- `/queue <task>` — add a general task to overnight queue (worker fires every minute)
- `/qlist` `/qresults` `/qclear` — manage queue
- `/post <topic>` — draft a LinkedIn post in Anushka voice
- `/draft <topic>` — general content draft
- `/subject <purpose>` — 8 cold-email subject variants
- `/email <recipient>` — cold email body
- `/bio <platform>` — bio for Twitter/meetup/etc
- `/schedule YYYY-MM-DD HH:MM <post>` — schedule a LinkedIn auto-publish
- `/scheduled` `/unschedule <id>` — manage schedule
- `/followup <client> | <finding 1> | <finding 2> | <finding 3>` — auto-generate Health Check follow-up email

## Crons on VPS

- `* * * * *` — task queue worker
- `30 3 * * 1-5` — daily LinkedIn connection-target list generator (09:00 IST Mon–Fri)
- `0 9 29 4 *` — DMARC tightening reminder (2026-04-29 09:00 IST)
- Hourly (after auth) — LinkedIn post auto-publisher

## Founder structure

- **Anushka B** — founder, public face, legal proprietor (once GST registered), Rohini Delhi. 7+ years independent cloud/DevOps practice.
- **Senior-architect advisory** — 22+ years Fortune 500 and global-consulting experience reviewing every engagement. Never named publicly. Referenced on-site as "senior-architect oversight" or "enterprise-reviewed".
