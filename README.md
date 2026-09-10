<p align="center">
  <img src="assets/logo.png" width="300" alt="TS4RLS — The Sims 4 Random Loading Screen">
</p>

# TS4RLS Website

**Version 1.0.0** — see [CHANGELOG.md](CHANGELOG.md) for release history.

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
style.css           # shared styles
assets/             # logo/icon/author avatar, copied from the Engine repo's assets/
assets/fontawesome/ # Font Awesome Free (vendored, self-hosted — see its own LICENSE.txt)
CNAME               # custom domain (ts4rls.stuxie.dev) for GitHub Pages
```

This is an early, single-page version of the site — more pages (usage
docs, Steam guide, changelog viewer, releases, a legal hub) and the
scripts behind them (theme/nav toggle, live version badges) are planned;
see [TIGHC/Website](https://github.com/TIGHC/Website) for the fuller
pattern this site will grow into.

## Versioning

Follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`),
independently of the Engine's own version — see
[CHANGELOG.md](CHANGELOG.md) for what changed in each release.

## License

See [LICENSE.md](LICENSE.md).

---

*Written & Maintained by <img src="https://github.com/StuxieDev.png" height="14" alt="StuxieDev" valign="middle"> [StuxieDev](https://projects.stuxie.dev).*
