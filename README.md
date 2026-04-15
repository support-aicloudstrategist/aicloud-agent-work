# aicloud-foundation

Source of truth for the AICloudStrategist business — Anushka B's cloud consulting practice. Founder-led. Enterprise-reviewed.

This folder is the **local dev mirror** of the GitHub repo at
https://github.com/support-aicloudstrategist/aicloud-agent-work.

## Layout

```
aicloud-foundation/
├── apps/                      per-container source + configs
│   ├── claude-mao/            Claude Code CLI + HTTP shim (the brain)
│   ├── tg-bot/                Lightweight Telegram front door
│   ├── git-ops/               Tiny git-ops container (replaces openclaw)
│   ├── n8n/                   Workflow exports + patch scripts
│   ├── openclaw-skills/       Legacy (reference only)
│   ├── health-check/          Cloud Cost Health Check prompt + samples
│   └── outreach/              Outreach playbook (LinkedIn, email, posts)
├── web/                       Live website (deployed to aicloudstrategist.com)
├── lead-magnets/              Public downloadable PDFs
├── docs/                      Business plans, strategic docs
├── sessions/                  Work-log transcripts
└── archive/                   Older material kept for reference
```

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
- Booking: https://aicloudstrategist.com/book.html (Calendly inline)
- Telegram bot: @bill_15_bot
- n8n: https://n8n-solq.srv1562252.hstgr.cloud (internal)
- Paperclip: https://paperclip-1jd6.srv1562252.hstgr.cloud (reserved, not in use)
