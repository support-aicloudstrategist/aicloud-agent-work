# Telegram Queue — Starter Script Pack

Everything you need to run the overnight task queue from your phone. No laptop required.

---

## TL;DR — from Telegram to `@bill_15_bot`

| Command | What it does |
|---|---|
| `/queue <task>` or `/q <task>` | Add a task to the overnight queue |
| `/qlist` | Show pending tasks (first 20) |
| `/qresults` | Show last ~3.5KB of the results log |
| `/qclear` | Empty the queue |
| `/new` | Start a fresh live-chat thread (doesn't touch the queue) |
| *any other text* | Live chat with claude-mao (synchronous) |

The queue worker fires every minute on the VPS. Laptop off = no problem. Results ping you on Telegram as each task completes.

---

## Writing good queue tasks

Tasks must be **self-contained**. Mao cannot ask you clarifying questions mid-run.

**Good:**
```
/queue Draft a 150-word LinkedIn post on Reserved Instance coverage gaps in Indian SMBs, voice matching apps/outreach/playbook.md Post B, save to /docker/task-queue/data/drafts/post-ri.md and commit.
```

**Bad (ambiguous):**
```
/queue write me a post about clouds
```

A good task includes: **what** to produce, **how** to style it (reference a file or sample), **where** to save it, and **whether to commit**.

---

## Common patterns to copy

### Draft content
```
/queue Draft a 180-word LinkedIn post in the voice of apps/outreach/playbook.md Post A (war story). Topic: [TOPIC]. Save to /docker/task-queue/data/drafts/post-[SLUG].md and commit in /data/work/aicloud-agent-work.
```

### Generate variants
```
/queue Generate 5 subject line variants for the outreach email 2 template. Under 55 chars each, no hype words, Indian tone. Save to /docker/task-queue/data/drafts/subject-email2.md and commit.
```

### Research without sending
```
/queue Research the top 3 competitors to AICloudStrategist in the Indian SMB cloud cost space. For each, list: positioning headline, pricing model (if public), one differentiator we have. Save to /docker/task-queue/data/drafts/competitor-scan.md. Do NOT send any emails or post anywhere.
```

### Audit existing content
```
/queue Audit web/services.html for any AI-tells (leverage, unlock, in today's, fast-paced, seamlessly, delve, navigate, landscape). List file:line + suggested replacement. Do NOT edit the file. Save to /docker/task-queue/data/drafts/services-audit.md.
```

### Prepare a deploy (without applying)
```
/queue Draft the Cloudflare API curl command to update the SPF record on aicloudstrategist.com to include sendgrid.net. Save the command + verification steps to /docker/task-queue/data/drafts/spf-sendgrid-plan.md. Do NOT execute.
```

### Multi-step tasks
Break long multi-step work into 2-3 separate queued tasks — each under 15 min of wall time — so one failure doesn't lose the whole batch. The session persists across queued tasks by default.

---

## SSH fallback (if Telegram bot is down)

From any terminal / phone SSH app:

```bash
ssh root@62.72.59.122   # password: Openclaw042026#

# Add a task
echo "your task here" >> /docker/task-queue/data/queue.txt

# Watch queue
tail -f /docker/task-queue/data/worker.log

# Watch results
tail -f /docker/task-queue/data/results.md

# See what's currently running
cat /docker/task-queue/data/inprogress.txt

# Clear the queue
> /docker/task-queue/data/queue.txt

# Start a fresh mao session (forget prior context)
rm -f /docker/task-queue/data/session_id

# Check cron is alive
systemctl status cron
crontab -l | grep task-queue
```

---

## What's running now (2026-04-15 evening)

8 tasks seeded in the queue — mao will work through them overnight at ~1 per minute (queue is serial, long tasks take the full 30-min slot):

1. LinkedIn post draft — S3 storage tiers
2. LinkedIn post draft — orphaned EBS volumes
3. 8 cold-email subject line variants
4. LinkedIn post draft — GCP egress war story
5. Blog post — RI coverage (300 words)
6. 5 WhatsApp voice-note variants
7. Playbook audit — AI-tells
8. GCP cost checklist lead magnet (draft)

All output lands in `/docker/task-queue/data/drafts/` and is committed to the git repo. You'll get a Telegram ping on each completion.

Run `/qresults` in the morning for the last chunk, or SSH and `cat /docker/task-queue/data/results.md` for the full log.

---

## Operational limits

| Limit | Value | Why |
|---|---|---|
| Max wall time per task | 30 min | `curl --max-time 1800` in worker.sh |
| Max turns per task | 40 | `max_turns=40` in worker.sh |
| Queue worker cadence | 1 / min | Cron entry `* * * * *` |
| Concurrency | 1 | `flock` — serial by design |
| Daily run cap | Set by shim `SHIM_DAILY_BUDGET_USD=5` env | Prevents runaway loops |
| Telegram msg size | 3,900 chars | Auto-split by bot |

If a task exceeds 30 min the curl times out, the task is logged as failed in `results.md`, and the worker moves on. The in-progress file gets cleared.

---

## Escalation — when mao gets stuck

If you see the same task in `inprogress.txt` for more than 40 min, something is hung. Clear it:

```bash
ssh root@62.72.59.122
rm /docker/task-queue/data/.lock /docker/task-queue/data/inprogress.txt
docker restart claude-mao   # only if shim itself is hung
```

Then the next cron fire (within 1 min) will pick up the next task.

---

## What to avoid queueing

- **Tasks that need live approval** ("send this email", "push to prod") — use live chat instead
- **Tasks with external side effects you haven't pre-authorised** (posting on LinkedIn, sending WhatsApp) — always queue the *draft*, review in the morning, then manually trigger the send
- **Open-ended research** ("research cloud trends") — too vague; scope it (word count, sources, output format)
- **Very long tasks** (anything taking >20 min) — break into stages

---

## Bookmark / pin this

Save `@bill_15_bot` on Telegram. All queue commands work from there.

SSH fallback: `root@62.72.59.122` / `Openclaw042026#`

Results archive: `/docker/task-queue/data/results.md` on VPS, append-only.
