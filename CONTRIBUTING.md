<p align="center">
  <img src="assets/logo.png" width="300" alt="TS4RLS — The Sims 4 Random Loading Screen">
</p>

# Contributing to the TS4RLS Website

Issues and pull requests are welcome at
[github.com/TS4RLS/Website](https://github.com/TS4RLS/Website).

## Getting set up

No build tooling required — plain HTML/CSS. Run `./dev-server.sh` (or
`dev-server.bat` on Windows) and open http://127.0.0.1:8000, or just open
`index.html` directly in a browser.

## Making a change

- Keep pages consistent with `style.css` — avoid inline styles or one-off
  CSS unless there's a good reason.
- Icons come from the vendored Font Awesome build under
  `assets/fontawesome/` — don't load icons from a CDN.
- If you add a script that reads Engine's `VERSION.md`/`CHANGELOG.md`,
  test it with `./dev-server.sh`/`dev-server.bat` (not `file://`), since
  `fetch` needs an HTTP origin — it proxies `/dev-sibling/engine` to a
  sibling `../Engine` checkout so local edits show up without pushing
  first.

## Versioning

Bump [`VERSION.md`](VERSION.md) and add a matching entry to
[`CHANGELOG.md`](CHANGELOG.md) in the same PR, following
[Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`),
independent of the Engine's own version. Also bump the `?v=X.Y.Z` query
string on every `style.css`/`script.js`/`versions.js`/`changelogs.js`/
`releases.js`/`logo.png`/`icon.png`/`favicon.ico`/`assets/steam/*`
reference across every page, to that same version — it exists purely to
bust browser caches on release, so it needs to move every time or
visitors can keep serving a stale cached copy indefinitely.

## Deploying

Merges to `main` publish automatically via GitHub Pages — no separate
deploy step. Don't remove the `CNAME` file unless the custom domain setup
is changing too.

## Reporting a bug

Open an issue with the page, browser, and what looked wrong (a screenshot
helps).

## License

TS4RLS Website is licensed under the [GPL-3.0-or-later](LICENSE.md). By
contributing, you agree your contribution is licensed under the same terms.
