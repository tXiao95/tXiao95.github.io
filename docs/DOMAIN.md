# Connect and maintain twhsiao.com

The canonical address is **https://www.twhsiao.com**. The registered domain is `twhsiao.com`; `www` is a subdomain. Cloudflare manages registration and DNS; GitHub Pages hosts the site. The apex redirects to `www`, with the CV at `https://www.twhsiao.com/cv.pdf`.

## Setup status — October 14, 2026

- GitHub account ownership verification completed for `twhsiao.com`.
- Cloudflare contains four IPv4 records, four IPv6 records, the `www` CNAME, and GitHub's verification TXT record. Web records use DNS only and a 300-second TTL.
- Repository Pages uses GitHub Actions and custom domain `www.twhsiao.com`.
- Actions repository variable `SITE_PROFILE=domain` is saved.
- The initial GitHub Actions build and deployment completed successfully. The custom domain serves the website with a valid certificate, and **Enforce HTTPS** is enabled.

The following steps document this configuration for maintenance or recovery. Check live settings first; do not duplicate existing records.

## 1. Verify ownership in GitHub

Open [personal GitHub Settings → Pages](https://github.com/settings/pages), select **Add a domain**, and enter `twhsiao.com`. Copy GitHub's exact TXT name and generated value into **Cloudflare → twhsiao.com → DNS → Records**. The name follows the form `_github-pages-challenge-tXiao95`; use GitHub's exact spelling and value. Return to GitHub and select **Verify**. Retain the TXT afterward. Apex verification also covers the immediate `www` subdomain. [GitHub domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)

## 2. Configure Pages

In [repository Settings → Pages](https://github.com/tXiao95/tXiao95.github.io/settings/pages), choose **GitHub Actions** as the source. Save **Custom domain** as `www.twhsiao.com` before pointing DNS to GitHub. Actions deployments ignore `CNAME` for this setting; the file alone cannot configure it. [GitHub custom-domain setup](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

## 3. Configure Cloudflare DNS

In **Cloudflare → twhsiao.com → DNS → Records**, use **Proxy status: DNS only** (gray cloud) for these records. Use **TTL: Auto**, or the existing **5 min / 300 seconds** setting. DNS-only records send traffic directly to GitHub, which handles TLS and redirects. [Cloudflare proxy status](https://developers.cloudflare.com/dns/proxy-status/)

| Type | Name | Content |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `txiao95.github.io` |

IPv6 records are optional; all four are included in this setup:

| Type | Name | Content |
| --- | --- | --- |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

`@` means the apex. Replace conflicting parking or old hosting records at `@` and `www`, preserving unrelated email and verification records. Use no wildcard. The `www` target has no `https://`, path, or repository name. With both names configured, GitHub redirects the apex to the saved `www` domain. Propagation can take up to 24 hours. [GitHub DNS values and redirects](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

No Cloudflare redirect rule or paid add-on is needed. Leave these web records DNS only for this configuration.

## 4. Enable the custom-domain build

Open repository **Settings → Secrets and variables → Actions → Variables** and set:

| Name | Value |
| --- | --- |
| `SITE_PROFILE` | `domain` |

Run **Actions → Build and deploy academic website → Run workflow** on `main`, or commit an update. This variable becomes `QUARTO_PROFILE`; `_quarto-domain.yml` and `scripts/finalize.py` then produce custom-domain canonical URLs and copy `CNAME` into `_site/`.

If the domain changes, update `CNAME`, `website.site-url` in `_quarto-domain.yml`, the custom-domain `base` in `scripts/finalize.py`, GitHub Pages settings, DNS, and links in these guides together.

## 5. Finish HTTPS and verify

GitHub requests a certificate after the DNS check succeeds. Once available, select **Enforce HTTPS** in repository **Settings → Pages** to redirect HTTP traffic to HTTPS. If issuance remains pending, inspect DNS and Pages status before making further changes. [GitHub HTTPS setup](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)

Check in a browser:

- `https://www.twhsiao.com/` loads without a certificate warning.
- `https://twhsiao.com/` redirects to the `www` address.
- `http://www.twhsiao.com/` and `http://twhsiao.com/` end at HTTPS.
- `https://www.twhsiao.com/cv.pdf` shows the current CV.
- `/research.html` loads directly and navigation works.

Optional PowerShell DNS checks:

```powershell
Resolve-DnsName twhsiao.com -Type A
Resolve-DnsName www.twhsiao.com -Type CNAME
```

The apex should answer with the four IPv4 addresses above; `www` should target `txiao95.github.io`. DNS answers alone do not prove HTTPS is ready.

## Moving to another host

Registration stays in your Cloudflare account. Build the Quarto project and deploy `_site/` to the new static host, configure `www.twhsiao.com` there, and obtain its certificate. Replace web-hosting DNS records with the new host's values. Preserve `/cv.pdf` and page paths, and configure the same apex-to-`www` redirect. Remove the GitHub Pages custom domain after migration works. Changing hosts does not require a new domain or registrar transfer.

To return this repository to the default GitHub address, remove the Pages custom domain, clear `SITE_PROFILE`, and rebuild. Update or remove the old GitHub DNS records according to the domain's new destination.