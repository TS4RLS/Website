#!/usr/bin/env python3
"""Writes the Discord component embed (<script id="discord:component-embed">)
into the <head> of every page, between the favicon tags and </head>.

Run it after adding a page or changing a page's <title>/description:

    python scripts/build-discord-embeds.py

It is idempotent: an existing embed (or its "left out" comment) is replaced.
Pages that are error pages or redirect stubs are skipped. Names and
descriptions are escaped so Discord shows them as plain text, and an embed over
Discord's 3,000-byte limit is replaced by an HTML comment (Open Graph stays).
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://ts4rls.stuxie.dev"
ACCENT = 0x2E7D32
MAX_BYTES = 3000
SKIP = {"404.html", "changelog.html"}
ENGINE_REPO = "https://github.com/TS4RLS/Engine"

EMBED_RE = re.compile(
    r'(?:<script id="discord:component-embed" type="application/json">.*?</script>'
    r'|<!-- discord:component-embed left out[^>]*-->)\n?', re.S)


def md(s):
    """Escapes Discord markdown so data shows as plain text."""
    s = re.sub(r'([\*_~`|\[\]])', r'\\1', s)
    return re.sub(r'^([#>-])', r'\\1', s, flags=re.M)


def text(markdown):
    return {"type": 10, "content": markdown}


def buttons(links):
    return {"type": 1, "components": [
        {"type": 2, "style": 5, "label": label[:80], "url": url} for label, url in links]}


def build(url, name, desc, facts=None, links=None):
    body = "-# [TS4RLS](%s/)\n## [%s](%s)\n%s" % (SITE, md(name), url, md(desc))
    if facts:
        body += "\n-# " + md(facts)
    comps = [{"type": 9, "components": [text(body)],
              "accessory": {"type": 11, "media": {"url": SITE + "/assets/icon.png"}}}]
    if links:
        comps.append(buttons(links))
    payload = {"component": {"type": 17, "accent_color": ACCENT, "components": comps}}
    js = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\/")
    if len(js.encode("utf-8")) > MAX_BYTES:
        return "<!-- discord:component-embed left out: over %d bytes -->" % MAX_BYTES
    return '<script id="discord:component-embed" type="application/json">%s</script>' % js


GENERIC_LINKS = [("Website", SITE + "/"), ("Releases", SITE + "/releases")]

SPECIAL = {
    "index.html": dict(
        facts="Free · Windows, macOS and Linux · GUI and headless mode",
        links=[("Download", SITE + "/releases"), ("Guides", SITE + "/guides"), ("Source", ENGINE_REPO)]),
    "engine.html": dict(
        facts="Free · open source",
        links=[("Releases", SITE + "/releases"), ("Guides", SITE + "/guides"), ("Source", ENGINE_REPO)]),
    "releases.html": dict(
        facts="Windows, macOS and Linux builds",
        links=[("Home", SITE + "/"), ("Guides", SITE + "/guides")]),
    "guides/index.html": dict(
        facts="Windows · macOS · Linux",
        links=[("Windows", SITE + "/guides/windows"), ("macOS", SITE + "/guides/macos"),
               ("Linux", SITE + "/guides/linux")]),
}


def pages():
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel in SKIP or rel.startswith(("assets/fontawesome", "node_modules", ".")):
            continue
        yield rel, p


def main():
    changed = 0
    for rel, p in pages():
        src = p.read_text(encoding="utf-8")
        if "</head>" not in src:
            continue
        title = html.unescape(re.search(r"<title>(.*?)</title>", src, re.S).group(1)).strip()
        m = re.search(r'<meta name="description" content="(.*?)">', src, re.S)
        desc = html.unescape(m.group(1)).strip() if m else ""
        c = re.search(r'<link rel="canonical" href="(.*?)">', src)
        url = c.group(1) if c else SITE + "/" + rel
        name = title.split(" — ")[0] if rel != "index.html" else "TS4RLS"
        if rel == "index.html":
            desc = "The Sims 4 Random Loading Screen: picks a random image of your own and installs it as your loading screen."
        opts = SPECIAL.get(rel, {})
        tag = build(url, name, desc, opts.get("facts"), opts.get("links", GENERIC_LINKS))
        new = EMBED_RE.sub("", src)
        new = new.replace("</head>", tag + "\n</head>", 1)
        if new != src:
            p.write_text(new, encoding="utf-8", newline="")
            changed += 1
            print("updated", rel)
    print("%d page(s) changed" % changed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
