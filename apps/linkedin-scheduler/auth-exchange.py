#!/usr/bin/env python3
"""
Exchange an OAuth code for an access token, write token.json.
Non-interactive — takes the code as argv[1].

Usage: python3 auth-exchange.py <code>
"""
import os, json, pathlib, urllib.parse, urllib.request, urllib.error, sys, time

ENV_FILE = pathlib.Path("/docker/linkedin-scheduler/.env")
TOKEN_FILE = pathlib.Path("/docker/linkedin-scheduler/token.json")
REDIRECT = "https://aicloudstrategist.com/auth/linkedin/callback"

if len(sys.argv) < 2:
    print("Usage: auth-exchange.py <code>", file=sys.stderr)
    sys.exit(1)

code = sys.argv[1].strip()

# Read env
env = {}
for line in ENV_FILE.read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line:
        continue
    k, v = line.split("=", 1)
    env[k.strip()] = v.strip()

# Exchange code for access token
body = urllib.parse.urlencode({
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT,
    "client_id": env["CLIENT_ID"],
    "client_secret": env["CLIENT_SECRET"],
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
    print("Token exchange failed:", e.code, e.read().decode(), file=sys.stderr)
    sys.exit(2)

# Fetch user URN
userinfo_req = urllib.request.Request(
    "https://api.linkedin.com/v2/userinfo",
    headers={"Authorization": f"Bearer {tok['access_token']}"},
)
try:
    with urllib.request.urlopen(userinfo_req, timeout=30) as r:
        info = json.load(r)
except Exception as e:
    print("Userinfo fetch failed:", e, file=sys.stderr)
    info = {}

tok["_user_sub"] = info.get("sub")
tok["_author_urn"] = f"urn:li:person:{info['sub']}" if info.get("sub") else None
tok["_name"] = info.get("name")
tok["_fetched_at"] = time.time()

TOKEN_FILE.write_text(json.dumps(tok, indent=2))
os.chmod(TOKEN_FILE, 0o600)

print(f"SUCCESS. Authenticated as: {info.get('name')} ({tok.get('_author_urn')})")
print(f"Token expires in {tok.get('expires_in')} seconds (~60 days).")
