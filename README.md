# aicloud-agent-work

Source of truth for Rajiv's AICloudStrategist stack — website, AI agent fabric, outreach automation, lead magnets, business plan.

Owner: Rajiv (support@aicloudstrategist.com) · Delhi/NCR · Founded April 2026.

## Layout

```
aicloud-agent-work/
├── apps/                      ← per-container source + docs
│   ├── claude-mao/            Claude Code CLI + HTTP shim (the brain)
│   ├── tg-bot/                Lightweight Telegram front door
│   ├── n8n/                   Workflow exports (LeadScout, ContentDraft, InvoiceBot)
│   ├── openclaw/              Legacy runtime (stopped; kept for git workspace only)
│   └── paperclip/             Reserved for when orchestration is needed
├── web/                       The live site (served at aicloudstrategist.com)
├── lead-magnets/              PDFs + markdown sources
├── docs/                      Business plan, launch plans, session logs
└── sessions/                  Conversation transcripts (Claude Code work logs)
```

## How the stack connects

```
You (Telegram)
    ↓
tg-bot (container, on `ai-ops` Docker net)
    ↓ HTTP POST + bearer token
claude-mao shim :8080
    ↓ spawns
claude -p --resume <session> --permission-mode bypassPermissions
    ↓ uses
WebSearch, WebFetch, Bash, Read/Write/Edit, Glob, Grep, TodoWrite, docker-safe
    ↓
Response → tg-bot → Telegram → You
```

All three containers (tg-bot, claude-mao, n8n) sit on a shared Docker network `ai-ops` so they can reach each other by name.

## Cost model (April 2026)

| Line item | Monthly |
|---|---|
| Hostinger VPS | ₹522 |
| Google Workspace Business Starter (1 user) | ₹177 |
| Claude Max 20x subscription (already paying) | $200 |
| OpenRouter (not in active use; top up if needed) | ₹0 |
| **New spend on top of Max sub** | **~₹700/mo** |

## Key live endpoints

- Website: https://aicloudstrategist.com
- Booking: https://aicloudstrategist.com/book.html (Calendly inline)
- n8n UI: https://n8n-solq.srv1562252.hstgr.cloud
- Paperclip UI: https://paperclip-1jd6.srv1562252.hstgr.cloud (not in active use)
- Telegram bot: @bill_15_bot (tg-bot container)

## Getting started in a new Claude Code session

1. Skim `docs/` for the launch plan context
2. Skim `sessions/` for the latest conversation transcript
3. Check `apps/*/README.md` for each component

SSH to VPS:
```
plink -ssh -batch -pw '<password>' root@62.72.59.122
# creds in memory file: reference_vps_hostinger.md
```
