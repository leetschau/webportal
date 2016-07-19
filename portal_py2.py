import SimpleHTTPServer
import SocketServer


class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', 'https://www.newfairs.com%s' % self.path)
        self.end_headers()

PORT = 8000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print("serving at port %s" % PORT)
handler.serve_forever()
