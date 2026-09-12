<p align="center">
  <img src="assets/logo.png" width="300" alt="TS4RLS — The Sims 4 Random Loading Screen">
</p>

# TS4RLS Website

**Version 1.8.3** — see [CHANGELOG.md](CHANGELOG.md) for release history.

Source for [ts4rls.stuxie.dev](https://ts4rls.stuxie.dev), the landing site
for [TS4RLS](https://github.com/TS4RLS/Engine) (The Sims 4 Random Loading
Screen). Plain HTML/CSS — served directly from this repo via GitHub Pages,
no build step.

Website: https://ts4rls.stuxie.dev  
Repository: https://github.com/TS4RLS/Website  
License: [GPL-3.0-or-later](LICENSE.md)

## Structure

Plain HTML/CSS/JS, no build step, deployed via GitHub Pages (see `CNAME`):

```
index.html               # landing page — what TS4RLS is, features, how it works, get started
engine.html               # install/usage docs for the Engine (GUI tabs, config, the runner exe)
changelogs.html           # tabbed changelog viewer (Engine / Website)
changelogs.js             # fetches and renders CHANGELOG.md from each repo for changelogs.html
changelog.html            # redirect alias for /changelogs (singular → plural)
releases.html             # TS4RLS Engine releases, fetched live from the GitHub Releases API
releases.js               # fetches and renders TS4RLS/Engine's GitHub releases for releases.html
steam.html                # Steam library artwork landing hub (no sub-pages, so no /steam folder)
404.html                  # custom error page, served automatically by GitHub Pages
style.css                 # shared styles
script.js                 # mobile nav toggle and the light/dark theme toggle
versions.js               # fetches VERSION.md from Engine/Website on load, populates version badges
CNAME                     # custom domain (ts4rls.stuxie.dev) for GitHub Pages

legal/index.html          # "Boring Legal Stuff" hub, linking to legal/*.html
legal/privacy.html
legal/terms.html
legal/cookies.html
legal/imprint.html
legal/disclaimer.html
legal/opt-out.html

guides/index.html         # setup guides hub, linking to guides/*.html
guides/windows.html
guides/macos.html
guides/linux.html
guides/steam.html         # full "add TS4RLS to Steam" artwork guide
guides/install.html       # deploying a copy of this site (see Deploying below)
guides/developer.html     # running this site locally (see Local preview below)

assets/icon.png           # copied from the Engine repo's assets/
assets/logo.png
assets/author.png
assets/favicon.ico
assets/steam.html         # /assets/steam — redirects to the Engine's TS4RLS_Steam_Assets.zip
assets/steam/*.png        # generated Steam library artwork (6 files), copied from the
                          # Engine's src/build/steam_asset_builder.py output
assets/fontawesome/       # Font Awesome Free (vendored, self-hosted — see its own LICENSE.txt)

tests/changelogs.test.js  # node:test unit tests for changelogs.js
tests/releases.test.js    # node:test unit tests for releases.js
tests/versions.test.js    # node:test unit tests for versions.js
.github/workflows/ci.yml  # runs `node --test` and html-validate on every push/PR

dev-config.js             # written by dev-server.py at startup — gitignored, never deployed
dev-server.py             # local dev server shared by dev-server.sh/.bat (see Local preview below)
dev-server.sh             # Unix wrapper for dev-server.py
dev-server.bat            # Windows wrapper for dev-server.py

CHANGELOG.md / VERSION.md / CONTRIBUTING.md / LICENSE.md
commit.sh / commit.bat    # commit + tag a release, reading the version from VERSION.md
.gitignore
```

## Local preview

See [/guides/developer](https://ts4rls.stuxie.dev/guides/developer) to run
the site locally.

## Deploying

GitHub Pages is configured to serve from this repo's root on `main` — just
push. The `CNAME` file points the custom domain at GitHub Pages; don't
remove it unless the domain setup is changing too. See
[/guides/install](https://ts4rls.stuxie.dev/guides/install) for
self-hosting elsewhere.

## Testing

The parsing/formatting logic in `changelogs.js`, `releases.js`, and
`versions.js` (changelog Markdown parsing, release-notes formatting and
asset labeling/sorting, version-string handling) has unit tests under
`tests/`, using Node's built-in test runner — no extra dependencies
required:

```
node --test
```

CI (`.github/workflows/ci.yml`) runs these tests and validates the
top-level HTML pages with [html-validate](https://html-validate.org/) on
every push and pull request.

## Versioning

Follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`),
independently of the Engine's own version — see
[CHANGELOG.md](CHANGELOG.md) for what changed in each release.

## License

See [LICENSE.md](LICENSE.md).

---

*Written & Maintained by <img src="https://github.com/StuxieDev.png" height="14" alt="StuxieDev" valign="middle"> [StuxieDev](https://stuxie.dev).*

*[A StuxieDev Project](https://projects.stuxie.dev)*
