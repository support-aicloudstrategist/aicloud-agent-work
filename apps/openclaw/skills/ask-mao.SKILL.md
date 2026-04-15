---
name: ask-mao
description: Escalate complex coding/multi-step tasks to claude-mao (Claude Code CLI on Max subscription) via HTTP shim. Use when a task needs real reasoning, code changes, multi-tool work, file edits across a repo, debugging, research, or anything that would take more than 1-2 simple tool calls. Do NOT use for trivial Q&A or tasks you can answer directly.
---

# ask-mao — escalate to claude-mao

This skill lets the Telegram-fronted openclaw agent hand a hard task to claude-mao, which runs the official Claude Code CLI under a Claude Max subscription (zero marginal cost). claude-mao can edit files, run commands, search the web, and use its own tools.

## When to use

**Escalate to mao** when the task needs:
- Multi-step coding work (refactor, add feature, debug)
- Research that requires web search + synthesis
- File-system work across multiple files
- Anything you'd ask a senior engineer to do
- Tasks the user explicitly says are "complex" / "deep" / "investigate"

**Do NOT escalate** for:
- Single-line answers
- Status checks ("are you alive", "what time is it")
- Reading one file and reporting
- Sending a message
- Things you can finish in 1–2 tool calls yourself

When in doubt: try yourself first. Escalate only after you've reasoned about it and decided it's beyond a quick reply.

## How to use

The shim is at `http://claude-mao:8080/run` on the `ai-ops` Docker network. Bearer token lives in `/data/secrets/shim_token` inside this container.

### Step 1 — Confirm before sending (CRITICAL)

You MUST tell the user what you're about to escalate and ask for confirmation BEFORE calling the shim. Use this exact format on Telegram:

```
🔧 This looks like a deep task. I'll hand it to claude-mao (heavier brain, slower).

Task:
> <one-paragraph task summary you're about to send>

Reply "go" to proceed, or refine the task.
```

Wait for the user's "go" or refinement. Do not call the shim until the user explicitly approves.

### Step 2 — Call the shim

Once approved, run:

```bash
TOKEN=$(cat /data/secrets/shim_token)
curl -sS --max-time 600 -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H 'content-type: application/json' \
  -d '{"prompt": "<your task here>", "max_turns": 12}' \
  http://claude-mao:8080/run
```

### Step 3 — Stream progress (long tasks)

If you expect the task to take >30 seconds, send the user an interim message:

```
⏳ Working on it via claude-mao… (this can take 1–5 minutes)
```

Then wait for the response.

### Step 4 — Format and return

The shim returns JSON like:

```json
{
  "run_id": "...",
  "session_id": "...",
  "exit_code": 0,
  "duration_ms": 12345,
  "telemetry_cost_usd": 0.04,
  "result": "the actual answer text from claude",
  "raw": { ... },
  "stderr": ""
}
```

Send the user:

```
✅ Done in <duration_ms/1000>s

<result>

—
session: <session_id>  ·  cost: ~$<telemetry_cost_usd> (telemetry only — Max plan covers it)
```

If `exit_code != 0`, send:

```
❌ claude-mao failed (exit <code>).

stderr:
<stderr>

Want me to retry, or handle this myself in degraded mode?
```

### Step 5 — Continuing a session

To continue an earlier conversation with mao, pass the same `session_id`:

```bash
curl -sS --max-time 600 -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H 'content-type: application/json' \
  -d '{"prompt": "<follow-up>", "session_id": "<prior session_id>", "max_turns": 8}' \
  http://claude-mao:8080/run
```

## Limits and safety

- **Daily run cap**: 500 calls/day (shim circuit breaker). If you hit `daily_run_cap_exceeded`, tell the user and stop escalating until midnight UTC.
- **Single-task only**: claude-mao is serial. Don't fire multiple parallel `/run` calls; wait for each to complete.
- **Approval gate**: NEVER skip Step 1. The user must approve every escalation. This protects against runaway loops and protects user trust.
- **Sensitive data**: The Max-subscription LLM call is not zero-data-retention. Don't pass production secrets, customer PII, or billing data to claude-mao without warning the user.
- **Shim token**: Read fresh from `/data/secrets/shim_token` each call. Never log or echo the token.

## Quick health check

If you're unsure whether mao is reachable:

```bash
curl -sS http://claude-mao:8080/healthz
```

Expected: `{"ok":true,"usage":{...}}`. If this fails, tell the user mao is down and continue in degraded (openclaw-only) mode.
