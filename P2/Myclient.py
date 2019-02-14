import socket
# Create a socket for communicating with the server
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8086
    IP = "212.128.253.81"
    s.connect((IP, PORT))
    from Seq import Seq
    seq1 = Seq(input("Please, enter here your sequence : "))
    seq2 = Seq(seq1.reverse())
    seq3 = Seq(seq2.complement())

    s.send(str.encode(seq3.strbases))

    msg = s.recv(2048).decode("utf-8")
    print("This is the messege from the server")
    print(msg)

    s.close()