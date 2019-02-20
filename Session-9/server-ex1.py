import socket
import termcolor
PORT = 8089
IP = "212.128.253.76"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # reading the message from the client

    msg = cs.recv(2048).decode("utf-8")
    termcolor.cprint(msg, 'red')
    cs.send(str.encode(msg))
    cs.close()
    print("Message from the client  : {} ".format(msg))




# CREATE A SOCKET TO CONNECT TO THE CLIENTS

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready : {}".format(serversocket))

while True:

    print("Waiting for connection at : {}, {}".format(IP, PORT))

    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Assisting the client : {}".format(address))

    process_client(clientsocket)
    # -- Close the socket
    clientsocket.close()
