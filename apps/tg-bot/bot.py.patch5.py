#!/usr/bin/env python3
"""
Patch 5: adds /commit command to bot.
Queues a mao task that reviews pending drafts in /docker/task-queue/data/drafts/,
commits them to the git-ops repo with the supplied message, and pushes.
Idempotent.
"""
import pathlib, sys

p = pathlib.Path("/docker/tg-bot/bot.py")
src = p.read_text()

if "/commit" in src and "COMMIT_PROMPT" in src:
    print("already patched (v5)")
    sys.exit(0)

const = '''
COMMIT_PROMPT = (
    "You are helping maintain the AICloudStrategist git repo at /data/work/aicloud-agent-work "
    "(inside the git-ops container). The drafts directory at /docker/task-queue/data/drafts/ "
    "contains new content produced by earlier mao tasks. Your job: (1) list any files in "
    "/docker/task-queue/data/drafts/ that are not yet in the git repo drafts/ folder, "
    "(2) copy them into the repo via: docker cp /docker/task-queue/data/drafts/ git-ops:/tmp/drafts/ && "
    "docker exec git-ops sh -c 'cp -r /tmp/drafts/* /data/work/aicloud-agent-work/drafts/', "
    "(3) inside git-ops container run: git add -A && git -c user.email=support@aicloudstrategist.com "
    "-c user.name=\\"Anushka B\\" commit -m \\"{message}\\" && git push origin main, "
    "(4) report back: which files were committed + the commit hash. "
    "If there are no new files to commit, report 'nothing to commit'. "
    "Do NOT commit anything outside /docker/task-queue/data/drafts/."
)
'''
src = src.replace(
    'FOLLOWUP_TEMPLATE_URL = "https://raw.githubusercontent.com/support-aicloudstrategist/aicloud-agent-work/main/docs/health-check-followup-template.md"\n',
    'FOLLOWUP_TEMPLATE_URL = "https://raw.githubusercontent.com/support-aicloudstrategist/aicloud-agent-work/main/docs/health-check-followup-template.md"\n' + const,
)

new_cmd = '''
        if cmd == "/commit":
            msg = text.split(None, 1)[1].strip() if len(text.split(None, 1)) > 1 else ""
            if not msg:
                send(chat_id, "Usage: /commit <message>\\n\\nExample: /commit drafts: polish latest LinkedIn posts\\n\\nReviews pending files in /docker/task-queue/data/drafts/, commits them to the aicloud-agent-work repo, pushes to main. Reports back with commit hash.")
                return
            safe_msg = msg.replace('"', "\\\\\\"").replace("\\n", " ")[:200]
            task = COMMIT_PROMPT.replace("{message}", safe_msg)
            try:
                with QUEUE_FILE.open("a") as f:
                    f.write(task + "\\n")
                send(chat_id, f"commit queued: {safe_msg[:100]}\\nmao will run in next ~60 sec and ping back with result.")
            except Exception as e:
                send(chat_id, f"commit error: {e}")
            return
'''

src = src.replace(
    "    # let user know we're working",
    new_cmd + "    # let user know we're working",
)

# Update /help
old_help_fragment = '\'/followup <client> | <finding 1> | <finding 2> | <finding 3>\\\\n\\\\n\''
new_help_fragment = '\'/followup <client> | <finding 1> | <finding 2> | <finding 3>\\\\n/commit <message> — commit pending drafts to git\\\\n\\\\n\''
src = src.replace(old_help_fragment, new_help_fragment)

p.write_text(src)
print("patched OK (v5)")
