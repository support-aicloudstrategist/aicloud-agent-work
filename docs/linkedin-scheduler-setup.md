# LinkedIn Auto-Publisher Setup — Step-by-Step

**For:** Raj (one-time setup)
**Time needed:** 15 minutes
**Outcome:** 5 first-wave LinkedIn posts auto-publish on their scheduled dates without further human action.

---

## What this enables

Once set up, the `/docker/linkedin-scheduler/post.py` cron runs hourly on the VPS. If any post in `posts.yaml` is due (publish_at matches current hour and not yet in `published.log`), it publishes to Anushka's LinkedIn feed via the official LinkedIn API.

No Anushka clicks required. No Raj involvement after setup. Each successful publish pings the Telegram group with the post URN.

**Posts already scheduled** (from `apps/linkedin-scheduler/posts.yaml.example`):

| Date | Post |
|---|---|
| 2026-04-22 10:00 IST | Launch / founding story |
| 2026-04-24 10:00 IST | Reserved Instance coverage tip |
| 2026-04-29 10:00 IST | GCP cross-region egress war story |
| 2026-05-01 10:00 IST | Indian cloud market observation |
| 2026-05-06 10:00 IST | AI GPU reality |

---

## Step 1 — Create LinkedIn Developer App (5 minutes)

Do this while logged into Anushka's LinkedIn account (the publisher will post as whoever created the app).

1. Go to **https://www.linkedin.com/developers/apps**
2. Click **Create app**
3. Fill in:
   - **App name:** `AICloudStrategist Scheduler`
   - **LinkedIn Page:** Link to the AICloudStrategist company page if it exists, otherwise link to Anushka's personal profile. (If no company page exists yet, skip — the personal profile is enough for personal-feed posting.)
   - **Privacy policy URL:** `https://aicloudstrategist.com/privacy.html`
   - **App logo:** upload the linkedin-banner.png at `d:/aicloud-foundation/docs/linkedin-banner.png` (LinkedIn will crop to square)
   - **Legal agreement:** tick
4. Click **Create**

### Add products

On the app's **Products** tab, request access to:

1. **Sign In with LinkedIn using OpenID Connect** — approved instantly
2. **Share on LinkedIn** — approved instantly

(Do NOT request *Marketing Developer Platform* or *Community Management API* — those require lengthy manual review and are not needed for personal-feed posting.)

### Get credentials

On the app's **Auth** tab:

1. Copy the **Client ID** — a long alphanumeric string
2. Copy the **Client Secret** — click "View" to reveal it
3. Scroll down to **OAuth 2.0 settings** → **Authorized redirect URLs for your app**
4. Click **Add redirect URL** → paste: `https://aicloudstrategist.com/auth/linkedin/callback`
5. Click **Update**

**Leave the browser tab open — you'll need it in Step 3.**

---

## Step 2 — Add credentials to VPS (2 minutes)

SSH to the VPS:

```bash
ssh root@62.72.59.122
# password: Openclaw042026#
```

Create the `.env` file:

```bash
cat > /docker/linkedin-scheduler/.env <<'EOF'
CLIENT_ID=<paste the Client ID from Step 1 here>
CLIENT_SECRET=<paste the Client Secret from Step 1 here>
EOF

chmod 600 /docker/linkedin-scheduler/.env
```

Verify:

```bash
cat /docker/linkedin-scheduler/.env
```

Should show both values.

---

## Step 3 — Run the one-time OAuth auth flow (5 minutes)

On the VPS:

```bash
cd /docker/linkedin-scheduler
python3 auth.py
```

The script prints a long auth URL starting with `https://www.linkedin.com/oauth/v2/authorization?...`.

### In your browser

1. **Make sure you are logged into Anushka's LinkedIn account** (not your own). If you are logged in with a different account, open an incognito window and log in as Anushka first.
2. Copy the auth URL from the terminal and paste it into the browser
3. LinkedIn shows an approval screen: "AICloudStrategist Scheduler would like to access your LinkedIn profile / share content on your behalf"
4. Click **Allow**
5. LinkedIn redirects to `https://aicloudstrategist.com/auth/linkedin/callback?code=AQX...&state=aicloudstrategist-scheduler`
6. The page will probably 404 — that's fine, we only need the `code` value
7. **Copy the `code=` query parameter value from the URL bar** (everything between `code=` and `&state`)

### Back in the terminal

Paste the code when the script prompts for it, then press Enter.

**Successful output:**

