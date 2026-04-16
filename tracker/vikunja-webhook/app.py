#!/usr/bin/env python3
"""
Tiny webhook receiver that forwards Vikunja task events to the Telegram group.

Vikunja sends POSTs like:
  {"event_name": "task.created", "time": "...", "data": {"task": {...}, "project": {...}, ...}}

Vikunja can sign webhook requests with a shared secret (HMAC-SHA256 over the body).
We verify, format to a short human-readable line, and send via Telegram Bot API.
"""
import hashlib
import hmac
import json
import os
import sys
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "")
PORT = int(os.environ.get("PORT", "8090"))
TRACKER_URL = os.environ.get("TRACKER_URL", "https://tracker.srv1562252.hstgr.cloud")

# Event types that are interesting enough to ping Telegram for. Others are silent.
NOISY_EVENTS = {
    "task.created",
    "task.updated",
    "task.deleted",
    "task.overdue",
    "task.comment.created",
    "task.assignee.created",
}


def send_telegram(msg: str) -> None:
    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": msg,
        "disable_web_page_preview": "true",
        "parse_mode": "HTML",
    }).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data=data,
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=10).read()
    except Exception as e:
        print("telegram send failed:", e, file=sys.stderr)


def format_event(payload: dict) -> str | None:
    ev = payload.get("event_name", "")
    data = payload.get("data", {}) or {}
    task = data.get("task", {}) or {}
    project = data.get("project", {}) or {}
    doer = data.get("doer", {}) or {}

    if ev not in NOISY_EVENTS:
        return None

    tid = task.get("id", "?")
    title = task.get("title", "(untitled)")
    proj_title = project.get("title", "")
    actor = doer.get("username", "")
    link = f"{TRACKER_URL}/tasks/{tid}"

    title_html = title.replace("<", "&lt;").replace(">", "&gt;")
    proj_html = proj_title.replace("<", "&lt;").replace(">", "&gt;")

    if ev == "task.created":
        return f"🟢 new task in <b>{proj_html}</b>\n<a href=\"{link}\">{title_html}</a>\n— by {actor}"
    if ev == "task.updated":
        if task.get("done"):
            return f"✅ done: <a href=\"{link}\">{title_html}</a>\n<i>{proj_html}</i>"
        return f"✏️ updated: <a href=\"{link}\">{title_html}</a>\n<i>{proj_html}</i>"
    if ev == "task.deleted":
        return f"🗑 deleted: {title_html}"
    if ev == "task.overdue":
        return f"⏰ <b>overdue</b>: <a href=\"{link}\">{title_html}</a>\n<i>{proj_html}</i>"
    if ev == "task.comment.created":
        comment = (data.get("comment", {}) or {}).get("comment", "")
        comment_html = comment.replace("<", "&lt;").replace(">", "&gt;")[:200]
        return f"💬 comment on <a href=\"{link}\">{title_html}</a>\n{comment_html}"
    if ev == "task.assignee.created":
        assignee = (data.get("assignee", {}) or {}).get("username", "")
        return f"👤 {assignee} assigned to <a href=\"{link}\">{title_html}</a>"
    return None


def verify_signature(body: bytes, signature_header: str) -> bool:
    if not WEBHOOK_SECRET:
        return True  # no secret configured, accept all
    if not signature_header:
        return False
    expected = hmac.new(WEBHOOK_SECRET.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header.strip())


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("[vikunja-webhook] " + (fmt % args) + "\n")

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            return
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        signature = self.headers.get("X-Vikunja-Signature", "")
        if not verify_signature(body, signature):
            print("bad signature, rejecting", file=sys.stderr)
            self.send_response(401)
            self.end_headers()
            return

        try:
            payload = json.loads(body.decode("utf-8"))
        except Exception as e:
            print("bad json:", e, file=sys.stderr)
            self.send_response(400)
            self.end_headers()
            return

        msg = format_event(payload)
        if msg:
            send_telegram(msg)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")


def main() -> None:
    srv = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"vikunja-webhook listening on :{PORT}", file=sys.stderr)
    srv.serve_forever()


if __name__ == "__main__":
    main()
