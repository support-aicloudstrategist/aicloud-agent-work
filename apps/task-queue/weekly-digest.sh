#!/bin/bash
# Weekly analytics digest for AICloudStrategist.
# Runs every Monday 09:00 IST (03:30 UTC).
# Queries Plausible, composes a short group-friendly summary, pings Telegram.

set -euo pipefail

PLAUSIBLE_URL="https://analytics.aicloudstrategist.com"
SITE_ID="aicloudstrategist.com"
# Plausible self-hosted exposes stats via /api/v1/stats/... using a site API key
# We use the Plausible container's internal unauthenticated API by running queries in the DB directly.

LOG=/docker/task-queue/data/weekly-digest.log
BOT=$(grep '^BOT_TOKEN=' /docker/tg-bot/.env | cut -d= -f2-)
CHAT=-4955349765

ts() { date -Is; }

query_db() {
    # Run a ClickHouse query against the Plausible events DB
    local sql="$1"
    docker exec plausible-analytics-iedj-plausible_events_db-1 clickhouse-client --query "$sql" 2>/dev/null || echo "0"
}

# Last 7 days, rolling window
SINCE=$(date -d '7 days ago' '+%Y-%m-%d %H:%M:%S')
NOW=$(date '+%Y-%m-%d %H:%M:%S')

# Total pageviews
PAGEVIEWS=$(query_db "SELECT count(*) FROM plausible_events_db.events_v2 WHERE site_id = 1 AND name = 'pageview' AND timestamp >= '${SINCE}' AND timestamp <= '${NOW}'")

# Unique visitors (user_id distinct)
VISITORS=$(query_db "SELECT uniq(user_id) FROM plausible_events_db.events_v2 WHERE site_id = 1 AND name = 'pageview' AND timestamp >= '${SINCE}' AND timestamp <= '${NOW}'")

# Top 5 pages
TOP_PAGES=$(query_db "SELECT pathname, count(*) AS c FROM plausible_events_db.events_v2 WHERE site_id = 1 AND name = 'pageview' AND timestamp >= '${SINCE}' AND timestamp <= '${NOW}' GROUP BY pathname ORDER BY c DESC LIMIT 5 FORMAT TabSeparated")

# Top 5 referrers
TOP_REFS=$(query_db "SELECT referrer_source, count(*) AS c FROM plausible_events_db.events_v2 WHERE site_id = 1 AND name = 'pageview' AND timestamp >= '${SINCE}' AND timestamp <= '${NOW}' AND referrer_source != '' GROUP BY referrer_source ORDER BY c DESC LIMIT 5 FORMAT TabSeparated")

# Book a call visits
BOOK_VISITS=$(query_db "SELECT count(*) FROM plausible_events_db.events_v2 WHERE site_id = 1 AND name = 'pageview' AND pathname = '/book.html' AND timestamp >= '${SINCE}' AND timestamp <= '${NOW}'")

# Previous-week comparison for delta
PREV_SINCE=$(date -d '14 days ago' '+%Y-%m-%d %H:%M:%S')
PREV_UNTIL=$(date -d '7 days ago' '+%Y-%m-%d %H:%M:%S')
PREV_VISITORS=$(query_db "SELECT uniq(user_id) FROM plausible_events_db.events_v2 WHERE site_id = 1 AND name = 'pageview' AND timestamp >= '${PREV_SINCE}' AND timestamp < '${PREV_UNTIL}'")

# Delta
if [ "${PREV_VISITORS:-0}" -gt 0 ]; then
    DELTA_PCT=$(( (VISITORS - PREV_VISITORS) * 100 / PREV_VISITORS ))
    DELTA="${DELTA_PCT}%"
else
    DELTA="(no prior week)"
fi

# Format top pages
format_list() {
    awk -F'\t' 'NF==2 {printf "  • %s (%d)\n", $1, $2}'
}

TOP_PAGES_FMT=$(echo "$TOP_PAGES" | format_list)
TOP_REFS_FMT=$(echo "$TOP_REFS" | format_list)

[ -z "$TOP_PAGES_FMT" ] && TOP_PAGES_FMT="  (no data)"
[ -z "$TOP_REFS_FMT" ] && TOP_REFS_FMT="  (direct traffic only)"

# Compose message
MSG="📊 Weekly Analytics Digest — $(date '+%Y-%m-%d')

Last 7 days on aicloudstrategist.com:
• Unique visitors: ${VISITORS} (vs ${PREV_VISITORS} prior week, ${DELTA})
• Pageviews: ${PAGEVIEWS}
• Book-a-call visits: ${BOOK_VISITS}

Top pages:
${TOP_PAGES_FMT}

Top referrers:
${TOP_REFS_FMT}

Full dashboard: https://analytics.aicloudstrategist.com

Notes:
- Book-a-call visits are the closest leading indicator of pipeline
- LinkedIn referrers start appearing once outreach kicks in
- Google organic traffic takes 4-8 weeks post-launch to appear"

echo "[$(ts)] digest sent: visitors=${VISITORS}, book=${BOOK_VISITS}" >> "$LOG"

# Send
curl -s -X POST "https://api.telegram.org/bot${BOT}/sendMessage" \
    --data-urlencode "chat_id=$CHAT" \
    --data-urlencode "text=$MSG" > /dev/null

echo "done"
