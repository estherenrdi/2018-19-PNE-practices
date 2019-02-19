# A sockect is an object for communicate
# Programming our first client
import socket
# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("socket created")

PORT = 8082
IP = "212.128.253.64"
s.connect((IP, PORT))

s.send(str.encode("HOLA ME LLAMO IRENE"))

msg = s.recv(2048).decode("utf-8")
print("This is the messege from the server")
print(msg)

s.close()

print("The end")

