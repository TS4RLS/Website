#!/bin/bash
# TS4RLS Website - Local dev server
# Usage: ./dev-server.sh [port] [--no-dev-mode]
#   port            default: 8000
#   --no-dev-mode   fetch Engine content from GitHub instead of the local
#                   sibling checkout (production behavior) for this run
#
# DEV_MODE is forced ON for every run of this script, regardless of what
# was passed last time - that's what reveals the dev-mode banner and (once
# there's a script that reads it) makes local content come from the
# sibling checkout next to this one (../Engine) instead of GitHub, so
# local edits show up here without pushing first. Pass --no-dev-mode to
# test the site as it behaves in production instead.
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="$(command -v python3 || command -v python)"
if [ -z "$PYTHON" ]; then
    echo "Python 3 is required to run dev-server.py" >&2
    exit 1
fi

exec "$PYTHON" "$DIR/dev-server.py" "$@"
