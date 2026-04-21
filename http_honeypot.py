from http.server import BaseHTTPRequestHandler, HTTPServer
from logger.logger import log_event

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]

        log_event("HTTP", ip, self.path)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Welcome to secure server")

def start_http_honeypot(port=8080):
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"[HTTP Honeypot] Running on port {port}")
    server.serve_forever()
