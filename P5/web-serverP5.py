import http.server
import socketserver

port = 8001

class testhandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        print("GET received")
        print("Request line " + self.requestline)
        print("Command " + self.command)
        print("Resource " + self.path)


        if self.path == "/":
            with open('index.html') as f:
                contents = f.read()
        elif self.path == "/blue":
            with open('blue.html') as f:
                contents = f.read()
        elif self.path == "/pink":
            with open('pink.html') as f:
                contents = f.read()
        else:
            with open('error.html') as f:
                contents = f.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html")

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

handler = testhandler

with socketserver.TCPServer(("", port), handler) as http:
    print("Serving at port {}".format(port))

    http.serve_forever()
