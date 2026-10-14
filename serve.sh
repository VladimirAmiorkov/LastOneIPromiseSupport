#!/bin/sh
# Serve the website locally (like GitHub Pages) and open it in the browser.
# Usage: ./serve.sh [port]   (default 8000) — Ctrl+C to stop.
cd "$(dirname "$0")" || exit 1
PORT="${1:-8000}"
(sleep 1 && open "http://localhost:$PORT/LastOneIPromiseSupport/") &
exec python3 scripts/serve.py "$PORT"
