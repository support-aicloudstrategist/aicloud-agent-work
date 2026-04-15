# AI Fabric Build Session — 2026-04-14 / 15

**Participants:** Rajiv (user) + Claude (Opus 4.6, 1M context)
**Objective:** Build a cost-effective AI agent stack on Hostinger VPS where Telegram is the front door, simple work runs cheap, and complex work uses a Claude Max subscription.

---

## Starting state

- **VPS:** Hostinger (`root@62.72.59.122`, also `srv1562252.hstgr.cloud`), Docker host with 10+ containers.
- **openclaw-kfgm-openclaw-1:** OpenClaw agent runtime, Telegram bot, was using shared Claude Max OAuth.
- **claude-mao:** Claude Code CLI container, authenticated with Max subscription (Max 20x tier, `default_claude_max_20x`).
- **paperclip-1jd6-paperclip-1:** Hostinger one-click install of Paperclip (misidentified as password manager; actually AI agent orchestration platform).
- **n8n, plausible, uptime-kuma, website, traefik, ntfy, ollama, webtop:** other unrelated services.

---

## Problem 1 — Anthropic blocked shared Max OAuth for openclaw

**Symptom (recurring billing error on Telegram bot):**
```
API provider returned a billing error — your API key has run out of credits
or has an insufficient balance.
```

**Actual Anthropic 400 response:**
> "Third-party apps now draw from your extra usage, not your plan limits. We've added a $200 credit to get you started. Claim it at claude.ai/settings/usage and keep going."

**Root cause:** Anthropic's April 2026 policy change. Max subscription OAuth tokens used by non-official clients (openclaw, etc.) no longer draw from plan limits — they require separate "extra usage" credit bundle. User claimed the $200 credit but rejections persisted (likely payment-method / account-linking issue, but structurally it's an enforcement gate, not a soft rejection).

**Fix applied:**
- Disabled `plugins.entries.anthropic` in `/docker/openclaw-kfgm/data/.openclaw/openclaw.json`.
- Switched agent defaults to OpenRouter:
  - `agents.list[0].model` = `openrouter/anthropic/claude-sonnet-4.5`
  - `agents.defaults.model` = `openrouter/deepseek/deepseek-chat-v3.1`
- Archived sticky live session files at `/docker/openclaw-kfgm/data/.openclaw/agents/main/sessions/archive/` (they had per-session `model_change` events pinning haiku via Anthropic, overriding the new global default).
- Restarted container. Telegram bot started responding normally via OpenRouter.

**Saved as memory:** `project_openclaw_anthropic_3p_block.md`

---

## Problem 2 — aicloud-agent-work repo + deploy key

**Task:** Give openclaw container push access to `https://github.com/support-aicloudstrategist/aicloud-agent-work`.

**Actions:**
1. Cloned empty repo into openclaw container at `/data/work/aicloud-agent-work`.
2. Generated ed25519 deploy key at `/data/.ssh/id_ed25519_aicloud` (fingerprint `SHA256:Ti09XA8RSHL07Js5L8LuIpBjlncLetdOsWNhJioD3Fk`).
3. Public key added as Deploy Key (write access) on the repo.
4. First push attempt failed with "Permission denied (publickey)" — SSH config `Host github-aicloud` alias wasn't being picked up.
5. Fixed with explicit `GIT_SSH_COMMAND` env var + `git config core.sshCommand` persisted in the repo config.
6. First real push: `test commit from bot` → commit `15907cb`, README on main.
7. Permission fix: files were root-owned but container runs as `node`; chowned `/data/work` and `/data/.ssh` to node:node.

**Saved as memory:** `reference_aicloud_agent_work_repo.md`

---

## Research — can we use OpenAI or Gemini subscriptions instead?

**Answer: No clean path.**

- **ChatGPT Plus ($20/mo) / Pro ($200/mo):** subscription ≠ API. Only Codex CLI (a coding tool) can use "Sign in with ChatGPT" but Codex is not a drop-in LLM backend. ToS forbids automating against ChatGPT web.
- **Gemini Advanced / Google AI Pro ($19.99/mo) / Ultra ($249.99/mo):** subscription doesn't unlock API access at all. Gemini CLI has a free personal-login tier (~60 RPM, ~1k RPD on Gemini 2.5 Pro) but it's not tied to the paid subscription.

**Conclusion:** There is no legitimate monthly-fixed-price subscription from OpenAI or Google that powers a third-party agent. For bot-scale traffic, pay-per-token via OpenRouter ($5–10/mo) is cheapest.

---

## Research — OpenRouter free tier

