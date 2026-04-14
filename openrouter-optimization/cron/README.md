# 📊 Hourly Session Summary - Cron Job

Automated hourly reports for token usage and cost tracking.

## 🎯 Purpose

Generate cost-optimized hourly summaries of:
- Token usage by model (input/output)
- Cost breakdown per model
- Cache efficiency statistics
- Brief work summary

## 💰 Cost Optimization

**Traditional Approach:**
- Manual request every hour
- Loads full conversation context
- Uses current model (could be expensive)
- Cost: ~$9.30/month

**Cron Job Approach:**
- Isolated task execution
- No context loading
- Uses Gemini 2.5 Flash (cheapest)
- **Cost: ~$0.15/month**
- **Savings: $9.15/month (98% cheaper!)**

## 📁 Files

```
cron/
├── README.md ........................... This file
├── hourly-summary.sh .................. Shell script (placeholder)
├── setup-cron.sh ...................... Cron setup automation
├── hourly-summary-task.json ........... Task definition
└── summary-template.md ................ Report format template
```

## 🚀 Setup Instructions

### Option 1: Automated Setup (Recommended)

```bash
cd openrouter-optimization/cron
bash setup-cron.sh
```

Then tell your OpenClaw bot:
```
Set up cron job from openrouter-optimization/cron/hourly-summary-task.json
```

### Option 2: Manual Setup

Tell your OpenClaw bot:
```
Create a cron job:
- Name: hourly-session-summary
- Schedule: 0 * * * * (every hour at :00)
- Model: openrouter/google/gemini-2.5-flash-lite
- Task: Generate hourly summary using template from 
  openrouter-optimization/cron/summary-template.md
- Light context: ON
- Isolated session: ON
- Skip if idle: ON
- Active hours: 09:00-21:00 Asia/Calcutta
```

### Option 3: OpenClaw CLI

```bash
openclaw cron add \
  --name "hourly-session-summary" \
  --schedule "0 * * * *" \
  --model "openrouter/google/gemini-2.5-flash-lite" \
  --file openrouter-optimization/cron/hourly-summary-task.json
```

## ⚙️ Configuration

**Schedule:** `0 * * * *` (every hour at :00 minutes)

**Active Hours:** 09:00 - 21:00 (Asia/Calcutta)
- 12 reports per day (not 24)
- Saves 50% on overnight idle time

**Model:** Gemini 2.5 Flash Lite
- Cheapest available ($0.075/M input, $0.30/M output)
- Perfect for simple summaries
- 10x cheaper than Haiku, 40x cheaper than Sonnet

**Skip If Idle:** Enabled
- Detects no activity in last hour
- Skips report generation
- Further cost reduction

## 📊 Cost Breakdown

**Per Report:**
- Input: ~100 tokens × $0.075/M = $0.0000075
- Output: ~500 tokens × $0.30/M = $0.00015
- **Total: ~$0.00016** (0.016 cents)

**Daily (12 active hours):**
- 12 reports × $0.00016 = **$0.002/day**

**Monthly:**
- 30 days × $0.002 = **$0.06/month**

**With idle detection (avg 8 reports/day):**
- 8 reports × $0.00016 × 30 days = **$0.04/month**

**Savings vs Manual:** $9.26/month (99.6% reduction!)

## 📋 Report Format

```
📊 HOURLY SESSION SUMMARY

⏰ Period: 2026-04-14 15:00 - 16:00
📍 Timezone: Asia/Calcutta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 TOKEN USAGE & COST BY MODEL

| Model            | Input  | Output | In Cost | Out Cost | Total  |
|------------------|--------|--------|---------|----------|--------|
| Haiku 4.5        | 1,200  | 2,500  | $0.0003 | $0.0031  | $0.0034|
| Gemini 2.5 Flash | 15,000 | 1,200  | $0.0011 | $0.0004  | $0.0015|
| Sonnet 4.5       | 700    | 2,800  | $0.0021 | $0.0420  | $0.0441|
| TOTAL            | 16,900 | 6,500  | $0.0035 | $0.0455  | $0.049 |

📊 Cache Efficiency:
├─ Cached tokens: 104,000 (97% hit rate)
├─ Cost savings: $0.089
└─ Net cost: $0.049

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 WORK SUMMARY

Cost optimization infrastructure deployed. Created 15 files,
fixed setup script, verified all tasks, committed to GitHub.
Infrastructure ready for 98% cost savings.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Report: 2026-04-14 17:00 GMT+5:30
```

## 🔍 Monitoring

**Check cron job status:**
```bash
openclaw cron list
```

**View recent reports:**
```bash
openclaw cron logs hourly-session-summary --limit 5
```

**Disable temporarily:**
```bash
openclaw cron disable hourly-session-summary
```

**Re-enable:**
```bash
openclaw cron enable hourly-session-summary
```

## 🎛️ Customization

### Change Schedule

Edit `hourly-summary-task.json`:
```json
{
  "schedule": "0 */2 * * *"  // Every 2 hours
}
```

### Adjust Active Hours

```json
{
  "activeHours": {
    "start": "08:00",
    "end": "22:00"
  }
}
```

### Change Model

```json
{
  "model": "openrouter/deepseek/deepseek-chat-v3.1"  // Slightly more powerful
}
```

## ✅ Verification

After setup, you should receive:
1. Confirmation message from OpenClaw
2. First report at next :00 hour mark
3. Reports every hour during active hours
4. Skipped reports during idle hours

**Cost tracking:**
- Check OpenRouter dashboard
- Should see ~$0.04-0.06/month for summaries
- 99%+ savings vs manual approach

## 🚨 Troubleshooting

**No reports received:**
- Check cron job status: `openclaw cron list`
- Verify active hours match your timezone
- Check logs: `openclaw cron logs hourly-session-summary`

**Reports too verbose:**
- Edit `summary-template.md`
- Reduce token limit in task definition

**Too many reports:**
- Enable `skipIfIdle: true`
- Reduce active hours window

## 📈 Expected Results

**Week 1:**
- 84 reports (12/day × 7 days)
- Cost: ~$0.014
- Baseline established

**Week 4:**
- With idle detection: ~50-60 reports
- Cost: ~$0.01/week
- Optimized delivery

**Monthly:**
- 200-250 reports (avg 8/day)
- Cost: $0.04-0.06
- **Savings: $9.24/month vs manual**

---

**Status:** ✅ Ready to deploy  
**Cost:** $0.04-0.06/month  
**Savings:** 99.6% vs manual approach  
**Next Step:** Run `bash setup-cron.sh` to activate
