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

This project uses [Date Versioning](https://datevers.ing). To release:

1. Add a `## vYY.MM.DD` entry at the top of `CHANGELOG.md`, with its sections in this order: Added, Changed, Fixed, Removed, Security, Deprecated.
2. Set `VERSION.md` to the same bare version (no `v`): today's **UTC** date as `YY.MM.DD`, or `YY.MM.DD-1`, `-2`… for later releases the same UTC day. Never a future date. Use UTC, not local time: just after midnight in the UK it is still the previous day in UTC.
3. Run `bash tests/version.sh`.
4. Run `./commit.sh` (or `commit.bat` on Windows). It checks the version, commits and tags `vYY.MM.DD`, and never pushes.

## Sitemap

`sitemap.xml`, `sitemap/index.html` and `robots.txt` are generated: after adding or removing a public page, edit the `PAGES` list in `scripts/build-sitemap.py`, run `python scripts/build-sitemap.py`, and commit the result. `python -m unittest discover -s tests` checks them.

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
