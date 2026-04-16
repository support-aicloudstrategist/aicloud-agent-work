#!/usr/bin/env python3
"""
Patch 4: adds /followup command to tg-bot.
Anushka types after a Health Check call: /followup <client name> | <finding 1> | <finding 2> | <finding 3>
Bot queues a task that mao expands into a fully-formatted follow-up email
using docs/health-check-followup-template.md.
Idempotent.
"""
import pathlib, sys

p = pathlib.Path("/docker/tg-bot/bot.py")
src = p.read_text()

if "/followup" in src and "FOLLOWUP_TEMPLATE_URL" in src:
    print("already patched (v4)")
    sys.exit(0)

const = '''
FOLLOWUP_TEMPLATE_URL = "https://raw.githubusercontent.com/support-aicloudstrategist/aicloud-agent-work/main/docs/health-check-followup-template.md"
'''
src = src.replace(
    'POSTS_YAML = pathlib.Path("/linkedin-scheduler/posts.yaml")\n',
    'POSTS_YAML = pathlib.Path("/linkedin-scheduler/posts.yaml")\n' + const,
)

new_cmd = '''
        if cmd == "/followup":
            # /followup <client name> | <finding 1> | <finding 2> | <finding 3>
            rest = text.split(None, 1)[1].strip() if len(text.split(None, 1)) > 1 else ""
            if "|" not in rest or rest.count("|") < 3:
                send(chat_id, "Usage: /followup <client name> | <finding 1> | <finding 2> | <finding 3>\\n\\nExample:\\n/followup Acme Logistics | 41% idle EC2 fleet ~₹4L/month | 47TB S3 Standard cold data ~₹1.5L/month | RI coverage 12% ~₹2.8L/month\\n\\nProduces the full post-call follow-up email using docs/health-check-followup-template.md.")
                return
            parts = [p.strip() for p in rest.split("|", 3)]
            client = parts[0]
            findings = parts[1:4]
            slug = "".join(c if c.isalnum() else "-" for c in client.lower())[:40].strip("-")
            task = (
                f"Read the follow-up template at {FOLLOWUP_TEMPLATE_URL} via WebFetch. "
                f"Fill it in for client \\"{client}\\" with these three findings from today's Health Check call:\\n"
                f"1. {findings[0]}\\n"
                f"2. {findings[1]}\\n"
                f"3. {findings[2]}\\n"
                "For each finding, write the 'What we see' / 'Why it is probably happening' / 'Recoverable estimate' / 'Effort to close' / 'Risk level' blocks in Anushka's voice — specific, Indian-business tone, INR-first, no hype. Extract the rupee figures from the findings text provided. Compute the combined table and annualised total. Fill the three options (DIY / QuickStart / Gain-share) with realistic numbers based on the total recoverable spend. "
                f"Save the complete email-ready markdown to /docker/task-queue/data/drafts/followup-{slug}.md. "
                "Start output with 'Subject: ...' line so the whole document is a drop-in email. "
                "Use 'Anushka B' in signoff. Do not invent facts not in the findings."
            )
            try:
                with QUEUE_FILE.open("a") as f:
                    f.write(task + "\\n")
                send(chat_id, f"follow-up queued for {client} → drafts/followup-{slug}.md\\npings back when ready (~90 sec).")
            except Exception as e:
                send(chat_id, f"followup error: {e}")
            return
'''

src = src.replace(
    '    # let us know we\\\'re working',
    new_cmd + '    # let us know we\\\'re working',
)
# If the above marker line format changed, try the actual string with single quote handling
if '/followup' not in src:
    src = src.replace(
        "    # let user know we're working",
        new_cmd + "    # let user know we're working",
    )

# Update /help text — append followup helper
old_help = '\'LinkedIn scheduler:\\\\n/schedule YYYY-MM-DD HH:MM <post> — schedule a LinkedIn post\\\\n/scheduled — list scheduled posts\\\\n/unschedule <id> — remove a scheduled post\\\\n\\\\n\''
new_help = '\'LinkedIn scheduler:\\\\n/schedule YYYY-MM-DD HH:MM <post> — schedule a LinkedIn post\\\\n/scheduled — list scheduled posts\\\\n/unschedule <id> — remove a scheduled post\\\\n\\\\nAfter a Health Check call:\\\\n/followup <client> | <finding 1> | <finding 2> | <finding 3>\\\\n\\\\n\''
src = src.replace(old_help, new_help)

p.write_text(src)
print("patched OK (v4)")
