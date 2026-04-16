#!/usr/bin/env python3
"""
One-time OAuth flow for LinkedIn scheduler.
Run interactively on VPS. Prints auth URL, asks for the code query param
from the redirect, exchanges for access token, writes token.json.

Requires: CLIENT_ID and CLIENT_SECRET in /docker/linkedin-scheduler/.env
"""
import os, json, pathlib, urllib.parse, urllib.request, urllib.error, sys

ENV_FILE = pathlib.Path("/docker/linkedin-scheduler/.env")
TOKEN_FILE = pathlib.Path("/docker/linkedin-scheduler/token.json")
REDIRECT = "https://aicloudstrategist.com/auth/linkedin/callback"
SCOPES = "openid profile email w_member_social"

def read_env():
    if not ENV_FILE.exists():
        print("ERROR: /docker/linkedin-scheduler/.env missing.")
        print("Create it with:")
        print("  CLIENT_ID=...")
        print("  CLIENT_SECRET=...")
        sys.exit(1)
    env = {}
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env

def main():
    env = read_env()
    cid = env["CLIENT_ID"]
    csec = env["CLIENT_SECRET"]

    # Step 1: print the auth URL
    auth_url = "https://www.linkedin.com/oauth/v2/authorization?" + urllib.parse.urlencode({
        "response_type": "code",
        "client_id": cid,
        "redirect_uri": REDIRECT,
        "scope": SCOPES,
        "state": "aicloudstrategist-scheduler",
    })
    print("Open this URL in a browser while logged into Anushka's LinkedIn account:")
    print()
    print(auth_url)
    print()
    print("After approving, you'll be redirected to aicloudstrategist.com/auth/linkedin/callback")
    print("The page won't exist — but the URL will contain ?code=... — copy that code value.")
    print()
    code = input("Paste the code value here: ").strip()

    # Step 2: exchange code for access token
    body = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT,
        "client_id": cid,
        "client_secret": csec,
    }).encode()

    req = urllib.request.Request(
        "https://www.linkedin.com/oauth/v2/accessToken",
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            tok = json.load(r)
    except urllib.error.HTTPError as e:
        print("Token exchange failed:", e.code, e.read().decode())
        sys.exit(1)

    # Step 3: fetch user URN (needed to post on behalf of this user)
    userinfo_req = urllib.request.Request(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {tok['access_token']}"},
    )
    try:
        with urllib.request.urlopen(userinfo_req, timeout=30) as r:
            info = json.load(r)
    except Exception as e:
        print("Could not fetch userinfo:", e)
        info = {}

    tok["_user_sub"] = info.get("sub")
    tok["_author_urn"] = f"urn:li:person:{info['sub']}" if info.get("sub") else None
    tok["_name"] = info.get("name")
    tok["_fetched_at"] = __import__("time").time()

    TOKEN_FILE.write_text(json.dumps(tok, indent=2))
    os.chmod(TOKEN_FILE, 0o600)
    print()
    print("SUCCESS. Token written to", TOKEN_FILE)
    print(f"Authenticated as: {info.get('name')} ({tok.get('_author_urn')})")
    print("Token expires in", tok.get("expires_in"), "seconds (~60 days).")
    print()
    print("Next: create posts.yaml and enable cron. See README.md.")

if __name__ == "__main__":
    main()
