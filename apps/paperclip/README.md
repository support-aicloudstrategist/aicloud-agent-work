# paperclip

Hostinger one-click install of [paperclip](https://github.com/paperclipai/paperclip) — open-source AI agent orchestration platform ("org chart + budgets + approvals + audit for AI employees"). Currently **installed but not integrated** with our stack.

## Status (2026-04-15)
- Running at https://paperclip-1jd6.srv1562252.hstgr.cloud (port 3100)
- Admin account provisioned (`support@aicloudstrategist.com`)
- CLI auth flow never completed (user decided to simplify stack with tg-bot → claude-mao instead)
- No employees hired, no company configured, no workflows running through it

## Why it's paused
Early in the stack build we planned to use paperclip as the orchestrator (openclaw + claude-mao + n8n as "employees", paperclip dispatching heartbeats with budget/approval gates). Two things changed that plan:
1. openclaw turned out to be expensive (~₹15–100/day). We retired it in favour of a lightweight tg-bot.
2. Paperclip is pre-1.0 (53k ⭐, daily commits, 2k+ open issues). Good for future; too early-stage for a business just trying to sign its first customer.

The tg-bot → claude-mao flow covers the core use case with zero added complexity.

## When to revisit
Come back to paperclip if/when:
- You add multiple specialised agents (sales bot, support bot, research bot) and want one place to see them all
- You need formal approval workflows (board-level gates for destructive actions, spend caps per agent)
- You need an immutable audit log for compliance/governance reasons
- Paperclip cuts a 1.0 release

Until then, this folder is a placeholder holding notes + the URL.

## Useful paths
- Host config: `/docker/paperclip-1jd6/`
- Container: `paperclip-1jd6-paperclip-1`
- Enter as root: `docker exec -it -u 0 paperclip-1jd6-paperclip-1 bash` (sudo blocked by no-new-privileges)
- Internal DB: embedded Postgres at `/paperclip/instances/default/db`
- Secrets: `/paperclip/instances/default/secrets/master.key`
