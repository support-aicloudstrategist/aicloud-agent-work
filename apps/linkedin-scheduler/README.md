# LinkedIn Auto-Post Scheduler

A small cron-driven script that publishes pre-written posts to Anushka's LinkedIn feed on a schedule. Runs on the VPS — laptop does not need to be on.

## Architecture

```
posts.yaml (schedule)  →  linkedin-post.py (cron every hour)  →  LinkedIn API  →  @bill_15_bot ping (group)
```

- **posts.yaml** — schedule file: post text + publish datetime (IST)
- **linkedin-post.py** — script that runs hourly, checks if any post is due (within last 60 min and not yet published), calls LinkedIn API
- **LinkedIn access token** — stored at `/docker/linkedin-scheduler/token.json`, refreshed via OAuth as needed
- **published.log** — append-only record of what was published when (prevents duplicate posts on re-runs)

## One-time setup

### Step 1 — Create a LinkedIn Developer App

Anushka does this once:

1. Go to https://www.linkedin.com/developers/apps
2. Click "Create app"
3. App name: `AICloudStrategist Scheduler`
4. LinkedIn Page: link to AICloudStrategist company page (create one first if it doesn't exist)
5. Legal agreement: accept
6. Click Create

Once the app is created:

7. Go to "Products" tab → request access to:
   - **Share on LinkedIn** (for posting to personal feed)
   - **Sign In with LinkedIn using OpenID Connect** (for user authentication)
   - If posting to a Company Page: also **Community Management API**

LinkedIn usually approves these instantly for personal/small company apps.

### Step 2 — Get OAuth tokens

From the app's "Auth" tab:

1. Copy **Client ID** and **Client Secret**
2. Add redirect URL: `https://aicloudstrategist.com/auth/linkedin/callback` (doesn't need to resolve for one-time auth — any page that shows the query string is enough)
3. Run the one-time auth flow (below)

### Step 3 — One-time auth flow

On the VPS:

```bash
cd /docker/linkedin-scheduler
python3 auth.py
```

This prints an auth URL. Anushka opens it in her browser (while logged into her LinkedIn account), approves the app, and is redirected to `https://aicloudstrategist.com/auth/linkedin/callback?code=XYZ...`.

Copy the `code` query param value and paste it back into the terminal when prompted.

The script exchanges it for an access token and writes `/docker/linkedin-scheduler/token.json`. Token is valid 60 days; refresh tokens extend automatically.

### Step 4 — Enable cron

```bash
(crontab -l; echo "0 * * * * /docker/linkedin-scheduler/post.py >> /docker/linkedin-scheduler/cron.log 2>&1") | crontab -
```

Runs every hour on the hour. The script is idempotent — it only posts items whose `publish_at` is in the last 60 minutes and not in `published.log`.

## Adding posts to the schedule

Edit `/docker/linkedin-scheduler/posts.yaml`:

```yaml
- id: launch-post
  publish_at: "2026-04-22 10:00"  # IST (Asia/Kolkata)
  text: |
    Seven years into working independently across DevOps...

- id: ri-tip
  publish_at: "2026-04-24 10:00"
  text: |
    If your AWS Reserved Instance coverage is below 70%...
```

On next cron fire, the scheduler picks up new entries automatically. No restart needed.

## Monitoring

- **Cron output:** `/docker/linkedin-scheduler/cron.log`
- **Publish record:** `/docker/linkedin-scheduler/published.log`
- **Telegram ping on publish:** each successful post triggers a message to the group with the LinkedIn post URL

## Pausing

Remove the cron entry, or set a future date on all pending posts.

## Limitations

- **LinkedIn rate limit:** ~100 posts per day per app (far higher than we'll ever hit)
- **Text-only posts** on the first version. Images, PDFs, videos can be added later — the LinkedIn API supports them, but requires multi-step upload.
- **No editing after publish.** LinkedIn does not provide an edit-post API. Fix-ups are manual.
- **Company Page vs personal profile:** this scheduler posts to whichever profile owns the access token. For company page posts, the token must have `w_organization_social` scope and the author URN must be the organization URN.

## References

- LinkedIn Share API: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/share-api
- LinkedIn OAuth 2.0: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow
- UGC Post API: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/ugc-post-api