- **28 free models** currently available (query `/api/v1/models` at runtime; list rotates weekly).
- **Rate limits:** ~50 req/day on fresh accounts; **~1,000 req/day once $10 lifetime credits loaded**.
- **Top 5 free models for agent/tool-use:**
  1. `openrouter/free` (auto-router, 200k ctx)
  2. `qwen/qwen3-coder:free` (262k ctx, code-tuned)
  3. `openai/gpt-oss-120b:free` (131k, strongest free reasoning)
  4. `z-ai/glm-4.5-air:free` (131k, agent benchmarks)
  5. `nvidia/nemotron-3-super-120b-a12b:free` (262k, MoE)
- **Caveat:** no zero-data-retention on `:free` models — all prompts logged. Don't send company secrets via free tier.

---

## Research — Paperclip (paperclipai/paperclip)

Originally investigated as potential orchestrator for the fabric.

- **Not a password manager** (Hostinger image name `hvps-paperclip` is misleading).
- **53k GitHub stars, MIT, daily commits, pre-1.0.**
- **Runs at `paperclip-1jd6.srv1562252.hstgr.cloud:3100`** (already installed by Hostinger one-click).
- **Role:** scheduler + UI + state + audit + budget + approval gates. Zero LLM spend at the Paperclip layer itself.
- **Built-in adapters:** `openclaw_gateway`, `claude_local`, `codex_local`, `cursor_local`, `http`, `process`.
- **"If it can receive a heartbeat, it's hired"** — Paperclip drives agents via scheduled heartbeats, not the reverse.
- **Onboarding flow:** Paperclip UI → Invites → Generate OpenClaw Invite Prompt → paste into openclaw chat → approve device pairing.

Implementation was paused mid-way (stage 2+ pending CLI auth approval from user).

---

## Infrastructure built

### Stage 1 — `ai-ops` Docker network ✅

```
docker network create ai-ops
docker network connect ai-ops paperclip-1jd6-paperclip-1   # 172.28.0.2
docker network connect ai-ops openclaw-kfgm-openclaw-1     # 172.28.0.3
docker network connect ai-ops claude-mao                    # 172.28.0.4
docker network connect ai-ops n8n-solq-n8n-1                # 172.28.0.5
```

Verified DNS + HTTP reachability across all four.

### Stage 4a — claude-mao HTTP shim ✅

`/docker/claude-mao/bin/shim-server.mjs` (Node 22), bind-mounted as `/opt/mao-bin/` in container. Survives restarts.

**API:**
- `GET /healthz` — unauthed
- `GET /usage` — unauthed
- `POST /run` — bearer-token auth, body `{prompt, session_id?, max_turns?}`, shells out to `claude -p --output-format json`, returns structured response.

**Safety:** daily run cap (500/day default) — circuit breaker against runaway loops. No USD budget (cost is cosmetic under Max OAuth, see below).

### Stage 4b — `docker-safe` whitelist wrapper ✅

`/docker/claude-mao/bin/docker-safe` (bash). Symlinked to `/usr/local/bin/docker-safe` on every container start via `sudo -n ln -sf` in compose command.

- **Allowed:** ps, images, inspect, logs, top, stats, version, info, network, volume, port, events; `exec` only for safe inner commands (apt/pip/npm/git/…); `restart` only for ai-fabric containers.
- **Blocked:** rm, stop, kill, run, create, `--force-yes`, `-rf /`, all other subcommands.
- **Audit:** every invocation logged to `/home/mao/docker-safe.log`.
- mao user added to gid 988 (host docker group) via `group_add: ["988"]` in compose.

### End-to-end verification ✅

```
openclaw container → POST http://claude-mao:8080/run
                   → claude-mao runs `claude -p`
                   → result "PONG" in 4.5s
```

Second test: "List /home/mao using docker-safe" → Claude used its tools, returned correct listing in 8s.

---

## Critical billing finding ⚠️ → ✅

Initial panic: every `claude -p` call was returning `total_cost_usd: $0.02–0.04` and `service_tier: "standard"`. Feared this broke the "zero marginal cost" assumption.

**Research cleared it up:**

