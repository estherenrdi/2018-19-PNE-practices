import socket

IP = "127.0.0.1"
PORT = 8080

msg = """aacctttttttttttttttttttttttttttttggg\nlen\ncountA\ncountG\npercC"""
# msg = """hola\nlen\ncountA\ncountG\npercC"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode(msg))

# Receive the servers response and print it
response = s.recv(2048).decode()
print("Response: {}".format(response))
s.close()
