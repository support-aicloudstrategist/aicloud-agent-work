# openclaw

Hostinger one-click install of [openclaw](https://openclaw.ai) — full-featured AI agent runtime. Currently **stopped** (`restart: no`) and kept only because the `aicloud-agent-work` git workspace lives inside its container.

## Status (2026-04-15)
- Container: `openclaw-kfgm-openclaw-1`
- State: stopped, auto-restart disabled
- Telegram channel: disabled (tg-bot owns the bot token now)
- Anthropic plugin: disabled (subscription gate prevented usage)
- Default model was `openrouter/anthropic/claude-sonnet-4.5`

## Why retired
Per-message cost was ₹15–100 (heavy system prompt + multi-turn tool loops on OpenRouter). A dumb Python bridge to claude-mao achieves the same result for ₹0 (Claude Max subscription).

## What's still in this folder
- `skills/` — the `ask-mao` skill we built when openclaw was the front door. Kept as reference; not loaded anywhere.

## When to start it up briefly
Only when we need to push to the `aicloud-agent-work` GitHub repo. The SSH deploy key for the repo lives inside this container (`/data/.ssh/id_ed25519_aicloud`).

```
docker start openclaw-kfgm-openclaw-1
# ... do git work via docker exec ...
docker stop openclaw-kfgm-openclaw-1
```

**Do not enable its telegram channel again** — it will fight tg-bot for the bot token and both will 409.

## When to fully decommission
Move the repo + deploy key into a lighter git container (e.g. a minimal alpine with git + ssh) and delete this container. Not urgent; it costs no money while stopped, just disk.
