# Changelog

All notable changes to this repo are documented here. Versioning follows
[Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`), independent
of the Engine's own version.

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
