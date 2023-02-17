from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from http.server import HTTPServer
import json

class Consumer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse URL.
        parsed_url = urlparse(self.path)
        route: str = parsed_url.path
        query: dict = parse_qs(parsed_url.query)  # each entry is a list.

        # Response values.
        r_code: int = 200
        r_type: str = "application/json"
        r_content: str = ""

        try:
            if route == "/":
                # Do work
                print("Working...")

            # Fallback, handle 404s.
            else:
                r_code = 404
                r_content = json.dumps({
                    "error": "No route found matching {0}".format(route)
                })

            # Send the response.
            self.send_response(r_code)
            self.send_header("Content-Type", r_type)
            self.end_headers()
            self.wfile.write(r_content.encode("utf8"))

        # Handle server errors.
        except Exception as exc:
            self.send_error(500, message="Server Error.", explain=str(exc))


if __name__ == "__main__":
    try:
        print("Running web server...")
        httpd = HTTPServer(("localhost", 8000), Consumer)
        httpd.serve_forever()
    except KeyboardInterrupt:
            print("Bye.")