# n8n workflow imports — known issues (2026-04-15)

**Status:** workflows imported, JSON patched in repo, but live execution hits an HTTP-node expression bug. Workflows **deactivated** until we can fix properly in the n8n UI.

## What works

- Webhooks register and accept POST (when n8n + traefik are freshly restarted)
- Env vars (`SHIM_TOKEN`, `BOT_TOKEN`, `TG_CHAT_ID`) are injected into the n8n container
- Network: n8n ↔ claude-mao reachable inside `ai-ops`
- `N8N_BLOCK_ENV_ACCESS_IN_NODE=false` set so expressions can read `$env.*`

## What's broken

Every execution of the HTTP Request node "Ask Mao" errors with:

> `NodeOperationError: The value in the "JSON Body" field is not valid JSON`

Symptoms:
- Tried `jsonBody` with JSON.stringify(...) wrapper → fails
- Tried `specifyBody=keypair` with contentType=json → fails (still hits same parser)
- Error persists even after `active=0` → restart → `active=1` → restart cycles
- Webhook URL sometimes 404s after a restart until traefik is also restarted

## Likely root cause

n8n v2.15 HTTPRequest node V4.2 evaluates `jsonBody` expressions differently when the workflow is imported programmatically (via DB write) versus when edited in UI. Our patch writes raw JSON params to the DB but n8n's UI-level validation is skipped, so the workflow stays in an inconsistent state that UI re-save would fix.

## Fix path

Have someone (Rajiv or Comet) open each of the 3 workflows in the n8n UI:
1. Go to https://n8n-solq.srv1562252.hstgr.cloud
2. Open `01_LeadScout`
3. Click the **Ask Mao (enrich + score)** node → **Body** tab → toggle **Send Body** off then on → select **"JSON"** and paste this for the Body Parameters (keypair style):
   - `prompt` (string, expression) → the prompt text
   - `max_turns` (number) → `8`
4. Save, activate
5. Repeat for `02_ContentDraft` and `03_InvoiceBot`

Alternative: delete workflows in UI, re-import the (now-fixed) JSON files fresh — n8n's UI import does the validation dance that the DB-patch route skips.

## Status

All three workflows are currently **deactivated** (`active=0`) so they don't accumulate failed executions. Their webhook paths return 404 when deactivated, which is fine.

## Priority

LOW. These workflows are outreach automation — nice-to-have, not blocking first customer. Revisit after entity registrations + first lead in pipeline.
