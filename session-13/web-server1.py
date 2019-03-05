import http.server
import socketserver

port = 8000

class testhandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        print("GET received")
        print("Request line" + self.requestline)
        print("Command" + self.command)
        print("Resource" + self.path)

        content = "Im always happy"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content.lenght", len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return

handler = testhandler

with socketserver.TCPServer(("", port), handler) as http:
    print("Serving at port {}".format(port))

    http.serve_forever()
