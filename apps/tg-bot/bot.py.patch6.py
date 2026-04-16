#!/usr/bin/env python3
"""
Patch 6: adds /stats command — reads the latest weekly-digest.log entry.
Idempotent.
"""
import pathlib, sys

p = pathlib.Path("/docker/tg-bot/bot.py")
src = p.read_text()

if '"/stats"' in src:
    print("already patched (v6)")
    sys.exit(0)

new_cmd = '''
        if cmd == "/stats":
            log_path = pathlib.Path("/queue/weekly-digest.log")
            try:
                if not log_path.exists():
                    send(chat_id, "No digest run yet. Monday 09:00 IST cron will fire automatically. For on-demand, SSH and run: /docker/task-queue/bin/weekly-digest.sh")
                    return
                lines = log_path.read_text().strip().splitlines()
                if not lines:
                    send(chat_id, "Digest log empty. Check cron.")
                    return
                last = lines[-1]
                send(chat_id, f"Last weekly digest entry:\\n{last}\\n\\nMonday cron runs at 09:00 IST. Full dashboard: https://analytics.aicloudstrategist.com")
            except Exception as e:
                send(chat_id, f"stats error: {e}")
            return
'''

src = src.replace(
    "    # let user know we're working",
    new_cmd + "    # let user know we're working",
)

# Update /help
old_help = '\'/followup <client> | <finding 1> | <finding 2> | <finding 3>\\\\n/commit <message> — commit pending drafts to git\\\\n\\\\n\''
new_help = '\'/followup <client> | <finding 1> | <finding 2> | <finding 3>\\\\n/commit <message> — commit pending drafts to git\\\\n/stats — last weekly analytics digest summary\\\\n\\\\n\''
src = src.replace(old_help, new_help)

p.write_text(src)
print("patched OK (v6)")
