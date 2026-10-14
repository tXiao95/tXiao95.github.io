# Publication sources and link audit

Checked on **October 14, 2026**. The supplied October 14, 2026 CV is the source for the publication list and abbreviated author lists. The website contains 18 works: 16 peer-reviewed publications and two public preprints. No publication or research result was added without a supplied or primary source.

## Metadata and dates

The table links to the registry records checked for each public publication. Each record returned successfully and matched the listed work. Crossref holds publisher-deposited metadata; DataCite holds the arXiv DOI metadata.

The `year` field preserves the CV's citation year. `sort_date` orders entries within that year, using the journal issue/print date when available, otherwise the online publication date. Preprints use their first submission date, so an updated version does not silently move above a newer work. Only verified precision is stored: a month is not assigned an invented day. Equal dates retain their order in the data file.

| Publication ID | Registry source | `sort_date` | Date basis |
| --- | --- | --- | --- |
| `li-2026-stillbirth` | [Crossref](https://api.crossref.org/works/10.1097/EE9.0000000000000505) | 2026-08 | August issue; metadata also records July 7 first publication |
| `hsiao-2026-isiw` | [Crossref](https://api.crossref.org/works/10.1007/s13253-026-00730-z) | 2026-04-17 | Online publication |
| `hsiao-2026-hypertension` | [Crossref](https://api.crossref.org/works/10.1161/HYPERTENSIONAHA.125.25829) | 2026-02 | Print issue |
| `hsiao-2026-aje` | [Crossref](https://api.crossref.org/works/10.1093/aje/kwaf019) | 2026-01-08 | Print issue; online January 28, 2025 |
| `varghese-2026-obesity` | [Crossref](https://api.crossref.org/works/10.1002/oby.70141) | 2026-04 | Print issue; online February 11, 2026 |
| `hsiao-2025-allocation` | [Crossref](https://api.crossref.org/works/10.1038/s41598-025-13804-8) | 2025-09-25 | Online publication |
| `hsiao-2025-jama` | [Crossref](https://api.crossref.org/works/10.1001/jamacardio.2025.2487) | 2025-10-01 | Print issue |
| `kendrick-2021-tobacco` | [Crossref](https://api.crossref.org/works/10.1016/S2468-2667%2821%2900065-7) | 2021-07 | Print issue |
| `reitsma-2021-smoking` | [Crossref](https://api.crossref.org/works/10.1016/S0140-6736%2821%2901169-7) | 2021-06 | Print issue |
| `vollset-2020-population` | [Crossref](https://api.crossref.org/works/10.1016/S0140-6736%2820%2930677-2) | 2020-10 | Print issue |
| `stanaway-2018-risk` | [Crossref](https://api.crossref.org/works/10.1016/S0140-6736%2818%2932225-6) | 2018-11 | Print issue |
| `murray-2018-population` | [Crossref](https://api.crossref.org/works/10.1016/S0140-6736%2818%2932278-5) | 2018-11 | Print issue |
| `lozano-2018-sdg` | [Crossref](https://api.crossref.org/works/10.1016/S0140-6736%2818%2932281-5) | 2018-11 | Print issue |
| `roth-2018-mortality` | [Crossref](https://api.crossref.org/works/10.1016/S0140-6736%2818%2932203-7) | 2018-11 | Print issue |
| `anderson-2017-arousal` | [Crossref](https://api.crossref.org/works/10.1145/3056540.3064956) | 2017-06-21 | Proceedings publication |
| `wu-2015-polyomavirus` | [Crossref](https://api.crossref.org/works/10.1159/000444921) | 2015 | Print year; online April 8, 2016 |
| `hsiao-2026-csdr` | [DataCite](https://api.datacite.org/dois/10.48550/arXiv.2606.14840) | 2026-06-12 | First arXiv submission |
| `li-2026-ozone` | [DataCite](https://api.datacite.org/dois/10.48550/arXiv.2602.16970) | 2026-02-19 | First arXiv submission |

## Corrections relative to the supplied CV

- The Environmental Epidemiology title includes **“air pollution exposure”** in the publisher's version.
- The Hypertension title includes **“in the United States”** in the publisher's version. Its February 2026 volume and issue are recorded, so the redundant “Advance online publication” label was removed. No page range was invented.
- The Obesity title ends with **“, 2024–2025”** in the publisher's version.
- The Lancet Public Health page range is **e482–e499**.
- The two 2021 tobacco articles now have DOI links as well as their existing open-access PMC links. The [NCBI identifier converter](https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=PMC8251505,PMC8223261&format=json) confirmed both PMC-to-DOI mappings, and the titles were then checked in Crossref.
- The AJE citation remains **2026**, and Intervirology remains **2015**, following their journal issue years and the supplied CV. Earlier/later online dates do not change those citation years.
- Abbreviated author lists are retained from the CV. The ozone preprint's registry gives Rebecca H. Zhang's full name; the website retains the CV's abbreviated “Zhang R.”

The [JAMA Cardiology editor's note](https://api.crossref.org/works/10.1001/jamacardio.2025.2492) was separately verified: Khan, Harrington, and Ahmad; “Blood Pressure Measurement in Retail Stores and Population Health”; 2025, 10(10), 1049. It is a note about the research, not an additional Hsiao publication.

## External link results

Ordinary HTTP GET requests followed redirects. **No tested publication, software, or professional link returned a 404.** A successful DOI registration or redirect does not imply free full-text access.

- Both arXiv pages and DOI redirects returned their matching titles.
- Both PMC article pages returned their matching titles. The corresponding DOI links also resolved to Elsevier's article redirect service.
- ISIW, Scientific Reports, and Environmental Epidemiology DOI links returned their matching publisher pages.
- The remaining Lancet DOI links resolved to Elsevier's article redirect service; their work titles and citation metadata were independently verified in Crossref.
- JAMA Cardiology (article and editor's note), Wiley/Obesity, Oxford/AJE, ACM, Karger/Intervirology, and AHA/Hypertension returned automated-browser challenges (HTTP 403) after valid DOI redirects. Their identifiers and work metadata were verified through Crossref. Full publisher-page access is **unverified by this automated check**, rather than classified as broken.
- [GitHub profile](https://github.com/tXiao95), [csdr](https://github.com/tXiao95/csdr), [ISIW](https://github.com/tXiao95/ISIW), [gallery on CRAN](https://cran.r-project.org/package=gallery), [Google Scholar](https://scholar.google.com/citations?user=5Jnm9BoAAAAJ), and [ORCID](https://orcid.org/0009-0005-7848-7992) returned successfully. GitHub and Scholar identified Thomas Hsiao; CRAN identified him as gallery's author and maintainer.
- [LinkedIn](https://www.linkedin.com/in/thsiao3/) returned its automation-denial status (HTTP 999). The link is supplied in the CV and retained; its profile content is **unverified by this automated check**.
- The email address is copied from the user and CV. Email delivery was not tested, and no message was sent.

## Research description sources

The [CSDR arXiv abstract](https://arxiv.org/abs/2606.14840) supports the description of low-dimensional causal exposure summaries and the application to maternal PFAS exposure and infant birth weight. The [ISIW publisher abstract](https://link.springer.com/article/10.1007/s13253-026-00730-z) supports the preferential-sampling methods description. The [allocation paper](https://www.nature.com/articles/s41598-025-13804-8) supports the access, precision, and equity application. The [ozone preprint](https://arxiv.org/abs/2602.16970) supports the respiratory-health mediation topic. The remaining application descriptions follow the verified publication topics. Informative missingness and data fusion are presented as current interests, as requested by the user; the site does not claim that the kiosk application papers establish a new missing-data method.

The portrait remains pending. The site does not substitute a stock or generated photograph, and no unavailable research statement is treated as a source.
