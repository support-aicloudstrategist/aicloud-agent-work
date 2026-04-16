#!/bin/bash
# Scans /var/www/aicloudstrategist/blog/ for published HTML posts and regenerates feed.xml.
# Extracts title, description, pubDate, author from OG/article meta tags.
# Idempotent. Safe to run multiple times.
#
# Typical use:
#   - Run manually after publishing a new blog post
#   - Or add to cron: 0 11 * * * /docker/task-queue/bin/regen-feed.sh

set -euo pipefail

BLOG_DIR=/var/www/aicloudstrategist/blog
OUT=/var/www/aicloudstrategist/feed.xml
TMP=$(mktemp)

# Extract metadata from a single blog HTML file
# stdout: title|description|url|pubDate|author (pipe-separated)
extract_meta() {
    local f="$1"
    local base
    base=$(basename "$f")
    local url="https://aicloudstrategist.com/blog/$base"

    local title
    title=$(grep -oE '<meta property="og:title" content="[^"]+"' "$f" | head -1 | sed 's|<meta property="og:title" content="||; s|"$||')

    local desc
    desc=$(grep -oE '<meta property="og:description" content="[^"]+"' "$f" | head -1 | sed 's|<meta property="og:description" content="||; s|"$||')

    local pubdate
    pubdate=$(grep -oE '<meta property="article:published_time" content="[^"]+"' "$f" | head -1 | sed 's|<meta property="article:published_time" content="||; s|"$||')

    local author
    author=$(grep -oE '<meta property="article:author" content="[^"]+"' "$f" | head -1 | sed 's|<meta property="article:author" content="||; s|"$||')

    # Default values
    [ -z "$title" ] && title=$(grep -oE '<title>[^<]+</title>' "$f" | head -1 | sed 's|<title>||; s|</title>||; s| — AICloudStrategist||')
    [ -z "$desc" ] && desc="(no description)"
    [ -z "$pubdate" ] && pubdate=$(date -I)
    [ -z "$author" ] && author="Anushka B"

    printf '%s\t%s\t%s\t%s\t%s\n' "$title" "$desc" "$url" "$pubdate" "$author"
}

# Convert YYYY-MM-DD to RFC822 (for RSS pubDate)
to_rfc822() {
    local d="$1"
    date -d "$d 10:00:00 +0530" -R 2>/dev/null || echo "Wed, 01 Jan 2026 10:00:00 +0530"
}

# XML escape (basic)
xml_escape() {
    sed -e 's|&|\&amp;|g' -e 's|<|\&lt;|g' -e 's|>|\&gt;|g' -e 's|"|\&quot;|g' -e "s|'|\\&apos;|g"
}

# Collect metadata for all blog posts, sorted by pubdate descending
META_FILE=$(mktemp)
for f in "$BLOG_DIR"/*.html; do
    [ -f "$f" ] || continue
    extract_meta "$f" >> "$META_FILE"
done

# Sort by pubdate (column 4), descending (newest first)
sort -t$'\t' -k4,4r "$META_FILE" > "${META_FILE}.sorted"
mv "${META_FILE}.sorted" "$META_FILE"

# Build feed.xml
{
cat <<'HEADER'
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
  <title>AICloudStrategist — Writing</title>
  <link>https://aicloudstrategist.com/blog.html</link>
  <atom:link href="https://aicloudstrategist.com/feed.xml" rel="self" type="application/rss+xml" />
  <description>Practitioner writing on FinOps, cloud architecture, AI infrastructure, and DevOps for Indian engineering leaders and CFOs. Founder-led. Enterprise-reviewed.</description>
  <language>en-IN</language>
  <copyright>Copyright 2026 AICloudStrategist</copyright>
  <managingEditor>support@aicloudstrategist.com (Anushka B)</managingEditor>
  <webMaster>support@aicloudstrategist.com (Anushka B)</webMaster>
HEADER

    # Build lastBuildDate from newest post
    NEWEST=$(head -1 "$META_FILE" | cut -f4)
    printf '  <lastBuildDate>%s</lastBuildDate>\n' "$(to_rfc822 "$NEWEST")"
    cat <<'MID'
  <category>Cloud Computing</category>
  <category>FinOps</category>
  <category>DevOps</category>
  <category>AI Infrastructure</category>
  <generator>regen-feed.sh</generator>

MID

    # Items
    while IFS=$'\t' read -r title desc url pubdate author; do
        [ -z "$title" ] && continue
        title_esc=$(echo "$title" | xml_escape)
        desc_esc=$(echo "$desc" | xml_escape)
        pub_rfc=$(to_rfc822 "$pubdate")
        author_esc=$(echo "$author" | xml_escape)
        cat <<ITEM

  <item>
    <title>${title_esc}</title>
    <link>${url}</link>
    <guid isPermaLink="true">${url}</guid>
    <pubDate>${pub_rfc}</pubDate>
    <dc:creator>${author_esc}</dc:creator>
    <description>${desc_esc}</description>
  </item>
ITEM
    done < "$META_FILE"

cat <<'FOOTER'

</channel>
</rss>
FOOTER
} > "$TMP"

# Atomic install
mv "$TMP" "$OUT"
chmod 644 "$OUT"
rm -f "$META_FILE"

echo "feed.xml regenerated with $(grep -c '<item>' "$OUT") items."
