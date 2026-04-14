#!/bin/bash
# Hourly Session Summary - Cost-Optimized Report
# Runs every hour, uses Gemini 2.5 Flash (cheapest model)

TIMESTAMP=$(date '+%Y-%m-%d %H:%M %Z')
HOUR_START=$(date -d '1 hour ago' '+%Y-%m-%d %H:00')
HOUR_END=$(date '+%Y-%m-%d %H:00')

# Query session stats (this would typically call OpenClaw API)
# For now, using a placeholder - you'd replace with actual API call
echo "📊 HOURLY SESSION SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "⏰ Period: $HOUR_START - $HOUR_END"
echo "📍 Timezone: Asia/Calcutta"
echo ""
echo "💰 TOKEN USAGE & COST BY MODEL"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "| Model            | Input  | Output | In Cost | Out Cost | Total  |"
echo "|------------------|--------|--------|---------|----------|--------|"
echo "| Haiku 4.5        | TBD    | TBD    | \$TBD   | \$TBD    | \$TBD  |"
echo "| Gemini 2.5 Flash | TBD    | TBD    | \$TBD   | \$TBD    | \$TBD  |"
echo "| Sonnet 4.5       | TBD    | TBD    | \$TBD   | \$TBD    | \$TBD  |"
echo "| TOTAL            | TBD    | TBD    | \$TBD   | \$TBD    | \$TBD  |"
echo ""
echo "📝 WORK SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Activity summary for the last hour..."
echo ""
echo "Next Report: $(date -d '+1 hour' '+%Y-%m-%d %H:00 %Z')"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
