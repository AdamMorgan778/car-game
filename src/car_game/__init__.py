"""Serve the car game locally so it can be played in a browser."""

import argparse
import functools
import http.server
import webbrowser
from pathlib import Path

# The game lives in docs/ so GitHub Pages can serve the same file.
STATIC_DIR = Path(__file__).resolve().parents[2] / "docs"


def main() -> None:
    parser = argparse.ArgumentParser(description="Play the car game in your browser.")
    parser.add_argument("--port", type=int, default=8000, help="port to serve on (default 8000)")
    parser.add_argument("--no-browser", action="store_true", help="don't open a browser tab")
    args = parser.parse_args()

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=STATIC_DIR)
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        url = f"http://127.0.0.1:{server.server_address[1]}/"
        print(f"Car game running at {url}  (Ctrl+C to stop)")
        if not args.no_browser:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nBye!")
