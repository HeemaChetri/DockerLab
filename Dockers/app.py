
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from Kubernetes Rolling Update!")

server = HTTPServer(("0.0.0.0", 5000), MyHandler)

print("Python application running on port 5000")

server.serve_forever()
