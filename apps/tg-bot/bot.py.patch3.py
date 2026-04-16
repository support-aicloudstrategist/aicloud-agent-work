#!/usr/bin/env python3
"""
Patch 3: adds /schedule command to tg-bot.
Lets Anushka type /schedule 2026-04-22 10:00 <post text> from phone and have it
appended to /docker/linkedin-scheduler/posts.yaml automatically.
Also /scheduled (list) and /unschedule <id>.
Idempotent.
"""
import pathlib, sys

p = pathlib.Path("/docker/tg-bot/bot.py")
src = p.read_text()

if "/schedule" in src and "POSTS_YAML" in src:
    print("already patched (v3)")
    sys.exit(0)

# Inject constants
const = '''
POSTS_YAML = pathlib.Path("/linkedin-scheduler/posts.yaml")
'''
src = src.replace(
    'WORKER_LOG = pathlib.Path("/queue/worker.log")\n',
    'WORKER_LOG = pathlib.Path("/queue/worker.log")\n' + const,
)

# Insert command handlers before "# let user know we're working"
new_cmds = '''
        if cmd == "/schedule":
            # /schedule YYYY-MM-DD HH:MM <post text>
            rest = text.split(None, 1)[1].strip() if len(text.split(None, 1)) > 1 else ""
            parts = rest.split(None, 2)
            if len(parts) < 3:
                send(chat_id, "Usage: /schedule YYYY-MM-DD HH:MM <post text>\\nExample: /schedule 2026-05-06 10:00 My next post about GPU costs...")
                return
            date, tm, post_text = parts
            try:
                import re, datetime
                if not re.match(r"^\\d{4}-\\d{2}-\\d{2}$", date):
                    raise ValueError("bad date format, use YYYY-MM-DD")
                if not re.match(r"^\\d{2}:\\d{2}$", tm):
                    raise ValueError("bad time format, use HH:MM")
                datetime.datetime.strptime(date + " " + tm, "%Y-%m-%d %H:%M")
                # Build a sluggy id from first 30 chars of post
                slug = "".join(c if c.isalnum() else "-" for c in post_text[:40].lower()).strip("-")[:30]
                pid = f"{date}-{slug}"
                if not POSTS_YAML.exists():
                    POSTS_YAML.parent.mkdir(parents=True, exist_ok=True)
                    POSTS_YAML.write_text("")
                # Indented text block for YAML
                indented = "\\n".join("    " + line for line in post_text.split("\\\\n"))
                entry = f"\\n- id: {pid}\\n  publish_at: \\"{date} {tm}\\"\\n  text: |\\n{indented}\\n"
                with POSTS_YAML.open("a") as f:
                    f.write(entry)
                send(chat_id, f"scheduled ✓\\nid: {pid}\\npublish: {date} {tm} IST\\nscheduler fires hourly on VPS.")
            except Exception as e:
                send(chat_id, f"schedule error: {e}")
            return
        if cmd == "/scheduled":
            try:
                if not POSTS_YAML.exists() or not POSTS_YAML.read_text().strip():
                    send(chat_id, "no posts scheduled")
                    return
                content = POSTS_YAML.read_text()
                ids = []
                for line in content.splitlines():
                    if line.startswith("- id:"):
                        ids.append(line.split(":", 1)[1].strip())
                    elif "publish_at:" in line and ids:
                        when = line.split(":", 1)[1].strip().strip("\\"'")
                        ids[-1] = f"{ids[-1]} → {when}"
                msg = "scheduled posts:\\n" + "\\n".join(f"- {i}" for i in ids[:20])
                send(chat_id, msg)
            except Exception as e:
                send(chat_id, f"scheduled error: {e}")
            return
        if cmd == "/unschedule":
            post_id = text.split(None, 1)[1].strip() if len(text.split(None, 1)) > 1 else ""
            if not post_id:
                send(chat_id, "Usage: /unschedule <id>\\nUse /scheduled to see ids.")
                return
            try:
                if not POSTS_YAML.exists():
                    send(chat_id, "no posts.yaml yet")
                    return
                lines = POSTS_YAML.read_text().splitlines()
                out_lines = []
                skip = False
                removed = False
                for line in lines:
                    if line.startswith("- id:") and line.split(":", 1)[1].strip() == post_id:
                        skip = True
                        removed = True
                        continue
                    if skip:
                        if line.startswith("- id:"):
                            skip = False
                            out_lines.append(line)
                        # otherwise continue skipping the block
                        continue
                    out_lines.append(line)
                POSTS_YAML.write_text("\\n".join(out_lines))
                send(chat_id, f"removed {post_id}" if removed else f"id not found: {post_id}")
            except Exception as e:
                send(chat_id, f"unschedule error: {e}")
            return
'''

src = src.replace(
    '    # let user know we\'re working',
    new_cmds + '    # let user know we\'re working',
)

# Update /help text
old_help_line = '\'/bio <platform> — bio for Twitter/meetup/etc\\\\n\\\\n\''
new_help_line = '\'/bio <platform> — bio for Twitter/meetup/etc\\\\n\\\\nLinkedIn scheduler:\\\\n/schedule YYYY-MM-DD HH:MM <post> — schedule a LinkedIn post\\\\n/scheduled — list scheduled posts\\\\n/unschedule <id> — remove a scheduled post\\\\n\\\\n\''
src = src.replace(old_help_line, new_help_line)

p.write_text(src)
print("patched OK (v3)")
