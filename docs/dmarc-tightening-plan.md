# DMARC Tightening Plan — aicloudstrategist.com

**Status:** Prepared, not applied. Waiting on 2 weeks of aggregate reports before pulling the trigger.

## Current state (2026-04-15)

DNS TXT record at `_dmarc.aicloudstrategist.com`:

```
v=DMARC1; p=none; rua=mailto:support@aicloudstrategist.com; ruf=mailto:support@aicloudstrategist.com; fo=1; aspf=r; adkim=r
```

- **Policy:** `p=none` — receivers report, do not quarantine or reject
- **Alignment:** relaxed (`aspf=r`, `adkim=r`) — subdomain senders pass
- **Reporting:** aggregate (`rua`) + forensic (`ruf`) to support@
- **Record ID (Cloudflare):** `3a9550eaac01252d319c7d3233ba4ac6`
- **Zone ID:** stored at `/docker/secrets/cloudflare_zone_id` on VPS

## Why we are not tightening yet

- Outreach sending is just starting (April 2026). Zero baseline.
- Google Workspace is the only confirmed legitimate sender. We need to confirm from `rua` reports that no other IPs are sending as `@aicloudstrategist.com` (forgotten n8n notifier, test scripts, form providers, etc.).
- `p=quarantine` applied before a clean baseline will silently drop legitimate email.

## Trigger to tighten (any one of):

1. 14 consecutive days of `rua` reports showing ≥99% of volume from Google Workspace IPs only, AND
2. Outreach cadence has been live for at least 10 days without bounces, AND
3. No new sending integrations planned for the next 30 days.

Earliest candidate date: **2026-04-29**.

## Target record (after trigger)

```
v=DMARC1; p=quarantine; pct=25; rua=mailto:support@aicloudstrategist.com; ruf=mailto:support@aicloudstrategist.com; fo=1; aspf=s; adkim=s
```

Changes:
- `p=none` → `p=quarantine` (route suspicious mail to spam folder, don't outright reject)
- Add `pct=25` (only 25% of non-passing mail gets quarantined — a safety valve during rollout)
- `aspf=r` → `aspf=s` (strict SPF alignment)
- `adkim=r` → `adkim=s` (strict DKIM alignment)

After 14 more days at `p=quarantine; pct=25` with clean reports, next step is `pct=100`, then finally `p=reject` (month 3+).

## How to apply when ready (Cloudflare API via VPS)

```bash
TOKEN=$(cat /docker/secrets/cloudflare_token)
ZONE=$(cat /docker/secrets/cloudflare_zone_id)
RECORD_ID=3a9550eaac01252d319c7d3233ba4ac6

curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/$ZONE/dns_records/$RECORD_ID" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "TXT",
    "name": "_dmarc.aicloudstrategist.com",
    "content": "v=DMARC1; p=quarantine; pct=25; rua=mailto:support@aicloudstrategist.com; ruf=mailto:support@aicloudstrategist.com; fo=1; aspf=s; adkim=s",
    "ttl": 3600
  }' | jq '.success, .result.content'
```

## Verification after apply

```bash
# Check DNS propagation
dig +short TXT _dmarc.aicloudstrategist.com @1.1.1.1
dig +short TXT _dmarc.aicloudstrategist.com @8.8.8.8

# Confirm via mxtoolbox (browser):
# https://mxtoolbox.com/SuperTool.aspx?action=dmarc%3aaicloudstrategist.com

# Send test mail to mail-tester.com and verify DMARC pass + 10/10 score
```

## Rollback

If legitimate mail starts getting quarantined:

```bash
curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/$ZONE/dns_records/$RECORD_ID" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"type":"TXT","name":"_dmarc.aicloudstrategist.com","content":"v=DMARC1; p=none; rua=mailto:support@aicloudstrategist.com; ruf=mailto:support@aicloudstrategist.com; fo=1; aspf=r; adkim=r","ttl":3600}'
```

Rollback propagation: typically under 5 minutes on Cloudflare.

## Aggregate report parsing (optional, for the 2-week observation window)

DMARC aggregate reports arrive as XML zipped attachments to support@. To summarise:

```bash
# On any machine with python3
pip install parsedmarc
parsedmarc --imap-host imap.gmail.com --imap-user support@aicloudstrategist.com --imap-password <app-pw> --folder DMARC
```

Or queue a task for mao to build a simple parser once the first reports arrive:

```
/queue Parse all DMARC aggregate XML reports in support@ inbox from last 7 days. List every sending IP, its SPF/DKIM alignment status, and volume. Flag any IP that is not Google Workspace.
```