- `total_cost_usd` is **informational telemetry**, not actual charge.
- With `subscriptionType: "max"`, `rateLimitTier: "default_claude_max_20x"`, and scopes `user:inference` + `user:sessions:claude_code`, usage draws from Max plan rate limits, not overage.
- The dangerous foot-gun is `ANTHROPIC_API_KEY` env var — if set, `claude -p` silently switches to pay-per-token API billing (GitHub issue #37686: a Max user racked up $1,800 in two days from this).
- **Confirmed for claude-mao:** `env | grep -iE "ANTHROPIC_API_KEY|ANTHROPIC_AUTH_TOKEN"` → nothing. Safe.

**Conclusion:** claude-mao is truly $0 marginal cost, billed only against Max 20x plan rate limits.

Sources: [Manage costs effectively](https://code.claude.com/docs/en/costs), [Authentication docs](https://code.claude.com/docs/en/authentication), [Using Claude Code with Pro/Max](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan).

---

## The reset — what the user actually wants

Reframed after drift:

> A Telegram bot where I give any task, simple or complex, and it gets done. Cheap work runs cheap (OpenRouter), heavy work uses Max subscription (claude-mao), no surprise bills. I get a report when done.

**Not needed right now:** Paperclip orchestration, multi-agent org charts, n8n, docker-safe for cross-container work (unless agent explicitly needs it), approval workflows.

**Minimum viable build (paused for next session):**

1. Write one openclaw skill `ask-mao` that POSTs to `http://claude-mao:8080/run`.
2. Update openclaw system prompt to classify simple vs complex and call `ask-mao` when complex.
3. Stream progress back to Telegram during long runs.
4. Test with 3 real tasks.

Estimated: **2 hours**, one deliverable, testable outcome.

---

## State at time of save (2026-04-15)

### Running services
| Container | Status | Model / auth |
|---|---|---|
| openclaw-kfgm-openclaw-1 | running | OpenRouter (DeepSeek v3.1 default, Sonnet 4.5 for main agent); anthropic plugin disabled |
| claude-mao | running | Claude Code CLI w/ Max 20x OAuth (cost telemetry only, draws from plan limits); shim on :8080; docker-safe wrapper active |
| paperclip-1jd6-paperclip-1 | running | Authenticated mode, admin provisioned (`support@aicloudstrategist.com`), CLI not yet authed, no employees hired |
| n8n-solq-n8n-1 | running | unchanged, joined ai-ops network |

### Files on host (VPS)
- `/docker/openclaw-kfgm/data/.openclaw/openclaw.json` — OpenRouter config
- `/docker/openclaw-kfgm/data/.ssh/id_ed25519_aicloud` — deploy key for aicloud-agent-work
- `/docker/claude-mao/bin/shim-server.mjs` + `docker-safe` — fabric plumbing
- `/docker/claude-mao/.shim_token` — bearer token for shim
- `/docker/claude-mao/docker-compose.yml` — patched (group_add 988, bind mount ./bin, compose command auto-starts shim)
- `/docker/claude-mao/docker-compose.yml.bak-*` — backups

### Files on dev machine
- `d:/dockers/hostinger/claude-mao-shim/server.mjs`
- `d:/dockers/hostinger/claude-mao-shim/docker-safe.sh`
- `d:/dockers/hostinger/claude-mao-shim/OPS.md`
- `d:/dockers/hostinger/claude-mao-shim/README.md`

### Persisted memories for next session
- `feedback_execution_flow.md` — no mid-task approvals; complete → verify → report → how-to-test
- `reference_vps_hostinger.md` — SSH creds, paths, container inventory
- `project_openclaw_oauth_sharing.md` — original Max OAuth sharing setup (now superseded)
- `project_openclaw_anthropic_3p_block.md` — Anthropic block, OpenRouter fallback details
- `reference_aicloud_agent_work_repo.md` — repo clone path + deploy key
- `project_ai_fabric_plan.md` — full plan approved, execution paused
- `project_ai_fabric_progress.md` — what got built overnight

---

## Next session — pick up here

**Recommended first step:** build the minimum viable router (the 4 steps above). Don't touch Paperclip until the router proves the flow works end-to-end.

If the router works and feels solid after a week of real use, decide whether Paperclip adds enough value to justify its onboarding complexity.

**If picking Paperclip route instead:**
1. User logs into https://paperclip-1jd6.srv1562252.hstgr.cloud as `support@aicloudstrategist.com`.
2. Regenerate CLI auth URL on VPS: `docker exec -u 0 paperclip-1jd6-paperclip-1 npx -y paperclipai auth login --instance-admin --api-base https://paperclip-1jd6.srv1562252.hstgr.cloud`
3. User approves CLI in browser.
4. Create company "AICloudStrategist", mint API key.
5. Generate openclaw invite prompt → paste into openclaw Telegram → approve device.
6. Register claude-mao HTTP adapter at `http://claude-mao:8080/run` with bearer token from `/docker/claude-mao/.shim_token`.
7. Register n8n HTTP adapter pointed at its webhook URL.
8. End-to-end scenarios: simple Q&A, heavy task via mao, approval-gated destructive flow.

Either path is viable. The router is faster and cheaper; Paperclip gives better audit + scaling later.
