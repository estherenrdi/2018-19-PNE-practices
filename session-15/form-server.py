import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        var = self.path.split('?')

        # PRINTING THE REQUEST LINE

        termcolor.cprint(self.requestline, 'green')

        if var[0] == "/":
            f = open('ex1.html', 'r')
            content = f.read()
        elif var[0] == "/echo":
            var1 = var[1].split('=')
            content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Echo message</title>
</head>
<body>"""
            content += "<p>{}</p>".format(var1[1])
            content += """<a href="/">[Main page]</a>
</body>
</html>"""

        else:
            f = open('error.html', 'r')
            content = f.read()


        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        # --- Sending the body of the response message
        self.wfile.write(str.encode(content))

# --- Now we have to write the main programe
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:


    print("serving at port {}".format(PORT))

    try:

        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
