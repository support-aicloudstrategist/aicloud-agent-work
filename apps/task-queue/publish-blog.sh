#!/bin/bash
# Converts a blog draft markdown file to styled HTML + deploys to /var/www + regenerates feed + pings Telegram.
#
# Usage:
#   /docker/task-queue/bin/publish-blog.sh <slug> [pubdate-YYYY-MM-DD]
#
#   slug is the filename stem, e.g. "my-new-post" — the script expects:
#     source: /docker/task-queue/data/drafts/blog-<slug>.md
#            OR /data/work/aicloud-agent-work/drafts/blog-<slug>.md
#     output: /var/www/aicloudstrategist/blog/<slug>.html
#
# The draft markdown must start with a single H1 title line. Everything after
# the first H1 becomes the body. Other metadata (description, author, date) is
# inferred or passed as args.

set -euo pipefail

SLUG="${1:-}"
PUBDATE="${2:-$(date -I)}"

if [ -z "$SLUG" ]; then
    echo "Usage: $0 <slug> [YYYY-MM-DD]"
    echo "Example: $0 my-new-post 2026-05-27"
    exit 1
fi

# Find source draft
SRC=""
for candidate in \
    "/docker/task-queue/data/drafts/blog-${SLUG}.md" \
    "/data/work/aicloud-agent-work/drafts/blog-${SLUG}.md"; do
    if [ -f "$candidate" ]; then
        SRC="$candidate"
        break
    fi
done

if [ -z "$SRC" ]; then
    echo "ERROR: no draft found for slug '$SLUG'."
    echo "Searched:"
    echo "  /docker/task-queue/data/drafts/blog-${SLUG}.md"
    echo "  /data/work/aicloud-agent-work/drafts/blog-${SLUG}.md"
    exit 1
fi

echo "Using source: $SRC"

OUT="/var/www/aicloudstrategist/blog/${SLUG}.html"

# Extract title (first # line)
TITLE=$(grep -m1 -E '^# ' "$SRC" | sed 's|^# ||')
if [ -z "$TITLE" ]; then
    echo "ERROR: no H1 title found in $SRC"
    exit 1
fi

# First meaningful paragraph after title = description (first 200 chars)
DESC=$(awk '/^# / {started=1; next} started && /^[A-Za-z0-9*"]/ {print; exit}' "$SRC" | sed 's|^\*||; s|\*$||' | head -c 240)
DESC_CLEAN=$(echo "$DESC" | sed -e 's|"|\&quot;|g' -e 's|&|\&amp;|g' | head -c 240)

AUTHOR="Anushka B"

# Word count → estimate read time
WC=$(wc -w < "$SRC")
READ_MIN=$(( WC / 200 ))
[ "$READ_MIN" -lt 2 ] && READ_MIN=2

# Human-readable date
DATE_HUMAN=$(date -d "$PUBDATE" "+%-d %B %Y")

# Convert markdown body to HTML (pandoc in claude-mao container)
BODY_HTML=$(mktemp)
SRC_IN_MAO="/tmp/publish-blog-src-$$.md"
BODY_IN_MAO="/tmp/publish-blog-body-$$.html"
docker cp "$SRC" "claude-mao:${SRC_IN_MAO}"
# Skip the first H1 (we use our own header block) and pipe through pandoc inside container
docker exec claude-mao bash -c "tail -n +2 '${SRC_IN_MAO}' | pandoc -f markdown -t html5 --no-highlight > '${BODY_IN_MAO}'"
docker cp "claude-mao:${BODY_IN_MAO}" "$BODY_HTML"
docker exec claude-mao rm -f "${SRC_IN_MAO}" "${BODY_IN_MAO}"

# Build the final HTML file
cat > "$OUT" <<HEAD
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${TITLE} — AICloudStrategist</title>
<meta name="description" content="${DESC_CLEAN}">
<link rel="stylesheet" href="/assets/style.css">
<link rel="canonical" href="https://aicloudstrategist.com/blog/${SLUG}.html">
<meta property="og:type" content="article">
<meta property="og:url" content="https://aicloudstrategist.com/blog/${SLUG}.html">
<meta property="og:title" content="${TITLE}">
<meta property="og:description" content="${DESC_CLEAN}">
<meta property="og:site_name" content="AICloudStrategist">
<meta property="article:published_time" content="${PUBDATE}">
<meta property="article:author" content="${AUTHOR}">
<script defer data-domain="aicloudstrategist.com" src="https://analytics.aicloudstrategist.com/js/script.outbound-links.js"></script>
<link rel="alternate" type="application/rss+xml" title="AICloudStrategist Writing" href="/feed.xml">
</head>
<body>
<header class="nav">
  <a class="brand" href="/">AICloudStrategist</a>
  <nav>
    <a href="/services.html">Services</a>
    <a href="/proof.html">Proof</a>
    <a href="/compare.html">Compare</a>
    <a href="/blog.html">Writing</a>
    <a href="/book.html">Book a call</a>
  </nav>
</header>

<main>
<article class="blog-post">

<header class="blog-header">
  <p class="lede small"><a href="/blog.html">← All writing</a></p>
  <h1>${TITLE}</h1>
  <p class="lede small">By ${AUTHOR} · Published ${DATE_HUMAN} · ${READ_MIN} min read</p>
</header>

HEAD

cat "$BODY_HTML" >> "$OUT"

cat >> "$OUT" <<TAIL

<hr>

<p class="lede small"><em>AICloudStrategist · Founder-led. Enterprise-reviewed. · Written by ${AUTHOR}, Founder.</em></p>

</article>

<section class="cta-band">
  <p>More writing every Tuesday and Thursday.</p>
  <a class="cta" href="/blog.html">See all writing →</a>
</section>

<footer>
  <p>AICloudStrategist · Rohini, Delhi 110085 · <a href="mailto:support@aicloudstrategist.com">support@aicloudstrategist.com</a></p>
  <p class="legal"><a href="/privacy.html">Privacy</a> · <a href="/services.html">Services</a> · <a href="/proof.html">Proof</a> · <a href="/compare.html">Compare</a> · <a href="/blog.html">Writing</a> · <a href="/faq.html">FAQ</a></p>
</footer>
</main>
</body>
</html>
TAIL

rm -f "$BODY_HTML"
chmod 644 "$OUT"

# Regenerate feed
/docker/task-queue/bin/regen-feed.sh

# Ping Telegram
BOT=$(grep '^BOT_TOKEN=' /docker/tg-bot/.env | cut -d= -f2-)
CHAT=-4955349765
MSG="blog post published ✓

${TITLE}

https://aicloudstrategist.com/blog/${SLUG}.html

Published ${DATE_HUMAN}. RSS feed regenerated. ${WC} words, ~${READ_MIN} min read.

next: update blog.html hub + commit + push + post on LinkedIn when ready."

curl -s -X POST "https://api.telegram.org/bot${BOT}/sendMessage" \
    --data-urlencode "chat_id=$CHAT" \
    --data-urlencode "text=$MSG" > /dev/null

echo "Published: https://aicloudstrategist.com/blog/${SLUG}.html"
echo "Title: $TITLE"
echo "Words: $WC | Read time: ${READ_MIN} min"
echo "Feed regenerated."
