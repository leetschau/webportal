from http.server import SimpleHTTPRequestHandler, HTTPServer
params = []


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location',  params[0] + self.path)
        self.end_headers()


def main(target, port):
    server_address = ("", port)
    params.append(target)
    httpd = HTTPServer(server_address, MyHandler)
    print("serving at port %s" % port)
    httpd.serve_forever()
