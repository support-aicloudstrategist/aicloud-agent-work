#!/usr/bin/env python3
"""
Webhook receiver that forwards signal-worthy Vikunja task events to Telegram.

Philosophy: trackers generate a lot of events. Most are noise (priority tweaks,
label changes, due-date shuffles). We ping Telegram only for:
  - task.created           — new work added
  - task.updated           — ONLY when the `done` bit flipped
  - task.deleted
  - task.overdue / tasks.overdue
  - task.comment.created
  - task.assignee.created

All other `task.updated` events are swallowed silently (label changes, priority
changes, description edits, due-date changes, title edits).

To tune: edit FILTER_RULES below.
"""
import hashlib
import hmac
import json
import os
import sys
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "")
PORT = int(os.environ.get("PORT", "8090"))
TRACKER_URL = os.environ.get("TRACKER_URL", "https://tracker.srv1562252.hstgr.cloud")

# Event types we care about. For task.updated we additionally require that
# `done` has flipped (see should_notify()).
NOISY_EVENTS = {
    "task.created",
    "task.updated",
    "task.deleted",
    "task.overdue",
    "tasks.overdue",
    "task.comment.created",
    "task.assignee.created",
}

# Debounce state: don't ping if the same (task_id, event_name, done_state)
# fired in the last N seconds. Protects against rapid double-saves.
DEBOUNCE_SECONDS = 10
_recent_events: dict[tuple, float] = {}
_recent_lock = threading.Lock()


def should_notify(payload: dict) -> bool:
    """Return True if this event deserves a Telegram ping."""
    ev = payload.get("event_name", "")
    if ev not in NOISY_EVENTS:
        return False
    data = payload.get("data", {}) or {}
    task = data.get("task", {}) or {}

    # For task.updated, only notify if the `done` bit flipped.
    # There's no direct "old state" in the payload, so we use a conservative
    # heuristic: we already keep track of tasks we've announced as done;
    # if the current state differs from what we last announced (or there's
    # no prior announcement and the task is currently done), it counts as a flip.
    if ev == "task.updated":
        tid = task.get("id")
        cur_done = bool(task.get("done"))
        key = ("done_state", tid)
        with _recent_lock:
            prev = _recent_events.get(key)
            _recent_events[key] = float(cur_done)  # store current state
        if prev is None:
            # First time we've seen an update for this task — only ping if now done
            return cur_done
        return prev != float(cur_done)

    # Debounce every other event on (task_id, event_name)
    tid = task.get("id")
    key = (ev, tid)
    now = time.time()
    with _recent_lock:
        last = _recent_events.get(key)
        _recent_events[key] = now
    if last is not None and (now - last) < DEBOUNCE_SECONDS:
        return False
    return True


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

    tid = task.get("id", "?")
    title = (task.get("title") or "(untitled)").replace("<", "&lt;").replace(">", "&gt;")
    proj = (project.get("title") or "").replace("<", "&lt;").replace(">", "&gt;")
    actor = doer.get("username", "")
    link = f"{TRACKER_URL}/tasks/{tid}"

    if ev == "task.created":
        return f"🟢 new · <b>{proj}</b>\n<a href=\"{link}\">{title}</a>"
    if ev == "task.updated":
        if task.get("done"):
            return f"✅ done · <a href=\"{link}\">{title}</a>\n<i>{proj}</i>"
        else:
            return f"↩️ reopened · <a href=\"{link}\">{title}</a>\n<i>{proj}</i>"
    if ev == "task.deleted":
        return f"🗑 deleted · {title}"
    if ev in ("task.overdue", "tasks.overdue"):
        return f"⏰ <b>overdue</b> · <a href=\"{link}\">{title}</a>\n<i>{proj}</i>"
    if ev == "task.comment.created":
        comment = (data.get("comment", {}) or {}).get("comment", "")
        comment_html = comment.replace("<", "&lt;").replace(">", "&gt;")[:240]
        return f"💬 comment · <a href=\"{link}\">{title}</a>\n{comment_html}"
    if ev == "task.assignee.created":
        assignee = (data.get("assignee", {}) or {}).get("username", "")
        return f"👤 {assignee} assigned · <a href=\"{link}\">{title}</a>"
    return None


def verify_signature(body: bytes, signature_header: str) -> bool:
    if not WEBHOOK_SECRET:
        return True
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

        # Always return 200 quickly; do notification logic after
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

        try:
            if should_notify(payload):
                msg = format_event(payload)
                if msg:
                    send_telegram(msg)
            else:
                ev = payload.get("event_name", "?")
                tid = (payload.get("data", {}) or {}).get("task", {}).get("id", "?")
                print(f"silenced: {ev} task={tid}", file=sys.stderr)
        except Exception as e:
            print("notify error:", e, file=sys.stderr)


def main() -> None:
    srv = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"vikunja-webhook listening on :{PORT}", file=sys.stderr)
    srv.serve_forever()


if __name__ == "__main__":
    main()
