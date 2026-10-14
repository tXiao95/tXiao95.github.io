# Thomas Hsiao — academic website

A Quarto academic website with Markdown pages, structured publication and news data, a custom HTML template, and a custom responsive stylesheet. The published site uses no JavaScript, external fonts, analytics, or database.

- Website: [www.twhsiao.com](https://www.twhsiao.com/)
- Repository: [tXiao95/tXiao95.github.io](https://github.com/tXiao95/tXiao95.github.io)
- Permanent CV: [www.twhsiao.com/cv.pdf](https://www.twhsiao.com/cv.pdf)
- Original GitHub Pages address: [txiao95.github.io](https://txiao95.github.io/)

Cloudflare manages domain registration and DNS; GitHub Pages hosts the website. See the [domain guide](docs/DOMAIN.md) for configuration and verification.

## Everyday updates

Routine updates can be made in GitHub's browser interface. Open a file, select its pencil icon, edit, and select **Commit changes**. Commits to `main` automatically build and deploy. For larger edits, create a branch and pull request to check the build before merging.

| Change | File |
| --- | --- |
| Biography and research interests | `index.qmd` |
| Research descriptions and related papers | `research.qmd` |
| Publication details and links | `data/publications.json` |
| Teaching and course experience | `teaching.qmd` |
| Saved news, awards, and presentations (currently hidden) | `data/news.json` |
| Email and professional links | `contact.qmd` |
| Compiled CV | `cv.pdf` |
| Photograph | Add `assets/portrait.jpg`, `.webp`, or `.png` |
| Colors, typography, and spacing | `assets/styles.css` |

Keep the page descriptions in the YAML blocks at the top of `.qmd` files accurate: they supply search and sharing metadata. Content updates do not require CSS changes.

### Replace the CV

**Overleaf remains the source of truth.** The website serves the compiled PDF without recreating the CV in HTML.

1. Edit and compile in Overleaf, then download the PDF.
2. Rename the downloaded file exactly `cv.pdf` (lowercase).
3. Open the [repository root](https://github.com/tXiao95/tXiao95.github.io) on the `main` branch.
4. Select **Add file → Upload files** and drag in `cv.pdf`. Upload it at the root, alongside `_quarto.yml`; the matching filename replaces the existing PDF.
5. Enter a message such as `Update CV, October 2026` and commit directly to `main`. If branch protection requires a pull request, create and merge it instead.
6. Check the [Actions tab](https://github.com/tXiao95/tXiao95.github.io/actions) for a successful **Build and deploy academic website** run, then open `/cv.pdf` on the website. Refresh the PDF view if the browser cached an old version.

All CV buttons point to this one file. See [Overleaf integration](docs/OVERLEAF.md) for optional source synchronization and compilation.

### Add or update a publication

The current site lists 18 works: 16 peer-reviewed publications and two preprints. Edit `data/publications.json` to update them. Copy an existing object and replace its values. JSON requires double quotes and commas between objects, with no trailing comma after the last item. This example illustrates the format, not an academic claim:

```json
{
  "id": "surname-2027-short-title",
  "type": "peer-reviewed",
  "year": 2027,
  "sort_date": "2027-03-15",
  "authors": "Surname AB, Hsiao TW, Surname CD",
  "title": "Replace with the verified publication title",
  "venue": "Replace with journal, volume, issue, and pages"
}
```

Required fields are `id`, `type`, `year`, `authors`, `title`, and `venue`. Choose `peer-reviewed`, `preprint`, or `manuscript` for `type`; entries appear in separate sections. Keep each lowercase, hyphenated `id` unique and stable because research links can point to it.

| Optional field | Value |
| --- | --- |
| `doi` | DOI only, without `https://doi.org/` |
| `arxiv` | arXiv identifier only |
| `url` | Full `https://` article URL |
| `code` | Full `https://` code repository URL |
| `sort_date` | Verified date: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD` |
| `featured` | Optional selected-work rank; currently hidden on the homepage |
| `note` | Short factual note, such as an accompanying editorial |
| `note_url` | Optional link for the note |
| `year_label` | Display text overriding the numeric year, if needed |

Each section sorts by year, then `sort_date`, newest first. Records without dates retain their file order within the same year and follow dated records. Use only verified date precision. Some older collaborative author lists retain the CV's `et al.` convention; see [publication sources](docs/PUBLICATION-SOURCES.md).

When a preprint is published, update its existing record and type rather than creating a duplicate. Retain its `id` to preserve links. Link from a research page with `[Paper title](publications.qmd#the-publication-id)`.

### Add news, an award, or a presentation

The homepage currently contains only the About Me biography and professional links, with space for a future photograph. Selected work and recent highlights are hidden. Their data is retained; ask Codex to restore either section when needed. Editing news data alone will not display a section.

Add an object to `data/news.json`:

```json
{
  "date": "2027-03",
  "label": "Mar 2027",
  "text": "Replace with a factual announcement."
}
```

Dates use `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`; entries appear newest first. An optional `url` makes the text a link. Remove older entries when you want a shorter homepage.

### Add the photograph later

Upload one image named `portrait.jpg`, `portrait.webp`, or `portrait.png` into `assets/`. The build detects it and adds it to the homepage; no placeholder photo appears while it is absent. A crop around 4:5 works well. Aim for roughly 600–1000 pixels wide and a compressed file below 300 KB. Keep only one of these filenames; if several exist, the build prefers WebP, then JPG, then PNG.

## Build and preview locally

Install [Quarto](https://quarto.org/docs/get-started/) and Python 3. Deployment pins Quarto **1.10.19** and Python **3.12**; matching versions locally simplifies troubleshooting. Python scripts use only the standard library.

From the repository in a Linux, macOS, or WSL terminal:

```sh
python3 scripts/prepare.py
quarto preview
```

The first command creates the includes needed for the initial preview. Quarto's pre-render hook also refreshes them during builds. Open the local address it prints. For a full build and structural check:

```sh
python3 scripts/prepare.py
quarto render
python3 scripts/check_site.py
```

Checks cover local links and anchors, page metadata, publication records, basic accessibility landmarks, absence of JavaScript, and byte-for-byte CV preservation. They do not replace browser testing or check external publishers' availability. For substantial changes, inspect desktop/mobile widths, keyboard navigation, publication links, and the PDF.

To preview custom-domain metadata on Linux/macOS/WSL, use `QUARTO_PROFILE=domain quarto preview`. In PowerShell, set `$env:QUARTO_PROFILE = 'domain'` before the command; remove it afterward with `Remove-Item Env:QUARTO_PROFILE`. Generated files live in `_site/`; do not edit or commit them. `_generated/` and `.quarto/` are disposable build output too.

## Deployment

`.github/workflows/publish.yml` prepares content, renders Quarto, checks output, uploads `_site/`, and deploys with GitHub Pages. Pushes to `main` publish; pull requests run checks without publishing. You can also select **Actions → Build and deploy academic website → Run workflow** on `main`.

In [repository Settings → Pages](https://github.com/tXiao95/tXiao95.github.io/settings/pages), the source is **GitHub Actions**. Deployment uses built-in GitHub credentials; it needs no personal access token. If a build fails, inspect the failed step in Actions. Failed builds do not replace the previously deployed website.

Default builds use `https://txiao95.github.io`. The Actions repository variable `SITE_PROFILE=domain` activates `_quarto-domain.yml`, custom-domain canonical URLs, and `CNAME` output. Changing the variable alone does not start a build; run the workflow or commit an update. See the [domain guide](docs/DOMAIN.md) for DNS, redirects, HTTPS, and migration.

## Source layout

```text
*.qmd                      Page content
cv.pdf                     Compiled CV, copied unchanged
data/publications.json    Publication records
data/news.json            Homepage highlights
assets/styles.css          Custom responsive design
assets/favicon.svg         Site icon
templates/page.html        Shared HTML template
includes/footer.html       Shared footer
scripts/prepare.py         Navigation and content includes
scripts/finalize.py        Canonical metadata and domain resources
scripts/check_site.py      Generated-site checks
_quarto.yml                Base configuration
_quarto-domain.yml         Custom-domain configuration
CNAME                      Custom-domain name
.github/workflows/         Automatic deployment
docs/                      Domain and maintenance guides
```

Initial academic content comes from the October 14, 2026 CV, stated research interests, and verified publication links. A research statement and photograph were deferred. Update claims when their status changes; the site does not automatically synchronize academic facts.

For design changes, ask Codex to edit this repository and preview the result. For example: “Keep the typography, but give research sections more space on mobile.”