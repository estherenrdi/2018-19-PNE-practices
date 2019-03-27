import http.server
import socketserver
import termcolor
from Seq import Seq
PORT = 8000


def correct_sequence(seq):
    nucleo_acid = ['A', 'T', 'C', 'G']
    for letter in seq:
        if letter not in nucleo_acid:
            return False
    return True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path

        # PRINTING THE REQUEST LINE

        termcolor.cprint(self.path, 'green')

        if path == "/":
            f = open('P6-FORM.html', 'r')
            content = f.read()

        elif (path[:4] == '/Seq' and '=' in path) :
            msg = path.split('&')
            seq = (msg[0].split('=')[1]).upper()
            if correct_sequence(seq):
                content = ("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>SEQUENCE RESPONSE:</title>
                            </head>
                            <body style="background-color: light-green;">
                                <h1>Sequence information:</h1>
                                <p>{}</p>
                                <br>
                                <p>{}</p>
                                <br>
                                <p>{}</p>
                                <br>
                                <a href="/">Main page</a>
                            </body>
                            </html.>""")

                s = ""
                l = ""
                mode = ""

                s += 'Sequence:' + seq

                seq = Seq(seq)

                for i in range(len(msg)):

                    if "chk=on" in msg[i]:
                        lent = seq.len()
                        l += "Len:" + str(lent)
                    elif "base" in msg[i]:
                        base = msg[i].split("=")

                        b = base[1]

                    elif "operation" in msg[i]:
                        oper = msg[i].split("=")
                        if oper[1] == "count":
                            counter = seq.count_bases()
                            count_base = counter[b]
                            mode += "Base {} appears {} times in the sequence".format(b, str(count_base))
                            print(mode)
                        elif oper[1] == "perc":
                            dict_relation = {'A': 1, 'T': 2, 'C': 3, 'G': 4}
                            number = dict_relation[b]
                            perc = seq.perc()
                            myperc = perc[number]
                            mode += "The percentage for base {} is: {}".format(b, str(myperc))
                            print(mode)
                content = content.format(s, l, mode)



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
