# tg-bot

Minimal Python Telegram bot → claude-mao bridge. Runs on the VPS as container `tg-bot`.

## What it does
- Long-polls Telegram (no webhook)
- For every allowed chat: forwards text to `http://claude-mao:8080/run`, reads Claude's reply, sends it back
- Maintains a per-chat session id in `/data/sessions.json` so conversation memory persists across messages
- Falls back to a fresh session if Claude signals the stored one is stale

## Cost
- **Zero per message** — routes to claude-mao which runs on the Claude Max 20x subscription OAuth
- Daily-run-cap in the shim (500/day default) protects against runaway loops

## Files
- `bot.py` — the entire agent (~130 lines, stdlib only)
- `Dockerfile` — python:3.13-alpine, non-root
- `docker-compose.yml` — joins the `ai-ops` external network

## Env vars (set in `/docker/tg-bot/.env` on host)
- `BOT_TOKEN` — Telegram bot token from @BotFather
- `SHIM_TOKEN` — bearer for claude-mao shim (from `/docker/claude-mao/.shim_token`)
- `ALLOWED_CHAT_IDS` — comma-separated Telegram user IDs allowed to DM the bot

## Commands (built-in)
- `/start` / `/help` — intro
- `/new` — start a fresh conversation thread
- `/id` — show your chat id

## Deploy
```
cd /docker/tg-bot
docker compose up -d --build
docker logs -f tg-bot
```

## Notes
- On Alpine, the container UID inside matches the host-mounted `/data` dir UID (node=1000). Permission issues usually = host dir owned by root.
- openclaw must NOT also be polling Telegram with the same bot token or you'll get 409 conflicts. Keep openclaw stopped (`restart: no`) unless needed for git workspace.
