# claude-mao-shim ops

## What's deployed

- **Shim**: `/opt/mao-bin/shim-server.mjs` in claude-mao container, listens on `:8080`, reachable across `ai-ops` Docker network from any other AI container (`http://claude-mao:8080`).
  - `POST /run {prompt, session_id?, max_turns?}` with `Authorization: Bearer $SHIM_TOKEN` — runs `claude -p` and returns JSON.
  - `GET /healthz`, `GET /usage` — unauthed.
  - Daily USD budget cap (default $5) — when hit, returns 429 `budget_exceeded`.
- **docker-safe**: `/usr/local/bin/docker-safe` (symlink to `/opt/mao-bin/docker-safe`), whitelist-only docker CLI wrapper for mao → other containers. Logs every invocation to `/home/mao/docker-safe.log`.
  - Allowed: ps, images, inspect, logs, top, stats, version, info, network, volume, port, events, exec (to run apt/pip/npm/git/etc inside other containers), restart (of ai-fabric containers only).
  - Blocked: rm, stop, kill, run, create, anything not listed.

## Token
`/docker/claude-mao/.shim_token` on host (600/root), `/home/mao/.shim_token` in container (600/mao).

## Persistence
All baked into `/docker/claude-mao/docker-compose.yml`:
- bind mount `./bin → /opt/mao-bin` (read-only inside container)
- `group_add: ["988"]` so `mao` user can access host docker.sock
- compose `command` auto-creates the docker-safe symlink + starts the shim + starts ttyd+claude

Survives: `docker compose up -d --force-recreate`, VPS reboot.
Does NOT survive: image rebuild (would need symlink re-created). Compose `command` handles that too via `sudo -n ln -sf`.

## Networks
- `ai-ops` (172.28.0.0/16) — shared by paperclip, openclaw, claude-mao, n8n.
- Each container retains its own default network for traefik ingress.

## Verify checklist

```
# Shim healthy
docker exec claude-mao curl -sS http://localhost:8080/healthz
# expect: {"ok":true,"usage":{"day":"...","costUsd":0,"runs":0}}

# Cross-network
docker exec openclaw-kfgm-openclaw-1 curl -sS http://claude-mao:8080/healthz

# docker-safe denies destructive
docker exec -u mao claude-mao docker-safe rm -f traefik
# expect: blocked: subcommand_not_whitelisted rm

# docker-safe allows inspect
docker exec -u mao claude-mao docker-safe ps --format '{{.Names}}' | head

# End-to-end through shim
TOKEN=$(cat /docker/claude-mao/.shim_token | cut -d= -f2)
docker exec openclaw-kfgm-openclaw-1 curl -sS -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H 'content-type: application/json' \
  -d '{"prompt":"Say PONG"}' \
  http://claude-mao:8080/run
```

## ⚠️ Economic reality (important)

Each `/run` call costs real money (~$0.02–0.04 per simple turn) because Anthropic's
third-party-app gate routes the Max subscription token to per-token billing instead of
plan limits. Verified 2026-04-14: Sonnet usage_tier="standard", `total_cost_usd` non-zero.

Implication: the "zero marginal cost" assumption of the AI fabric plan is broken.
Either (a) pay per token via this path (same as API key), or (b) use OpenRouter free
tier for most work and reserve this for critical tasks, or (c) investigate whether
`claude-cli` with OAuth Max token *actually* bypasses the gate (it appears to bill
standard, but verify across longer test window — if it's truly plan-limited, the shim
is $0/day as long as you stay under Max daily caps).

Check `GET /usage` regularly. Daily budget cap (default $5) protects against runaway.
