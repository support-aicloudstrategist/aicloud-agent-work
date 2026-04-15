#!/usr/bin/env python3
"""
Minimal Telegram bot → claude-mao bridge.
- Long-poll Telegram (no webhook needed)
- Per-chat session continuity via claude session_id
- Cost: $0 per message (Max subscription via shim)
"""
import os, json, time, urllib.request, urllib.parse, urllib.error, pathlib, traceback
from threading import Lock

BOT_TOKEN = os.environ["BOT_TOKEN"]
SHIM_URL  = os.environ.get("SHIM_URL", "http://claude-mao:8080/run")
SHIM_TOKEN = os.environ["SHIM_TOKEN"]
ALLOWED_CHAT_IDS = {int(x) for x in os.environ.get("ALLOWED_CHAT_IDS", "").split(",") if x.strip()}
STATE_DIR = pathlib.Path(os.environ.get("STATE_DIR", "/data"))
STATE_DIR.mkdir(parents=True, exist_ok=True)
STATE_FILE = STATE_DIR / "sessions.json"
LOG_DIR = STATE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

API = f"https://api.telegram.org/bot{BOT_TOKEN}"

state_lock = Lock()
def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"offset": 0, "sessions": {}}
def save_state(s):
    with state_lock:
        STATE_FILE.write_text(json.dumps(s, indent=2))

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)
    with (LOG_DIR / time.strftime("%Y-%m-%d.log")).open("a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S')} {msg}\n")

def tg(method, **params):
    url = f"{API}/{method}"
    data = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None}).encode()
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req, timeout=70) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        log(f"tg {method} HTTP {e.code}: {body[:300]}")
        return {"ok": False, "error": body}
    except Exception as e:
        log(f"tg {method} error: {e}")
        return {"ok": False, "error": str(e)}

def send(chat_id, text, reply_to=None):
    # Telegram limits messages to 4096 chars; split if needed
    chunks = [text[i:i+3900] for i in range(0, len(text), 3900)] or [""]
    for i, c in enumerate(chunks):
        tg("sendMessage", chat_id=chat_id, text=c, reply_to_message_id=(reply_to if i == 0 else None))

def call_shim(prompt, session_id=None):
    body = json.dumps({"prompt": prompt, "session_id": session_id, "max_turns": 12}).encode()
    req = urllib.request.Request(
        SHIM_URL,
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {SHIM_TOKEN}"},
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)

def handle_message(msg, state):
    chat_id = msg["chat"]["id"]
    if ALLOWED_CHAT_IDS and chat_id not in ALLOWED_CHAT_IDS:
        log(f"deny chat={chat_id}")
        send(chat_id, "Sorry, this bot is private.")
        return
    text = (msg.get("text") or "").strip()
    if not text:
        return
    msg_id = msg.get("message_id")
    log(f"recv chat={chat_id} text={text[:120]!r}")

    # built-in commands
    if text.startswith("/"):
        cmd = text.split()[0].lower()
        if cmd in ("/start", "/help"):
            send(chat_id, "Hi. Just send me anything — code questions, research, ops tasks. /new starts a fresh thread. /id shows your chat id.")
            return
        if cmd == "/id":
            send(chat_id, f"chat_id: {chat_id}")
            return
        if cmd == "/new":
            state["sessions"].pop(str(chat_id), None)
            save_state(state)
            send(chat_id, "Started a fresh conversation thread.")
            return

    # let user know we're working
    tg("sendChatAction", chat_id=chat_id, action="typing")

    # carry session per-chat for continuity
    sess = state["sessions"].get(str(chat_id))
    def attempt(sid):
        try:
            return call_shim(text, session_id=sid), None
        except Exception as e:
            return None, e
    result, err = attempt(sess)
    # Fallback: drop session and retry fresh if the shim/Claude signals session trouble
    if result and result.get("exit_code", 0) != 0 and any(
        sig in (result.get("stderr") or "").lower()
        for sig in ("already in use", "not found", "no.*session", "does not exist")
    ):
        log(f"session {sess} not usable; retrying fresh")
        state["sessions"].pop(str(chat_id), None)
        save_state(state)
        result, err = attempt(None)
    if err:
        log(f"shim error: {err}\n{traceback.format_exc()}")
        send(chat_id, f"⚠️ claude-mao error: {err}", reply_to=msg_id)
        return

    new_session = result.get("session_id")
    if new_session:
        state["sessions"][str(chat_id)] = new_session
        save_state(state)

    reply = result.get("result") or "(no reply)"
    if result.get("exit_code", 0) != 0:
        reply = f"⚠️ claude-mao exit={result.get('exit_code')}\n\n{reply}\n\nstderr:\n{result.get('stderr','')[:1000]}"
    send(chat_id, reply, reply_to=msg_id)
    log(f"sent chat={chat_id} chars={len(reply)} dur_ms={result.get('duration_ms')}")

def main():
    state = load_state()
    log(f"starting bot offset={state['offset']} allowed={ALLOWED_CHAT_IDS or '*'}")
    while True:
        try:
            r = tg("getUpdates", offset=state["offset"], timeout=60, allowed_updates=json.dumps(["message"]))
            if not r.get("ok"):
                time.sleep(2); continue
            for upd in r.get("result", []):
                state["offset"] = upd["update_id"] + 1
                save_state(state)
                msg = upd.get("message")
                if not msg: continue
                try:
                    handle_message(msg, state)
                except Exception as e:
                    log(f"handle_message error: {e}\n{traceback.format_exc()}")
        except Exception as e:
            log(f"main loop error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
