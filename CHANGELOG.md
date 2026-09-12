# Changelog

All notable changes to this repo are documented here. Versioning follows
[Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`), independent
of the Engine's own version.

## [1.8.3] - 2026-09-12

### Changed
- Regenerated `assets/favicon.ico`, `assets/icon.png`, `assets/logo.png`,
  and `assets/steam/*` again from the Engine, which fixed the wordmark's
  vertical alignment/canvas cropping, the icon's tile-pattern margins, and
  a wordmark-crop bug in the Steam-art generator that clipped/overlapped
  text in `assets/steam/logo.png` — see the Engine's v5.2.0 changelog for
  details. `assets/steam/*` is now synced automatically by the Engine's
  build script instead of needing a manual copy.
- Bumped the site-wide cache-busting `?v=` query string from `1.8.0` to
  `1.8.3` on every page, so browsers pick up the regenerated assets above.

## [1.8.2] - 2026-09-12

### Changed
- Regenerated `assets/favicon.ico`, `assets/icon.png`, `assets/logo.png`
  from the Engine's `src/build/create_project_assets.py`, which now writes
  these directly instead of requiring a manual copy — kept in sync with
  the app's current branding.

## [1.8.1] - 2026-09-12

### Fixed
- **Cache-busting `?v=` query strings were stuck at `1.3.0`** on every
  page despite `VERSION.md` being at `1.8.0` — bumped every reference to
  `?v=1.8.0`. Added a note to `CONTRIBUTING.md`'s Versioning section so
  this gets bumped alongside `VERSION.md` on every future release instead
  of going stale again.
- `guides/steam.html` used root-absolute asset paths (`/assets/...`,
  `/style.css`) while every sibling page under `guides/` uses relative
  `../` paths — both worked, but it was an inconsistent convention.
  Normalized to match, and moved its one remaining inline
  `style="font-size:1.5rem;"` into a new `.page-title-sm` class (the last
  inline style anywhere outside `steam.html`'s already-fixed images).

## [1.8.0] - 2026-09-12

### Added
- **`guides/install.html`** and **`guides/developer.html`** — deploying a
  copy of this site (GitHub Pages/custom domain/any static host) and
  running it locally (cloning alongside the Engine, `dev-server.py`, dev
  mode), adapted from TIGHC's `INSTALL.md`/`DEV_GUIDE.md` content but as
  guide pages instead of root-level markdown files, matching this site's
  own `guides/` pattern. Linked from `/guides` and from the README's
  "Local preview"/"Deploying" sections.
- **`404.html`** — a custom error page (GitHub Pages serves it
  automatically for any unmatched path in production); `dev-server.py`
  now serves it locally too on a 404, instead of Python's generic error
  page, so it can actually be previewed.

### Changed
- **`guides.html` → `guides/index.html`, `legal.html` → `legal/index.html`**
  — each hub page now lives alongside its own sub-pages instead of
  beside the folder. `steam.html` stays a flat file (it has no
  sub-pages). All internal links were already root-relative
  (`/guides`, `/legal`, ...) so nothing else needed updating; only the
  moved pages' own relative asset/script paths gained a `../`.

### Fixed
- **`dev-server.py` couldn't resolve any of the site's clean URLs for
  flat pages** (`/engine`, `/steam`, `/changelogs`, `/releases` all
  404'd locally despite working in production) — `SimpleHTTPRequestHandler`
  has no extension-optional resolution of its own. Ported the fix
  already in the sibling TWRAR project's `dev-server.py`:
  `translate_path()` now prefers `<path>.html` when it exists.
- README's `Structure` section was badly stale — it still said the Steam
  guide, changelog viewer, and legal hub were "still planned" when all
  three have existed since earlier this session, and even after that fix
  it was still an abbreviated summary rather than every actual file.
  Rewrote it to exhaustively list the current file set, and added
  `Deploying`/`Testing` sections.

## [1.7.0] - 2026-09-12

### Added
- **CI** (`.github/workflows/ci.yml`), ported from the sibling TIGHC
  project's Website: a `node --test` unit-test job and an
  `html-validate` job over every top-level HTML page.
- **`tests/`**: `changelogs.test.js`, `versions.test.js`, and
  `releases.test.js` — unit tests for the pure logic those scripts
  already exported via `module.exports` but nothing previously
  exercised.

### Fixed
- Two inline `style="..."` attributes on `steam.html`'s preview images
  (`no-inline-style` html-validate failures) — moved into a new
  `.card-preview-img` class in `style.css`.

## [1.6.1] - 2026-09-12

### Fixed
- **`/engine` and `/changelogs` were dead links** — every page's nav and
  footer already linked to them, and `versions.js`/`style.css` already
  had the supporting code, but the pages themselves were never created.
  Added `engine.html` (install/usage guide), `changelogs.html` (live
  changelog viewer for both repos, ported from the sibling TWRAR
  project's pattern), `changelog.html` (singular → plural redirect), and
  `changelogs.js` (fetches and renders each repo's `CHANGELOG.md`).

## [1.6.0] - 2026-09-12

### Added
- **`icon.png`** listed on `/guides/steam`'s asset table (256x256, Steam's
  separate "Icon" custom-artwork slot) — matches the Engine's v5.1.0
  addition of `assets/steam/icon.png`.

### Changed
- Refreshed the local `assets/steam/*.png` preview copies (also adding the
  previously-missing `logo_horizontal.png`) to match the Engine's current
  generated set.

## [1.5.0] - 2026-09-13

### Added
- **`/legal`** (`legal.html`) + `legal/{privacy,terms,cookies,imprint,disclaimer,opt-out}.html`:
  the "Boring Legal Stuff" hub, ported from the TWRAR/Website pattern and
  rewritten for TS4RLS's own content (what the Engine actually does/
  collects, GPL-3.0-or-later, the EA/Maxis disclaimer, etc.) — the
  footer's `/legal` link across every existing page finally resolves to
  something instead of 404ing.
- **`/guides`** (`guides.html`) + `guides/{windows,macos,linux}.html`:
  per-platform setup notes (standalone executable, running from source,
  Mods-folder auto-detection/manual lookup including the Proton-prefix
  path on Linux, and platform-specific troubleshooting), same pattern as
  TWRAR/Website. Distinct from the existing `/guides/steam` page, which
  it cross-links.
- A "Guides" nav link and footer link added to every existing page
  (`index.html`, `releases.html`, `steam.html`, `guides/steam.html`).

### Changed
- Nav label reworded from bare "Steam" to "Steam Artwork" site-wide —
  "Steam" on its own read like a platform-availability claim rather than
  a link to the library artwork.

## [1.4.0] - 2026-09-12

### Added
- **`/steam`** (`steam.html`): a landing page for the Steam library
  artwork — a couple of previews, a download button, and a link to the
  full guide. Fixes every existing `/steam` link across the site (nav,
  footer, the homepage's "Steam artwork included" card) that previously
  404'd.
- **`/guides/steam`** (`guides/steam.html`): the full "add TS4RLS to
  Steam" guide — asset list (file/size/slot), the two setup steps, and
  a link to the community screenshot walkthrough.
- **`/assets/steam`** (`assets/steam.html`): redirects straight to the
  latest `TS4RLS_Steam_Assets.zip` (meta-refresh + JS, with a manual
  link as a fallback) — the single place that URL is hardcoded, so
  `/steam`, `/guides/steam`, and the Releases page button all link here
  instead of each repeating it.
- `script.js`: never actually existed in this repo despite every page's
  `<head>` loading it, so the theme toggle and mobile nav button have
  been silently dead site-wide until now. Restored (mobile nav
  open/close + theme toggle), matching the TIGHC/TWRAR sibling sites.
- A "Download Steam artwork (.zip)" button on the Releases page hero,
  linking to `/assets/steam`.

### Changed
- Footer's "Steam guide" link reworded to "Steam Artwork" and now points
  straight at `/assets/steam` (the zip download) instead of a guide page
  — `/guides/steam` is one click away from `/steam` for anyone who wants
  the how-to instead. The homepage card's copy updated to match.

## [1.3.0] - 2026-09-10

### Added
- **`releases.html`/`releases.js`**: lists every TS4RLS/Engine GitHub
  Release, fetched live from the API — platform-labeled asset download
  buttons (Windows/macOS/Linux, plus the Steam assets zip), release notes
  rendered from each release's body, and a standing notice that the
  text-menu CLI was discontinued in Engine v3.0.0 (older releases still
  show their CLI-era asset names for reference, since they predate the
  naming pattern this page otherwise labels).
- `.hero-warning` and `.profiles-hero` styles in `style.css` (the rest of
  the releases-page CSS — `.release-*`, `.page-title` — was already
  carried over from the TIGHC/TWRAR pattern, just unused until now).

## [1.2.2] - 2026-09-10

### Fixed
- `commit.sh`/`dev-server.sh` were committed without the executable bit
  (git tracked them as `100644` instead of `100755`) — found while fixing
  the identical issue in Engine's `build.sh`, which actually broke a
  release there. Not yet CI-invoked here, but worth the same fix.

## [1.2.1] - 2026-09-10

### Fixed
- **Dev Mode banner showed in production.** `.env-banner { display: flex }`
  overrode the `hidden` attribute's default styling (an author-stylesheet
  rule always beats the user-agent stylesheet at equal specificity), so
  the banner was visible on every page load regardless of whether
  `dev-config.js` had actually revealed it. Added `.env-banner[hidden] {
  display: none; }` (present in TIGHC's Website, missing here). Verified
  with a plain static server (no `dev-server.py` involved): banner now
  stays hidden.
- Synced `assets/logo.png` with Engine's updated brand mark again — bold
  weight, not just matching color, is what actually made the subtitle
  read clearly.

## [1.2.0] - 2026-09-10

### Added
- **`versions.js`**: fetches `VERSION.md` from Engine and this repo (from
  GitHub in production, from the dev-sibling proxy in dev mode) and
  populates every `[data-version]` element — the hero badge and footer
  version line were both stuck on placeholder text (`vX.Y.Z`/a stale
  hardcoded `v1.0.0`) with no script to fill them in.

### Changed
- Footer reorganized: "Written & Maintained by StuxieDev" (→ stuxie.dev)
  is now the last link in the "More" column instead of sitting before
  "Boring Legal Stuff"; "A StuxieDev Project" (→ projects.stuxie.dev) is
  now its own link under the "Unaffiliated with EA/Maxis" note, rather
  than being combined into one link.
- Synced `assets/logo.png` with Engine's updated brand mark again — the
  matching-color subtitle from the previous release was still too faint;
  the real fix was the font weight (light → regular), not just the color.

## [1.1.0] - 2026-09-10

### Added
- **Dev Mode banner**: `dev-server.py`/`.sh`/`.bat` for local preview,
  matching TIGHC's Website — `DEV_MODE` is forced on by default, revealing
  a yellow "Development Mode" banner and proxying `/dev-sibling/engine` to
  a sibling `../Engine` checkout for future scripts to read. Pass
  `--no-dev-mode` to preview production behavior instead.

### Changed
- Upgraded vendored Font Awesome Free from 6.7.2 to **7.3.1** (latest).
- Synced `assets/logo.png` with Engine's updated brand mark (darker,
  more visible subtitle text).

## [1.0.0] - 2026-09-10

### Added
- Initial landing page (`index.html`) for ts4rls.stuxie.dev: hero, feature
  grid, how-it-works steps, get-started section, and footer, matching
  Engine v4.1.0 (GUI + headless only, no CLI/CurseForge, single Steam
  artwork set, `TS4RLS.package` output).
- Vendored Font Awesome Free 6.7.2 (`assets/fontawesome/`) for site icons.
- Brand assets (`icon.png`, `logo.png`, `favicon.ico`, `author.png`,
  `steam/`) copied from the Engine repo.
