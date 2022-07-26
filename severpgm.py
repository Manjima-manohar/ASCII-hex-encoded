import http.server
import HTTPServer
import BasedHTTPRequestHandler
import base64
class requestHandler(BasedHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text')
        self.end_headers()
        payload = '0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38'
        base64_bytes = payload.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        self.wfile.write(bytes(payload, "utf8"))
    
PORT = 7878

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
   
    httpd.serve_forever()
    