```
SUCCESS. Token written to /docker/linkedin-scheduler/token.json
Authenticated as: Anushka B (urn:li:person:xxxxxxx)
Token expires in 5184000 seconds (~60 days).

Next: create posts.yaml and enable cron. See README.md.
```

### If it fails

- `Token exchange failed: 400` — the code you pasted was wrong or expired. Codes expire in ~60 seconds. Re-run `auth.py` and move faster.
- `Token exchange failed: 401` — client ID or secret in `.env` is wrong. Double-check both.
- `redirect_uri mismatch` — the URL in the LinkedIn app's Auth tab must be exactly `https://aicloudstrategist.com/auth/linkedin/callback` (no trailing slash, https not http).

---

## Step 4 — Seed posts.yaml (1 minute)

```bash
cp /docker/linkedin-scheduler/posts.yaml.example /docker/linkedin-scheduler/posts.yaml
ls -la /docker/linkedin-scheduler/posts.yaml
```

Check the 5 posts are there and publish dates look correct. If you want to change dates, edit the file — the cron reads it fresh on every run.

---

## Step 5 — Enable the hourly cron (1 minute)

```bash
(crontab -l 2>/dev/null; echo "0 * * * * /docker/linkedin-scheduler/post.py >> /docker/linkedin-scheduler/cron.log 2>&1") | crontab -

crontab -l | grep linkedin-scheduler
```

You should see:
```
0 * * * * /docker/linkedin-scheduler/post.py >> /docker/linkedin-scheduler/cron.log 2>&1
```

This fires every hour on the hour. The script itself is idempotent — only publishes posts whose `publish_at` has passed and which are not in `published.log`.

---

## Step 6 — Smoke test (1 minute)

```bash
# Dry-run the script manually to verify auth and path
python3 /docker/linkedin-scheduler/post.py
```

**Expected output:**
- If no posts are due: `no posts in posts.yaml` OR silence (normal — posts are in future)
- If a post IS due: `publishing launch-story (scheduled 2026-04-22 10:00)` followed by `published launch-story → urn:li:share:xxx`

**If you see an error** like `no token.json`, Step 3 didn't complete — re-run it.

---

## What happens next

On **April 22 at 10:00 IST** (04:30 UTC), the cron fires. The script sees:
- `launch-story` has `publish_at: "2026-04-22 10:00"` (in the past)
- `launch-story` is not in `published.log`
- It POSTs to LinkedIn's UGC API

Post appears on Anushka's feed. Group gets a Telegram ping with the URN.

Same for the next 4 posts on their scheduled dates.

---

## Ongoing usage

### Schedule new posts

From the VPS:
```bash
cat >> /docker/linkedin-scheduler/posts.yaml <<'EOF'

- id: my-new-post-2026-05-13
  publish_at: "2026-05-13 10:00"
  text: |
    (the post text)
EOF
```

Or from Anushka's phone via Telegram:
```
/schedule 2026-05-13 10:00 My next post about GPU costs...
```
(The bot command writes directly to posts.yaml.)

### See what's scheduled

- `/scheduled` in Telegram — shows the list
- Or SSH: `cat /docker/linkedin-scheduler/posts.yaml`

### Remove a scheduled post

- `/unschedule <id>` in Telegram
- Or edit posts.yaml directly

### Monitor

- `tail -f /docker/linkedin-scheduler/cron.log` — see each hourly fire
- `cat /docker/linkedin-scheduler/published.log` — running record of every post
- Telegram group pings on every success + every failure

### Token expiry

LinkedIn access tokens last ~60 days. The cron alerts the Telegram group 7 days before expiry: *"LinkedIn scheduler: access token expires within 7 days. SSH and run auth.py."*

Re-run Step 3 to refresh the token. Takes 3 minutes.

---

## Troubleshooting

### "Post failed: 401 Unauthorized"

Token has expired. Re-run `auth.py`.

### "Post failed: 403 Forbidden"

The app's "Share on LinkedIn" product wasn't approved. Go back to Step 1, check the Products tab.

### "Post failed: 422 Unprocessable Entity"

Post text has something LinkedIn refuses — usually a suspicious URL or excessive hashtags. Edit the post in posts.yaml and let the cron retry.

### Cron fires but nothing happens

- Check `posts.yaml` has valid YAML syntax (indentation matters)
- Check `publish_at` format is exactly `"YYYY-MM-DD HH:MM"` with quotes
- Run `python3 /docker/linkedin-scheduler/post.py` manually to see errors

---

## Cost

Zero incremental. LinkedIn's API is free for this tier of usage (100 posts/day limit, we use 2/week).

---

*AICloudStrategist · Founder-led. Enterprise-reviewed.*
