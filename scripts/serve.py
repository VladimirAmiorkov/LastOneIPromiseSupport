#!/usr/bin/env python3
"""Serve website/ locally the way GitHub Pages does, for testing.

- Pages are served under /LastOneIPromiseSupport/ (the project-site base path).
- Missing pages return website/404.html with status 404.

Usage: python3 scripts/serve.py [port]   (default port 8000)
Then open http://localhost:8000/LastOneIPromiseSupport/
"""

import http.server
import sys
from functools import partial
from pathlib import Path

BASE_PATH = "/LastOneIPromiseSupport"
SITE_DIR = Path(__file__).resolve().parent.parent / "website"


class PagesHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", BASE_PATH + "/")
            self.end_headers()
            return
        super().do_GET()

    def translate_path(self, path):
        # Strip the GitHub Pages base path so /LastOneIPromiseSupport/x maps to website/x.
        if path == BASE_PATH or path.startswith(BASE_PATH + "/"):
            path = path[len(BASE_PATH):] or "/"
        else:
            path = "/__not_found__"
        return super().translate_path(path)

    def send_error(self, code, message=None, explain=None):
        page = SITE_DIR / "404.html"
        if code == 404 and page.exists():
            body = page.read_bytes()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    handler = partial(PagesHandler, directory=str(SITE_DIR))
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as server:
        print(f"Serving {SITE_DIR} at http://localhost:{port}{BASE_PATH}/  (Ctrl+C to stop)")
        server.serve_forever()


if __name__ == "__main__":
    main()
