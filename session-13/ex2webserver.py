import http.server
import socketserver

port = 8009

class testhandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        print("GET received")
        print("Request line " + self.requestline)
        print("Command " + self.command)
        print("Resource " + self.path)


        if self.path == "/":
            with open('index.html') as f:
                contents = f.read()
        elif self.path != "/":
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
