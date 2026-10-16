"""Check rendered navigation, anchors, metadata, PDF integrity, and content counts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.errors = set(), [], []
        self.h1 = self.main = self.active = 0
        self.description = self.canonical = self.title = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            if a["id"] in self.ids: self.errors.append("duplicate id: " + a["id"])
            self.ids.add(a["id"])
        self.h1 += tag == "h1"
        self.main += tag == "main"
        self.active += a.get("aria-current") == "page"
        self.title |= tag == "title"
        self.description |= tag == "meta" and a.get("name") == "description" and bool(a.get("content"))
        self.canonical |= tag == "link" and a.get("rel") == "canonical"
        for attr in ("href", "src", "data"):
            if a.get(attr): self.links.append(a[attr])
        if tag == "img" and "alt" not in a: self.errors.append("image missing alt text")
        if tag == "script": self.errors.append("Unexpected JavaScript on this static site")

pages = {p: Page(p.read_text(encoding="utf-8")) for p in SITE.rglob("*.html")}
errors = []
if (SITE / "tmp").exists(): errors.append("Temporary audit files leaked into published output")
for path, page in pages.items():
    errors += [f"{path.name}: {e}" for e in page.errors]
    for ok, message in [(page.h1 == 1, "expected one h1"), (page.main == 1, "expected main landmark"),
                        (page.title and page.description and page.canonical, "missing SEO metadata"),
                        (page.active == (0 if path.name == "404.html" else 1), "active navigation incorrect")]:
        if not ok: errors.append(f"{path.name}: {message}")
    for href in page.links:
        u = urlsplit(href)
        if u.scheme or u.netloc: continue
        target = (SITE / unquote(u.path.lstrip("/")) if u.path.startswith("/") else path.parent / unquote(u.path)) if u.path else path
        if target.is_dir(): target /= "index.html"
        if not target.is_file():
            errors.append(f"{path.name}: missing {href}")
        elif u.fragment and target.suffix == ".html":
            other = pages.get(target) or Page(target.read_text(encoding="utf-8"))
            if unquote(u.fragment) not in other.ids:
                errors.append(f"{path.name}: missing anchor {href}")
expected_pages = {"index.html", "publications.html", "teaching.html", "contact.html", "404.html"}
if {p.relative_to(SITE).as_posix() for p in pages} != expected_pages:
    errors.append("Published pages differ from the approved public page list")
for private_path in ("_internal", "docs", "README.md", "research.html"):
    if (SITE / private_path).exists(): errors.append(f"Internal content leaked into output: {private_path}")
pdf = SITE / "cv.pdf"
if not pdf.is_file() or not pdf.read_bytes().startswith(b"%PDF-"):
    errors.append("Missing or invalid published CV")
elif hashlib.sha256(pdf.read_bytes()).digest() != hashlib.sha256((ROOT / "cv.pdf").read_bytes()).digest():
    errors.append("Published CV differs from source")
pubs = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
pub_ids = pages[SITE / "publications.html"].ids
for p in pubs:
    if p["id"] not in pub_ids: errors.append(f"Missing publication: {p['id']}")
if not (SITE / "sitemap.xml").exists(): errors.append("Missing sitemap")
elif "research.html" in (SITE / "sitemap.xml").read_text(encoding="utf-8"):
    errors.append("Hidden research page remains in sitemap")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(pages)} pages; all local links and anchors; {len(pubs)} publications; identical CV PDF; accessible landmarks; SEO metadata; no JavaScript.")
