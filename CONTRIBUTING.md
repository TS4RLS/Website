<p align="center">
  <img src="assets/logo.png" width="300" alt="TS4RLS — The Sims 4 Random Loading Screen">
</p>

# Contributing to the TS4RLS Website

Issues and pull requests are welcome at
[github.com/TS4RLS/Website](https://github.com/TS4RLS/Website).

## Getting set up

No build tooling required — plain HTML/CSS. Open `index.html` directly in
a browser, or serve the folder with any static file server.

## Making a change

- Keep pages consistent with `style.css` — avoid inline styles or one-off
  CSS unless there's a good reason.
- Icons come from the vendored Font Awesome build under
  `assets/fontawesome/` — don't load icons from a CDN.

## Versioning

Bump [`VERSION.md`](VERSION.md) and add a matching entry to
[`CHANGELOG.md`](CHANGELOG.md) in the same PR, following
[Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`),
independent of the Engine's own version.

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
