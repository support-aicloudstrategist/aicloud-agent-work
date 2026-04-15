# claude-mao

The brain of the AI fabric. Runs Claude Code CLI inside a Docker container on a Claude Max 20x subscription.

## What it is
- Ubuntu 24.04 container
- Claude Code CLI installed via `npm i -g @anthropic-ai/claude-code`
- Authenticated via Max subscription OAuth (`~/.claude/.credentials.json` + `CLAUDE_CODE_OAUTH_TOKEN` env)
- Exposes an HTTP shim on port 8080 inside the `ai-ops` network for other containers to dispatch tasks
- Has `docker.sock` mounted (with `docker-safe` whitelist) so it can operate on other containers

## Key files in this folder
- `server.mjs` — the HTTP shim (Node 22, stdlib only)
- `docker-safe.sh` — whitelist wrapper around `docker` CLI (allows inspection + safe installs, blocks rm/stop/kill/etc.)
- `OPS.md` — operational runbook + verify checklist
- `README.md` — this file

## Cost
- **$0 per call.** `total_cost_usd` in the JSON response is cosmetic telemetry when authenticated via Max OAuth.
- Actual consumption counts against Max 20x plan rate limits (5-hour rolling + weekly caps).
- **DO NOT set `ANTHROPIC_API_KEY` in the env** — that's the foot-gun that flips it to pay-per-token.

## Shim API
- `POST /run` `{prompt, session_id?, max_turns?}` — runs `claude -p`, returns structured JSON (result, session_id, exit_code, duration_ms, telemetry_cost_usd)
- `GET /healthz` — unauthed liveness
- `GET /usage` — unauthed usage stats
- Auth: `Authorization: Bearer $SHIM_TOKEN` (token lives at `/docker/claude-mao/.shim_token` on host)

## Session behaviour
- First call with no `session_id`: shim generates UUID, Claude starts a fresh conversation
- Subsequent call with same `session_id`: uses `--resume` to continue the conversation (memory preserved)
- If resume fails (session disappeared): auto-falls-through to a fresh session

## Safety envelope
- `--permission-mode bypassPermissions` is set by the shim (container is already sandboxed)
- `docker-safe` whitelist blocks destructive ops against other containers
- Daily run cap (500/day) in shim as circuit-breaker against loops

## Layout on VPS
```
/docker/claude-mao/
├── docker-compose.yml   (runs ttyd + shim; auto-creates docker-safe symlink)
├── Dockerfile
├── .env                 (OAuth token, ttyd password)
├── .shim_token          (random bearer token, 600/root)
├── bin/
│   ├── shim-server.mjs  ← mounted to /opt/mao-bin inside container
│   └── docker-safe      ← mounted to /opt/mao-bin, symlinked to /usr/local/bin
├── data/home/           (mao user home inside container)
└── skills/              (optional Claude Code skills)
```

## Redeploy
```
cd /docker/claude-mao
# Copy updated server.mjs or docker-safe into ./bin/ first
docker compose up -d --force-recreate
docker network connect ai-ops claude-mao  # networks get dropped on recreate
```
