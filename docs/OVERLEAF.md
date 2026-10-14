# Keep Overleaf as the CV source of truth

The active workflow is simple: edit in Overleaf, download the PDF, replace the root `cv.pdf`, and commit. GitHub Actions publishes it automatically. There is no parallel HTML CV to maintain. See the [browser-only replacement instructions](../README.md#replace-the-cv).

## Optional source synchronization

Overleaf's GitHub synchronization is a premium feature that may already be included through an institutional or group subscription. Check existing access before considering a purchase. It lets the project owner link an Overleaf project to a **new** GitHub repository, then explicitly push or pull through the project's GitHub menu. It does not continuously publish every edit. Overleaf currently cannot pair an existing Overleaf project directly with an existing GitHub repository. [Overleaf GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization)

Use a separate **private CV-source repository** created from the existing Overleaf project. Continue editing in Overleaf and push when ready. That repository can compile the PDF in Actions and supply a download or propose a website update.

Overleaf also exposes a Git endpoint at `https://git.overleaf.com/PROJECT_ID`. A script could fetch using an Overleaf Git authentication token and compile on demand or on a schedule. This adds credentials and another synchronization path, so it is unnecessary for the initial website. [Overleaf Git integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration)

## Optional Actions compiler

[examples/cv-build.yml.example](examples/cv-build.yml.example) is an inactive starting example. It enables no workflow here. The LaTeX source, main filename, compiler, fonts, and packages were not supplied, so it has **not been tested against the actual CV**.

To adopt it:

1. Create a private source repository through Overleaf's GitHub synchronization, separate from this website.
2. Check Overleaf's main document, compiler, and TeX Live version. Synchronize all source, bibliography, class, style, image, and required font files.
3. Copy the example to `.github/workflows/cv-build.yml` in that source repository. Adjust `MAIN_TEX`, `LATEXMK_MODE`, and TeX packages to match. Defaults are `main.tex` and pdfLaTeX; XeLaTeX needs `-xelatex` and the right fonts. For exact reproducibility, use a fixed TeX Live container matching the project once its version is known.
4. Push the ready CV from Overleaf, or select **Run workflow** in the source repository. Inspect the PDF artifact, including fonts and page breaks. A failed compile stops the workflow.
5. Initially download the artifact and replace the website's `cv.pdf` through GitHub as usual. This stage needs no cross-repository credential.

The example uses Ubuntu distribution TeX packages as a starting point. Private-repository Actions runs consume the account's included allowance; check usage before enabling frequent builds. Nothing here enables scheduled polling, a subscription, or paid capacity.

## Optional pull request delivery

The example's delivery job is disabled by default. After validating compilation, it can open a pull request containing only the new `cv.pdf` in the website repository:

1. Create a fine-grained GitHub token restricted to `tXiao95/tXiao95.github.io` with **Contents: read and write** and **Pull requests: read and write**, or use an App installation token with those permissions.
2. Store it as the private source repository's Actions secret `WEBSITE_UPDATE_TOKEN`. Keep it out of Overleaf source, URLs, and committed files.
3. Set that repository's Actions variable `ENABLE_WEBSITE_PR` to `true`.
4. Push from Overleaf. Inspect the website pull request and PDF, then merge it yourself. The human merge to `main` starts deployment.

Each changed build creates a branch and pull request. Close superseded requests before merging the newest. A rerun may encounter its existing branch; start a fresh workflow run if needed. Make textual corrections in Overleaf and synchronize again.

The default `GITHUB_TOKEN` belongs to its own repository and cannot supply this cross-repository access. A push using it also does not start another push-triggered workflow. A human merge, suitable App/personal token, or explicit workflow dispatch avoids that trap. [GitHub workflow triggers](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)

Manual PDF replacement remains a dependable fallback if this optional integration is adopted.