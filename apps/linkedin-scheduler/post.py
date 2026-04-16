#!/usr/bin/env python3
"""
Hourly cron job. Reads posts.yaml, finds any post whose publish_at is in the
last 60 minutes AND not yet in published.log, and posts it via LinkedIn API.

Sends a Telegram ping to the group on success or failure.
"""
import os, json, pathlib, urllib.request, urllib.parse, urllib.error, time, sys, datetime, re

BASE = pathlib.Path("/docker/linkedin-scheduler")
POSTS_FILE = BASE / "posts.yaml"
TOKEN_FILE = BASE / "token.json"
PUBLISHED = BASE / "published.log"
CRON_LOG = BASE / "cron.log"
ENV_FILE = pathlib.Path("/docker/tg-bot/.env")

TG_CHAT_ID = "-4955349765"  # Raj+Anushka+bill group


def log(msg):
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with CRON_LOG.open("a") as f:
        f.write(line + "\n")


def load_yaml_simple(path):
    """Parse the very limited YAML schema used by posts.yaml — no deps required."""
    if not path.exists():
        return []
    posts = []
    current = None
    body = None
    for raw in path.read_text().splitlines():
        if raw.startswith("- id:"):
            if current:
                if body is not None:
                    current["text"] = "\n".join(body).rstrip()
                posts.append(current)
            current = {"id": raw.split(":", 1)[1].strip()}
            body = None
        elif current and raw.startswith("  publish_at:"):
            current["publish_at"] = raw.split(":", 1)[1].strip().strip('"').strip("'")
        elif current and raw.startswith("  text: |"):
            body = []
        elif body is not None and (raw.startswith("    ") or raw == ""):
            body.append(raw[4:] if raw.startswith("    ") else "")
        elif raw.strip() == "":
            continue
    if current:
        if body is not None:
            current["text"] = "\n".join(body).rstrip()
        posts.append(current)
    return posts


def already_published(post_id):
    if not PUBLISHED.exists():
        return False
    return any(line.startswith(post_id + "\t") for line in PUBLISHED.read_text().splitlines())


def mark_published(post_id, urn):
    with PUBLISHED.open("a") as f:
        f.write(f"{post_id}\t{datetime.datetime.now().isoformat(timespec='seconds')}\t{urn}\n")


def tg_ping(msg):
    try:
        if not ENV_FILE.exists():
            return
        bot_token = None
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("BOT_TOKEN="):
                bot_token = line.split("=", 1)[1].strip()
                break
        if not bot_token:
            return
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        body = urllib.parse.urlencode({"chat_id": TG_CHAT_ID, "text": msg}).encode()
        urllib.request.urlopen(urllib.request.Request(url, data=body), timeout=15).read()
    except Exception as e:
        log(f"tg_ping failed: {e}")


def parse_publish_at(s):
    """Parse IST timestamp. Returns epoch seconds."""
    # Expected format: "2026-04-22 10:00" (IST = UTC+5:30)
    dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
    # Convert IST to UTC, then to epoch
    dt_utc = dt - datetime.timedelta(hours=5, minutes=30)
    return dt_utc.replace(tzinfo=datetime.timezone.utc).timestamp()


def post_to_linkedin(token_data, text):
    """POST to LinkedIn UGC Posts API. Returns post URN on success."""
    author_urn = token_data["_author_urn"]
    access_token = token_data["access_token"]
    if not author_urn:
        raise RuntimeError("no _author_urn in token.json — re-run auth.py")
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    req = urllib.request.Request(
        "https://api.linkedin.com/v2/ugcPosts",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        # LinkedIn returns the URN in X-RestLi-Id header for 201 responses
        urn = r.headers.get("X-RestLi-Id") or r.headers.get("x-restli-id") or ""
        return urn


def main():
    if not TOKEN_FILE.exists():
        log("no token.json — run auth.py first")
        sys.exit(0)
    token_data = json.loads(TOKEN_FILE.read_text())

    # Check token age (LinkedIn tokens are 60 days)
    fetched = token_data.get("_fetched_at", 0)
    expires_in = token_data.get("expires_in", 5184000)
    age = time.time() - fetched
    if age > expires_in - 7 * 86400:  # less than 7 days left
        log("token expires soon — manual refresh needed via auth.py")
        tg_ping("⚠️ LinkedIn scheduler: access token expires within 7 days. SSH to VPS and run /docker/linkedin-scheduler/auth.py to refresh.")

    posts = load_yaml_simple(POSTS_FILE)
    if not posts:
        log("no posts in posts.yaml")
        return

    now = time.time()
    for post in posts:
        if "publish_at" not in post or "text" not in post or "id" not in post:
            continue
        if already_published(post["id"]):
            continue
        try:
            publish_ts = parse_publish_at(post["publish_at"])
        except Exception as e:
            log(f"skip {post['id']}: bad publish_at {post['publish_at']} — {e}")
            continue

        # Fire if due in the last 60 minutes (not in future, not older than 1hr)
        # We give a 60-minute window because cron runs hourly
        if publish_ts > now:
            continue  # not yet due
        if now - publish_ts > 3600:
            # More than 1 hour past — but we still want to fire once if missed
            # (e.g., if cron was down). Fire anyway, but log a delay warning.
            log(f"post {post['id']} publish_at was {int((now-publish_ts)/60)}min ago — firing late")

        log(f"publishing {post['id']} (scheduled {post['publish_at']})")
        try:
            urn = post_to_linkedin(token_data, post["text"])
            mark_published(post["id"], urn)
            preview = post["text"][:200].replace("\n", " ")
            log(f"published {post['id']} → {urn}")
            tg_ping(f"✓ LinkedIn post published\n\nID: {post['id']}\nURN: {urn}\n\n{preview}...")
        except urllib.error.HTTPError as e:
            err = e.read().decode(errors="replace")[:500]
            log(f"FAILED {post['id']}: HTTP {e.code} — {err}")
            tg_ping(f"❌ LinkedIn post FAILED\n\nID: {post['id']}\nHTTP {e.code}\n{err}")
        except Exception as e:
            log(f"FAILED {post['id']}: {e}")
            tg_ping(f"❌ LinkedIn post FAILED\n\nID: {post['id']}\nError: {e}")


if __name__ == "__main__":
    main()
