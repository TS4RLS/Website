<p align="center">
  <img src="assets/logo.png" width="300" alt="TS4RLS — The Sims 4 Random Loading Screen">
</p>

# TS4RLS Website

**Version 1.7.0** — see [CHANGELOG.md](CHANGELOG.md) for release history.

Source for [ts4rls.stuxie.dev](https://ts4rls.stuxie.dev), the landing site
for [TS4RLS](https://github.com/TS4RLS/Engine) (The Sims 4 Random Loading
Screen). Plain HTML/CSS — served directly from this repo via GitHub Pages,
no build step.

Website: https://ts4rls.stuxie.dev  
Repository: https://github.com/TS4RLS/Website  
License: [GPL-3.0-or-later](LICENSE.md)

## Structure

```
index.html          # landing page — what TS4RLS is, features, how it works, get started
releases.html       # TS4RLS Engine releases, fetched live from the GitHub Releases API
style.css           # shared styles
versions.js         # fetches VERSION.md from Engine/Website on load, populates version badges
releases.js         # fetches and renders TS4RLS/Engine's GitHub releases for releases.html
assets/             # logo/icon/author avatar, copied from the Engine repo's assets/
assets/fontawesome/ # Font Awesome Free (vendored, self-hosted — see its own LICENSE.txt)
dev-server.py       # local dev server shared by dev-server.sh/.bat (see Local preview below)
dev-server.sh       # Unix wrapper for dev-server.py
dev-server.bat      # Windows wrapper for dev-server.py
CNAME               # custom domain (ts4rls.stuxie.dev) for GitHub Pages
```

More pages (usage docs, Steam guide, a changelog viewer, a legal hub) and
the scripts behind the header's theme/nav toggle are still planned; see
[TIGHC/Website](https://github.com/TIGHC/Website) for the fuller
pattern this site will grow into.

## Local preview

```
./dev-server.sh      # or dev-server.bat on Windows
```

Serves this folder the way GitHub Pages does, at http://127.0.0.1:8000.
`DEV_MODE` is forced on by default: it writes `dev-config.js` (gitignored,
never deployed), which reveals the yellow "Development Mode" banner at the
top of the page and proxies `/dev-sibling/engine` to a sibling `../Engine`
checkout, so future scripts reading Engine's `VERSION.md`/`CHANGELOG.md`
can use local edits without pushing first. Pass `--no-dev-mode` to test the
site as it behaves in production (banner hidden) instead, and a port
number to use something other than 8000.

## Versioning

Follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`),
independently of the Engine's own version — see
[CHANGELOG.md](CHANGELOG.md) for what changed in each release.

## License

See [LICENSE.md](LICENSE.md).

---

*Written & Maintained by <img src="https://github.com/StuxieDev.png" height="14" alt="StuxieDev" valign="middle"> [StuxieDev](https://stuxie.dev).*

*[A StuxieDev Project](https://projects.stuxie.dev)*
