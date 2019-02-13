import socket
# Create a socket for communicating with the server
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 8089
    IP = "212.128.253.81"
    s.connect((IP, PORT))
    msg1 = input("Please, enter here a sequence : ")

    s.send(str.encode(msg1))

    msg = s.recv(2048).decode("utf-8")
    print("This is the messege from the server")
    print(msg)

    s.close()