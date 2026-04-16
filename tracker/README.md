# Tracker — Vikunja

Self-hosted project tracker at https://tracker.srv1562252.hstgr.cloud/

## Stack

- **Vikunja v2.3.0** — single Go binary, SQLite, ~100MB RAM footprint
- **vikunja-webhook** — tiny Python sidecar that forwards task events to Telegram
- Routed via Traefik on `ai-ops` docker network
- Domain: free `*.srv1562252.hstgr.cloud` Hostinger subdomain (no Cloudflare DNS setup needed)

## Directory layout

```
tracker/
├── vikunja/                    # main app
│   ├── docker-compose.yml
│   └── vk                      # bash CLI wrapper for API
└── vikunja-webhook/            # Telegram notification bridge
    ├── app.py
    ├── Dockerfile
    └── docker-compose.yml
```

## Key config (env vars set in /docker/vikunja/docker-compose.yml)

- `VIKUNJA_DATABASE_TYPE=sqlite` — no external DB needed
- `VIKUNJA_SERVICE_ENABLEREGISTRATION=false` — admin-only signup
- `VIKUNJA_WEBHOOKS_ALLOWNONROUTABLEIPS=true` — allows webhook delivery to docker-internal IPs
- `VIKUNJA_OUTGOINGREQUESTS_ALLOWNONROUTABLEIPS=true` — **required** as of v2.3.0 (the `webhooks` variant alone is insufficient)

## CLI helper (`vk`)

Installed at `/usr/local/bin/vk` (symlink to `/docker/vikunja/vk`). Reads API token from `/docker/vikunja/.admin-creds` (mode 600). Run `vk help` for usage.

## Telegram integration

Per-project webhooks fire into `vikunja-webhook:8090`, which formats HTML and posts to the existing support-bot group (chat_id `-4955349765`). Events: `task.created`, `task.updated`, `task.deleted`, `task.overdue`, `task.comment.created`, `task.assignee.created`.

To stop a specific event from firing Telegram, edit the `NOISY_EVENTS` set in `vikunja-webhook/app.py`.

## Backup

SQLite database at `/docker/vikunja/files/vikunja.db` is included in the daily root backup at 03:00 UTC (cron `/root/scripts/backup.sh`).
