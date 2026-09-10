# Changelog

All notable changes to this repo are documented here. Versioning follows
[Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`), independent
of the Engine's own version.

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
