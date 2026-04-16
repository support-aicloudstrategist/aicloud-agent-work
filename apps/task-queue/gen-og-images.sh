#!/bin/bash
# Generates OG preview images (1200x630 PNG) for each key landing page.
# Uses wkhtmltoimage inside claude-mao container.
# Output: /var/www/aicloudstrategist/assets/og/<slug>.png

set -euo pipefail

TEMPLATE_SRC="/var/www/aicloudstrategist/assets/og/og-template.html"
OUT_DIR="/var/www/aicloudstrategist/assets/og"

if [ ! -f "$TEMPLATE_SRC" ]; then
    echo "ERROR: $TEMPLATE_SRC not found. Deploy the template first."
    exit 1
fi

mkdir -p "$OUT_DIR"

# Generate a single OG image
# Args: slug headline font_size
render() {
    local slug="$1"
    local headline="$2"
    local font_size="${3:-56}"

    local tmp_html="/tmp/og-${slug}-$$.html"
    local tmp_png="/tmp/og-${slug}-$$.png"

    # Fill template
    sed "s|{{HEADLINE}}|${headline}|; s|{{FONT_SIZE}}|${font_size}|" "$TEMPLATE_SRC" > "$tmp_html"

    # Render via mao container (root-exec for cleanup since docker cp makes files root-owned)
    docker cp "$tmp_html" "claude-mao:${tmp_html}"
    docker exec -u root claude-mao chown mao:mao "$tmp_html" 2>/dev/null || true
    docker exec claude-mao wkhtmltoimage -q --width 1200 --height 630 --quality 92 --format png "$tmp_html" "$tmp_png" 2>/dev/null || true
    docker cp "claude-mao:${tmp_png}" "${OUT_DIR}/${slug}.png"
    docker exec -u root claude-mao rm -f "$tmp_html" "$tmp_png"
    rm -f "$tmp_html"

    if [ -f "${OUT_DIR}/${slug}.png" ]; then
        size=$(stat -c%s "${OUT_DIR}/${slug}.png")
        echo "  ${slug}.png (${size} bytes)"
    else
        echo "  ${slug}.png FAILED"
    fi
}

echo "Generating OG images..."

# Homepage + core pages
render "homepage" "Cut your cloud bill 20-30% in four weeks." 64
render "services" "Nine services. Fixed-price. Founder-led." 60
render "proof" "Pattern studies from mid-market Indian cloud engagements." 54
render "compare" "Honest comparison vs Big-4, freelance, and in-house." 52
render "book" "Free 30-min Cloud Cost Health Check. Same-day summary." 52
render "blog" "Practitioner writing on cloud cost, architecture, AI, DevOps." 52
render "faq" "The questions CTOs and CFOs actually ask." 60

# Lead-magnet wrappers
render "aws-checklist" "30 AWS cost leak points. The checklist." 58
render "azure-checklist" "30 Azure cost leak points. The checklist." 58
render "ai-gpu-audit" "22 AI / GPU cost leak points. The audit checklist." 54
render "finops-assessment" "Where does your FinOps practice sit? 10-question diagnostic." 50
render "devops-assessment" "DORA-based DevOps maturity self-assessment. 12 questions." 52
render "one-pager" "Nine services. One page. INR pricing. Timelines." 58

# Blog posts
render "blog-ri-coverage" "Your Reserved Instance coverage is probably under 30%." 52
render "blog-orphaned-ebs" "Orphaned EBS volumes: the quiet compounding cost." 50
render "blog-cross-region" "The cross-region egress mistake that tripled a GCP bill." 50
render "blog-cp1ki" "Cost-per-1000-inferences: the one number every AI team needs." 48
render "blog-dora-cfo" "DORA metrics for the CFO: translating DevOps to business outcomes." 46
render "blog-ri-india" "Why 70% of Indian mid-market cloud accounts have RI coverage below 30%." 42

echo ""
echo "Done. Images in $OUT_DIR/"
ls -la "$OUT_DIR"/*.png 2>/dev/null | wc -l
