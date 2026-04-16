#!/bin/bash
# Regenerates /var/www/aicloudstrategist/sitemap.xml by scanning the actual
# HTML files present. Adds lastmod from filesystem mtime.
# Idempotent. Safe to run on cron or manually after publishing new pages.

set -euo pipefail

WEB=/var/www/aicloudstrategist
OUT=$WEB/sitemap.xml
BASE=https://aicloudstrategist.com
TMP=$(mktemp)

priority() {
    local path="$1"
    case "$path" in
        "") echo "1.0" ;;
        services.html) echo "0.9" ;;
        proof.html|blog.html|book.html) echo "0.9" ;;
        first-customer.html) echo "0.8" ;;
        compare.html|faq.html) echo "0.7" ;;
        blog/*) echo "0.7" ;;
        author/*) echo "0.6" ;;
        privacy.html) echo "0.4" ;;
        *) echo "0.6" ;;
    esac
}

changefreq() {
    local path="$1"
    case "$path" in
        ""|services.html|proof.html|blog.html) echo "weekly" ;;
        blog/*) echo "monthly" ;;
        book.html|first-customer.html) echo "monthly" ;;
        author/*) echo "monthly" ;;
        privacy.html) echo "yearly" ;;
        *) echo "monthly" ;;
    esac
}

{
    echo '<?xml version="1.0" encoding="UTF-8"?>'
    echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    ROOT_LASTMOD=$(date -r "$WEB/index.html" +%Y-%m-%d)
    echo "  <url><loc>${BASE}/</loc><priority>1.0</priority><changefreq>weekly</changefreq><lastmod>${ROOT_LASTMOD}</lastmod></url>"

    for f in "$WEB"/*.html; do
        [ -f "$f" ] || continue
        base=$(basename "$f")
        [ "$base" = "index.html" ] && continue
        [ "$base" = "404.html" ] && continue
        path="$base"
        p=$(priority "$path")
        cf=$(changefreq "$path")
        lm=$(date -r "$f" +%Y-%m-%d)
        echo "  <url><loc>${BASE}/${path}</loc><priority>${p}</priority><changefreq>${cf}</changefreq><lastmod>${lm}</lastmod></url>"
    done

    for f in "$WEB"/blog/*.html; do
        [ -f "$f" ] || continue
        base=$(basename "$f")
        path="blog/$base"
        p=$(priority "$path")
        cf=$(changefreq "$path")
        lm=$(date -r "$f" +%Y-%m-%d)
        echo "  <url><loc>${BASE}/${path}</loc><priority>${p}</priority><changefreq>${cf}</changefreq><lastmod>${lm}</lastmod></url>"
    done

    for f in "$WEB"/author/*.html; do
        [ -f "$f" ] || continue
        base=$(basename "$f")
        path="author/$base"
        p=$(priority "$path")
        cf=$(changefreq "$path")
        lm=$(date -r "$f" +%Y-%m-%d)
        echo "  <url><loc>${BASE}/${path}</loc><priority>${p}</priority><changefreq>${cf}</changefreq><lastmod>${lm}</lastmod></url>"
    done

    for f in "$WEB"/downloads/*.pdf; do
        [ -f "$f" ] || continue
        base=$(basename "$f")
        lm=$(date -r "$f" +%Y-%m-%d)
        echo "  <url><loc>${BASE}/downloads/${base}</loc><priority>0.7</priority><changefreq>monthly</changefreq><lastmod>${lm}</lastmod></url>"
    done

    echo '</urlset>'
} > "$TMP"

mv "$TMP" "$OUT"
chmod 644 "$OUT"

URL_COUNT=$(grep -c '<url>' "$OUT")
echo "sitemap.xml regenerated with ${URL_COUNT} URLs."
