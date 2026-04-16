#!/usr/bin/env python3
"""
Print the LinkedIn OAuth authorization URL.
Anushka opens this in her browser and clicks Allow.
"""
import pathlib, urllib.parse, sys

ENV_FILE = pathlib.Path("/docker/linkedin-scheduler/.env")
REDIRECT = "https://aicloudstrategist.com/auth/linkedin/callback"
SCOPES = "openid profile email w_member_social"

def read_env():
    if not ENV_FILE.exists():
        print("ERROR: /docker/linkedin-scheduler/.env missing.", file=sys.stderr)
        sys.exit(1)
    env = {}
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env

env = read_env()
url = "https://www.linkedin.com/oauth/v2/authorization?" + urllib.parse.urlencode({
    "response_type": "code",
    "client_id": env["CLIENT_ID"],
    "redirect_uri": REDIRECT,
    "scope": SCOPES,
    "state": "aicloudstrategist-scheduler",
})
print(url)
