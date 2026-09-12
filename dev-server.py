#!/usr/bin/env python3
"""TS4RLS Website — local dev server.

Serves this folder the way GitHub Pages does. DEV_MODE is forced on by
default: it writes dev-config.js (gitignored, never deployed), which
reveals the `#dev-banner` element the page already carries (hidden by
default) -- same env-banner treatment as TIGHC's Website -- and sets up
window.TS4RLS_DEV so scripts like changelogs.js and versions.js can read
Engine content from the sibling checkout (../Engine) instead of GitHub.
Pass --no-dev-mode to skip all of that, matching production (the banner
then stays hidden, since dev-config.js is never written).
"""
import http.server
import os
import socketserver
import sys

WEB_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(WEB_DIR)
SIBLINGS = {
    "engine": os.path.join(PARENT_DIR, "Engine"),
    "website": WEB_DIR,
}


def parse_args(argv):
    port = 8000
    dev_mode = True
    for a in argv:
        if a == "--no-dev-mode":
            dev_mode = False
        elif a.isdigit():
            port = int(a)
        else:
            print("Unknown option: %s" % a, file=sys.stderr)
            sys.exit(1)
    return port, dev_mode


def write_dev_config(dev_mode, port):
    path = os.path.join(WEB_DIR, "dev-config.js")
    if not dev_mode:
        if os.path.exists(path):
            os.remove(path)
        return
    lines = [
        "// Written by dev-server.py at startup - gitignored, never deployed.",
        "window.TS4RLS_DEV = {",
        "  repos: {",
        "    engine: '/dev-sibling/engine',",
        "    website: '/dev-sibling/website'",
        "  },",
        "  port: %d" % port,
        "};",
        "(function () {",
        "  var banner = document.getElementById('dev-banner');",
        "  var detail = document.getElementById('dev-banner-detail');",
        "  if (detail) {",
        "    detail.textContent = 'TS4RLS Website running on :' + window.TS4RLS_DEV.port +",
        "      ' \\u2014 Engine content served from the local sibling checkout, not GitHub.';",
        "  }",
        "  if (banner) banner.hidden = false;",
        "})();",
        "console.log('[TS4RLS dev mode] Engine/Website content is loaded from local sibling checkouts, not GitHub.');",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


class DevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def translate_path(self, path):
        path = path.split("?", 1)[0].split("#", 1)[0]
        for key, real_dir in SIBLINGS.items():
            prefix = "/dev-sibling/" + key
            if path == prefix or path.startswith(prefix + "/"):
                rest = path[len(prefix):].lstrip("/")
                return os.path.join(real_dir, *rest.split("/")) if rest else real_dir
        translated = super().translate_path(path)
        # Pretty URLs: GitHub Pages serves /foo from foo.html - match that
        # here so /engine, /steam, /changelogs, /releases, etc. all work
        # the same locally as they do in production, instead of 404ing
        # (SimpleHTTPRequestHandler has no extension-optional resolution
        # of its own). Folder-based hubs like /guides and /legal already
        # work via the normal directory + trailing-slash-redirect behavior,
        # since there's no same-named guides.html/legal.html to prefer.
        if not path.endswith("/"):
            with_html = translated + ".html"
            if os.path.isfile(with_html):
                return with_html
        return translated

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def send_error(self, code, message=None, explain=None):
        # GitHub Pages serves 404.html for any missing path in production;
        # SimpleHTTPRequestHandler has no equivalent, so without this a 404
        # locally looks nothing like what visitors actually see.
        if code == 404:
            not_found = os.path.join(WEB_DIR, "404.html")
            if os.path.isfile(not_found):
                with open(not_found, "rb") as f:
                    body = f.read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)


def main():
    port, dev_mode = parse_args(sys.argv[1:])
    write_dev_config(dev_mode, port)

    print("TS4RLS Website running at http://127.0.0.1:%d" % port)
    if dev_mode:
        print("DEV_MODE forced on for this run - Engine content is served")
        print("from %s instead of GitHub." % PARENT_DIR)
        print("Pass --no-dev-mode to fetch from GitHub instead, matching production.")
        if not os.path.isdir(SIBLINGS["engine"]):
            print("Note: %s not found next to Website/ - engine content will 404 locally." % SIBLINGS["engine"])
    else:
        print("DEV_MODE off for this run - Engine content is fetched live from GitHub, same as production.")

    with socketserver.TCPServer(("127.0.0.1", port), DevHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
