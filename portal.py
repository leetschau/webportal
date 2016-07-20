from http.server import SimpleHTTPRequestHandler, HTTPServer

TARGET = 'https://www.newfairs.com'
PORT = 7000


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', TARGET + self.path)
        self.end_headers()


def main():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, MyHandler)
    print("serving at port %s" % PORT)
    httpd.serve_forever()
