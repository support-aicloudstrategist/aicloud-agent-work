#!/bin/bash
# Setup Cron Job for Hourly Session Summaries
# Uses OpenClaw's cron scheduling system

echo "🔧 Setting up hourly summary cron job..."
echo ""

# Create the task definition
cat > hourly-summary-task.json << 'TASKDEF'
{
  "name": "hourly-session-summary",
  "description": "Generate hourly token usage and cost summary",
  "schedule": "0 * * * *",
  "model": "openrouter/google/gemini-2.5-flash-lite",
  "lightContext": true,
  "isolated": true,
  "task": "Generate an hourly session summary report with:\n1. Token usage by model (input/output)\n2. Cost breakdown by model\n3. Cache efficiency stats\n4. Brief work summary\n5. Send to Telegram\n\nUse the format from openrouter-optimization/cron/summary-template.md\nOnly generate if activity detected in last hour (skip if idle).",
  "skipIfIdle": true,
  "activeHours": {
    "start": "09:00",
    "end": "21:00",
    "timezone": "Asia/Calcutta"
  }
}
TASKDEF

echo "✓ Created task definition: hourly-summary-task.json"
echo ""
echo "📋 Cron Job Configuration:"
echo "  Schedule: Every hour at :00 minutes"
echo "  Active Hours: 09:00 - 21:00 (Asia/Calcutta)"
echo "  Model: Gemini 2.5 Flash Lite (cheapest)"
echo "  Cost: ~\$0.0004 per report"
echo "  Daily Cost: ~\$0.005 (12 reports during active hours)"
echo "  Monthly Cost: ~\$0.15"
echo ""
echo "⚠️  To activate this cron job:"
echo "  1. Tell your OpenClaw bot:"
echo "     'Set up a cron job from openrouter-optimization/cron/hourly-summary-task.json'"
echo "  2. Or use OpenClaw CLI:"
echo "     'openclaw cron add --file openrouter-optimization/cron/hourly-summary-task.json'"
echo ""
