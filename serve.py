"""Dev server for ANIME STICK HERO — serves files with Cache-Control: no-store.

Usage: python serve.py [port]   (default 8321)
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # quiet


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8321
server = ThreadingHTTPServer(("127.0.0.1", port), NoCacheHandler)
print(f"serving on http://127.0.0.1:{port}/ (no-store)")
server.serve_forever()
