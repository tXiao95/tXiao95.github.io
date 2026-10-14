"""Generate navigation and content includes. Uses only the Python standard library."""
from pathlib import Path
from html import escape
from itertools import groupby
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_generated"
OUT.mkdir(exist_ok=True)

def write(name, value):
    (OUT / name).write_text(value + "\n", encoding="utf-8")

def link(url, text):
    if not url.startswith(("https://", "/", "#")) and not re.match(r"[a-z0-9-]+\.html(?:#.*)?$", url):
        raise ValueError(f"Unsupported URL: {url}")
    return f'<a href="{escape(url, quote=True)}">{escape(text)}</a>'

nav = [("home", "index.html", "Home"), ("research", "research.html", "Research"),
       ("publications", "publications.html", "Publications"),
       ("teaching", "teaching.html", "Teaching"), ("cv", "cv.html", "CV"),
       ("contact", "contact.html", "Contact")]
for current in [row[0] for row in nav] + ["404"]:
    links = []
    for key, href, label in nav:
        active = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="/{href}"{active}>{escape(label)}</a>')
    write(f"header-{current}.html",
          '<a class="skip-link" href="#quarto-document-content">Skip to content</a>'
          '<header class="site-header"><a class="wordmark" href="/">Thomas Hsiao</a>'
          '<nav class="site-nav" aria-label="Main navigation">' + "".join(links) + '</nav></header>')

pubs = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
seen = set()
for p in pubs:
    for key in ("id", "type", "year", "authors", "title", "venue"):
        if not p.get(key):
            raise ValueError(f"Missing {key} in publication: {p}")
    if not re.fullmatch(r"[a-z0-9-]+", p["id"]) or p["id"] in seen:
        raise ValueError(f"Invalid or duplicate publication ID: {p['id']}")
    seen.add(p["id"])
    if p["type"] not in ("peer-reviewed", "preprint", "manuscript"):
        raise ValueError(f"Unknown publication type: {p['type']}")
    if not isinstance(p["year"], int):
        raise ValueError("Publication year must be an integer")
    if p.get("doi") and not re.fullmatch(r"10\.\d{4,9}/\S+", p["doi"]):
        raise ValueError(f"Invalid DOI: {p['doi']}")

def author_html(p):
    return re.sub(r"\bHsiao T(?:W)?\b", r"<strong>\g<0></strong>", escape(p["authors"]))

def primary_url(p):
    return ("https://arxiv.org/abs/" + p["arxiv"] if p.get("arxiv") else
            "https://doi.org/" + p["doi"] if p.get("doi") else p.get("url"))

def pub_links(p):
    links = []
    if p.get("doi"): links.append(link("https://doi.org/" + p["doi"], "DOI"))
    if p.get("arxiv"): links.append(link("https://arxiv.org/abs/" + p["arxiv"], "arXiv"))
    if p.get("url"): links.append(link(p["url"], "Article"))
    if p.get("code"): links.append(link(p["code"], "Code"))
    return '<p class="pub-links">' + "".join(links) + "</p>" if links else ""

sections = []
for kind, anchor, label in [("peer-reviewed", "peer-reviewed", "Peer-reviewed publications"),
                             ("preprint", "preprints", "Preprints"), ("manuscript", "manuscripts", "Manuscripts")]:
    subset = sorted((p for p in pubs if p["type"] == kind), key=lambda p: (p["year"], p.get("sort_date", "")), reverse=True)
    if not subset: continue
    section = [f'<section class="publications-section" aria-labelledby="{anchor}"><h2 id="{anchor}">{label}</h2>']
    for year, entries in groupby(subset, key=lambda p: p["year"]):
        section.append(f'<div class="publication-year"><h3>{year}</h3><ol class="publication-list">')
        for p in entries:
            title = link(primary_url(p), p["title"]) if primary_url(p) else escape(p["title"])
            note = p.get("note", "")
            note_html = (link(p["note_url"], note) if p.get("note_url") else escape(note))
            section.append(f'<li class="publication" id="{p["id"]}"><h4>{title}</h4>'
                           f'<p class="pub-authors">{author_html(p)}</p>'
                           f'<p class="pub-venue"><em>{escape(p["venue"])}</em> · {escape(str(p.get("year_label", year)))}</p>'
                           + pub_links(p) + (f'<p class="pub-note">{note_html}</p>' if note else "") + '</li>')
        section.append("</ol></div>")
    sections.append("".join(section) + "</section>")
write("publications.html", "\n".join(sections))

featured = []
for p in sorted((p for p in pubs if p.get("featured")), key=lambda p: p["featured"]):
    label = "Preprint" if p["type"] == "preprint" else "Peer-reviewed"
    featured.append(f'<article class="featured-item"><p class="pub-meta">{p["year"]} · {label}</p>'
                    f'<h3>{link("publications.html#" + p["id"], p["title"])}</h3>'
                    f'<p class="pub-authors">{author_html(p)}</p>' + pub_links(p) + '</article>')
write("featured.html", '<div class="featured-list">' + "".join(featured) + '</div>')

news = json.loads((ROOT / "data/news.json").read_text(encoding="utf-8"))
items = []
for n in sorted(news, key=lambda n: n["date"], reverse=True):
    text = link(n["url"], n["text"]) if n.get("url") else escape(n["text"])
    # HTML datetime accepts a year-month or full date, not a year alone.
    date_attr = f' datetime="{escape(n["date"])}"' if len(n["date"]) > 4 else ""
    items.append(f'<li><time{date_attr}>{escape(n["label"])}</time><span>{text}</span></li>')
write("news.html", '<ul class="news-list">' + "".join(items) + '</ul>')

portrait = next((ROOT / "assets" / f"portrait.{ext}" for ext in ("webp", "jpg", "png")
                 if (ROOT / "assets" / f"portrait.{ext}").is_file()), None)
write("portrait.html", f'<img class="portrait" src="assets/{portrait.name}" alt="Thomas Hsiao" width="245" height="306">' if portrait else "<!-- Add assets/portrait.jpg or portrait.webp when available. -->")
print(f"Prepared {len(pubs)} publications, {len(news)} highlights, and navigation.")
