#!/usr/bin/env python3
"""
Injects JSON-LD schema into AICloudStrategist pages.

Strategy:
- Blog posts: BlogPosting schema (headline, datePublished, author, publisher, image, url, wordCount, description)
- Blog index (blog.html): Blog + ItemList of all posts
- Homepage (index.html): WebSite schema (with SearchAction if supported) — added alongside existing ProfessionalService

Idempotent: skips pages already containing 'BlogPosting' / 'ItemList' / 'WebSite' markers.
Reads metadata from existing <title>, og:description, og:image, article:published_time tags.
"""
import pathlib, re, json, sys, html as _html

WEB_ROOT = pathlib.Path("/var/www/aicloudstrategist")
BASE = "https://aicloudstrategist.com"
AUTHOR = "Anushka B"
PUBLISHER = "AICloudStrategist"
PUBLISHER_LOGO = f"{BASE}/assets/og/logo-512.jpg"


def read(p: pathlib.Path) -> str:
    return p.read_text(encoding="utf-8")


def write(p: pathlib.Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def meta(html: str, prop: str, attr: str = "property") -> str | None:
    m = re.search(
        rf'<meta\s+{attr}=["\']{re.escape(prop)}["\']\s+content=["\']([^"\']*)["\']',
        html,
    )
    return _html.unescape(m.group(1)) if m else None


def title(html: str) -> str | None:
    m = re.search(r"<title>([^<]+)</title>", html)
    if not m:
        return None
    t = m.group(1).strip()
    # Strip " — AICloudStrategist" suffix
    return re.sub(r"\s*[—–-]\s*AICloudStrategist\s*$", "", t).strip()


def word_count(html: str) -> int:
    body = re.search(r"<article[^>]*>(.*?)</article>", html, re.S)
    if not body:
        return 0
    text = re.sub(r"<[^>]+>", " ", body.group(1))
    return len(re.findall(r"\b\w+\b", text))


def inject_before_head_close(html: str, block: str) -> str:
    return html.replace("</head>", f"{block}\n</head>", 1)


def blog_posting_schema(path: pathlib.Path) -> dict | None:
    html = read(path)
    if "BlogPosting" in html:
        return None

    rel = path.relative_to(WEB_ROOT).as_posix()
    url = f"{BASE}/{rel}"
    headline = meta(html, "og:title") or title(html)
    description = meta(html, "og:description") or meta(html, "description", "name") or ""
    date_pub = meta(html, "article:published_time")
    image = meta(html, "og:image") or f"{BASE}/assets/og/blog.jpg"
    wc = word_count(html)

    if not (headline and date_pub):
        print(f"  SKIP {rel}: missing headline or date", file=sys.stderr)
        return None

    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "description": description,
        "datePublished": date_pub,
        "dateModified": date_pub,
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{BASE}/"},
        "publisher": {
            "@type": "Organization",
            "name": PUBLISHER,
            "logo": {"@type": "ImageObject", "url": PUBLISHER_LOGO},
        },
        "image": image,
        "url": url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "inLanguage": "en-IN",
    }
    if wc > 0:
        schema["wordCount"] = wc
    return schema


def update_post(path: pathlib.Path) -> bool:
    html = read(path)
    schema = blog_posting_schema(path)
    if not schema:
        return False
    block = (
        '<script type="application/ld+json">\n'
        + json.dumps(schema, ensure_ascii=False, indent=2)
        + "\n</script>"
    )
    new = inject_before_head_close(html, block)
    write(path, new)
    return True


def collect_blog_posts() -> list[pathlib.Path]:
    return sorted((WEB_ROOT / "blog").glob("*.html"))


def blog_hub_schema() -> dict:
    posts = []
    for p in collect_blog_posts():
        html = read(p)
        rel = p.relative_to(WEB_ROOT).as_posix()
        url = f"{BASE}/{rel}"
        headline = meta(html, "og:title") or title(html) or p.stem
        date_pub = meta(html, "article:published_time") or ""
        posts.append((date_pub, headline, url))

    # Newest first
    posts.sort(key=lambda x: x[0], reverse=True)

    item_list = [
        {
            "@type": "ListItem",
            "position": i + 1,
            "url": url,
            "name": headline,
        }
        for i, (_, headline, url) in enumerate(posts)
    ]

    return {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "AICloudStrategist — Writing",
        "description": "Practitioner writing on FinOps, cloud architecture, AI infrastructure, and DevOps for Indian engineering leaders and CFOs.",
        "url": f"{BASE}/blog.html",
        "publisher": {
            "@type": "Organization",
            "name": PUBLISHER,
            "logo": {"@type": "ImageObject", "url": PUBLISHER_LOGO},
        },
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{BASE}/"},
        "inLanguage": "en-IN",
        "mainEntity": {
            "@type": "ItemList",
            "itemListOrder": "Descending",
            "numberOfItems": len(item_list),
            "itemListElement": item_list,
        },
    }


def update_blog_hub() -> bool:
    p = WEB_ROOT / "blog.html"
    html = read(p)
    if '"@type": "Blog"' in html or '"@type":"Blog"' in html:
        return False
    schema = blog_hub_schema()
    block = (
        '<script type="application/ld+json">\n'
        + json.dumps(schema, ensure_ascii=False, indent=2)
        + "\n</script>"
    )
    write(p, inject_before_head_close(html, block))
    return True


def website_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": PUBLISHER,
        "alternateName": "AICloudStrategist.com",
        "url": f"{BASE}/",
        "publisher": {
            "@type": "Organization",
            "name": PUBLISHER,
            "logo": {"@type": "ImageObject", "url": PUBLISHER_LOGO},
        },
        "inLanguage": "en-IN",
    }


def update_homepage() -> bool:
    p = WEB_ROOT / "index.html"
    html = read(p)
    if '"@type": "WebSite"' in html or '"@type":"WebSite"' in html:
        return False
    block = (
        '<script type="application/ld+json">\n'
        + json.dumps(website_schema(), ensure_ascii=False, indent=2)
        + "\n</script>"
    )
    write(p, inject_before_head_close(html, block))
    return True


def main():
    updated = []
    for p in collect_blog_posts():
        if update_post(p):
            updated.append(p.relative_to(WEB_ROOT).as_posix())

    if update_blog_hub():
        updated.append("blog.html")
    if update_homepage():
        updated.append("index.html")

    if updated:
        print(f"Injected JSON-LD on {len(updated)} page(s):")
        for u in updated:
            print(f"  + {u}")
    else:
        print("No changes — all pages already have schema.")


if __name__ == "__main__":
    main()
