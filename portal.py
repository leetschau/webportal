from http.server import SimpleHTTPRequestHandler, HTTPServer

ROOT = 'https://www.newfairs.com'
PORT = 8000


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location',  ROOT + self.path)
        self.end_headers()

server_address = ("", PORT)
httpd = HTTPServer(server_address, MyHandler)
print("serving at port %s" % PORT)
httpd.serve_forever()
