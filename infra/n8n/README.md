# n8n Workflows for AICloudStrategist

Three workflows to import into n8n at https://n8n-solq.srv1562252.hstgr.cloud

## How to import

1. Open n8n in browser, log in
2. **Workflows** → **Import from File** (or **+ Create** → **From File**)
3. Select one of the JSON files in this folder
4. Set the env vars (see "Required env" below)
5. **Activate** the toggle (top right)
6. Note the webhook URL shown for each (you'll trigger it from elsewhere)

## Required environment variables (set in n8n container)

Add to `/docker/n8n-solq/.env` and restart n8n:

```
SHIM_TOKEN=<paste from /docker/claude-mao/.shim_token, just the value after =>
BOT_TOKEN=8512868758:AAFZafaW3lWeAl0lQQ0e6ozghtyUd6oaPI8
TG_CHAT_ID=8752157678
ZOHO_INVOICE_TOKEN=<get from Zoho Self-Client OAuth — only needed when you enable invoicing>
ZOHO_ORG_ID=<your Zoho Invoice org id>
```

Then enable env passthrough in n8n compose by adding to environment block:
```
- SHIM_TOKEN
- BOT_TOKEN
- TG_CHAT_ID
- ZOHO_INVOICE_TOKEN
- ZOHO_ORG_ID
```

## The three workflows

### 01_LeadScout
**Webhook:** `POST https://n8n-solq.srv1562252.hstgr.cloud/webhook/leadscout`
**Body:** `{"url": "https://www.linkedin.com/in/<handle>"}`
**What it does:** Sends LinkedIn URL to claude-mao. Mao fetches the public profile, scores ICP fit (1–10), identifies intent signals, recommends an outreach angle. Returns JSON; pushes notification to your Telegram.

### 02_ContentDraft
**Webhook:** `POST https://n8n-solq.srv1562252.hstgr.cloud/webhook/contentdraft`
**Body:** `{"channel": "linkedin_post|cold_dm|email", "brief": "..."}`
**What it does:** Drafts an outreach message in your voice (no AI-tells, concrete, India-aware). Sends draft to your Telegram for approval. You reply `send` / `edit:` / `kill`.

### 03_InvoiceBot
**Webhook:** `POST https://n8n-solq.srv1562252.hstgr.cloud/webhook/invoice`
**Body:**
```json
{
  "customer_name": "Acme Pvt Ltd",
  "customer_email": "ap@acme.in",
  "customer_gstin": "07AAACA1234A1Z5",
  "customer_address": "...",
  "line_items": [{"name": "FinOps QuickStart", "qty": 1, "rate": 75000, "sac": "998313"}],
  "notes": "50% advance per SOW dated ...",
  "due_days": 14
}
```
**What it does:** Calculates GST split (Delhi GSTIN gets CGST+SGST 9+9; outside Delhi gets IGST 18). Sends invoice JSON for your approval via Telegram. When Zoho creds are set + node enabled, also creates the invoice in Zoho.

## Notes

- All three workflows have `disabled: true` on the destructive/external-side node where possible (file write, Zoho create) so you can dry-run safely after import.
- Approval-via-Telegram is built-in for the two outreach workflows. Nothing leaves your VPS without your explicit reply.
- Webhook paths are guessable. For production, set `Authentication: Header Auth` on each Webhook node with a shared secret you keep in env.
