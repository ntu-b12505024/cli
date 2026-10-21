#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Start a local static server for the BigNaiWa game."""

import os
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8080
ROOT = os.path.dirname(os.path.abspath(__file__))


def main():
    os.chdir(ROOT)
    handler = partial(SimpleHTTPRequestHandler, directory=ROOT)
    with ThreadingHTTPServer(("0.0.0.0", PORT), handler) as httpd:
        print(f"BigNaiWa is running at http://localhost:{PORT}")
        try:
            webbrowser.open(f"http://localhost:{PORT}")
        except Exception:
            pass
        httpd.serve_forever()


if __name__ == "__main__":
    main()
