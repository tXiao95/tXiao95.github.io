"""Add canonical metadata and deployment-specific resources."""
from pathlib import Path
from html import escape, unescape
import os
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "_site"
(out / ".nojekyll").touch()
domain_active = "domain" in os.environ.get("QUARTO_PROFILE", "").split(",")
base = "https://www.twhsiao.com" if domain_active else "https://txiao95.github.io"
for page in out.glob("*.html"):
    text = page.read_text(encoding="utf-8")
    # Make every browser/search title identifiable without duplicating the home title.
    title_match = re.search(r"<title>(.*?)</title>", text, flags=re.S)
    if title_match:
        title = unescape(title_match.group(1))
        if "Thomas Hsiao" not in title:
            title += " | Thomas Hsiao"
        text = re.sub(r"<title>.*?</title>", f"<title>{escape(title)}</title>", text, flags=re.S)
        text = re.sub(r'<meta property="og:title"[^>]*>',
                      f'<meta property="og:title" content="{escape(title)}">', text)
    # Keep the 404 functional even when served for a nested, missing URL.
    if page.name == "404.html":
        text = text.replace('href="./', 'href="/')
    canonical = base + ("/" if page.name == "index.html" else "/" + page.name)
    tags = (f'<link rel="canonical" href="{escape(canonical)}">\n'
            f'<meta property="og:url" content="{escape(canonical)}">\n')
    if page.name == "404.html":
        tags += '<meta name="robots" content="noindex">\n'
    text = re.sub(r'<link rel="canonical"[^>]*>\s*', "", text)
    text = re.sub(r'<meta property="og:url"[^>]*>\s*', "", text)
    page.write_text(text.replace("</head>", tags + "</head>"), encoding="utf-8")
if domain_active:
    shutil.copyfile(ROOT / "CNAME", out / "CNAME")
else:
    (out / "CNAME").unlink(missing_ok=True)
print("Custom domain active." if domain_active else "Using the GitHub Pages address.")
