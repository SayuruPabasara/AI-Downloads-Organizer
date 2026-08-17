from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path != "/download":

            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers["Content-Length"])

        body = self.rfile.read(content_length)

        data = json.loads(body)

        print("\n===== DOWNLOAD RECEIVED =====")
        print(json.dumps(data, indent=4))
        print("=============================\n")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = {
            "status": "received"
        }

        self.wfile.write(json.dumps(response).encode())


server = HTTPServer(
    ("127.0.0.1", 8765),
    RequestHandler
)

print("Python server running on http://127.0.0.1:8765")

server.serve_forever()

