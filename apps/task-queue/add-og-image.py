#!/usr/bin/env python3
"""
Adds og:image + twitter:image meta tags to each HTML page.
Idempotent: skips pages that already have og:image.
Maps page path to corresponding OG image filename.
"""
import pathlib, re, sys

WEB_ROOT = pathlib.Path("/var/www/aicloudstrategist")
OG_BASE = "https://aicloudstrategist.com/assets/og"

# Map each page to its OG image slug
MAP = {
    "index.html": "homepage",
    "services.html": "services",
    "proof.html": "proof",
    "compare.html": "compare",
    "book.html": "book",
    "blog.html": "blog",
    "faq.html": "faq",
    "privacy.html": "homepage",  # fallback
    "404.html": "homepage",  # fallback
    "aws-checklist.html": "aws-checklist",
    "azure-checklist.html": "azure-checklist",
    "ai-gpu-audit.html": "ai-gpu-audit",
    "finops-assessment.html": "finops-assessment",
    "devops-assessment.html": "devops-assessment",
    "one-pager.html": "one-pager",
    "blog/ri-coverage-under-30-percent.html": "blog-ri-coverage",
    "blog/orphaned-ebs-volumes.html": "blog-orphaned-ebs",
    "blog/cross-region-egress-mistake.html": "blog-cross-region",
    "blog/cost-per-1000-inferences.html": "blog-cp1ki",
    "blog/dora-metrics-for-cfo.html": "blog-dora-cfo",
    "blog/ri-coverage-india-governance.html": "blog-ri-india",
}

patched = 0
skipped = 0

for rel_path, slug in MAP.items():
    p = WEB_ROOT / rel_path
    if not p.exists():
        print(f"SKIP (missing): {rel_path}")
        continue

    s = p.read_text(encoding="utf-8")

    if "og:image" in s:
        skipped += 1
        continue

    og_image_url = f"{OG_BASE}/{slug}.png"
    inject = (
        f'<meta property="og:image" content="{og_image_url}">\n'
        f'<meta property="og:image:width" content="1200">\n'
        f'<meta property="og:image:height" content="630">\n'
        f'<meta name="twitter:image" content="{og_image_url}">\n'
    )

    # Inject before </head>
    new_s = s.replace("</head>", inject + "</head>", 1)
    if new_s == s:
        print(f"SKIP (no </head>): {rel_path}")
        continue

    p.write_text(new_s, encoding="utf-8")
    patched += 1
    print(f"OK: {rel_path} -> {slug}.png")

print(f"\nPatched: {patched} | Skipped (already had og:image): {skipped}")
