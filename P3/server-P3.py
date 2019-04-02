import socket
from Seq import Seq

PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUEST = 5

# Create an empty list to add the messages from the server to the client
response1 = list()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))
serversocket.listen(MAX_OPEN_REQUEST)
print("Socket ready: {}", format(serversocket))


def process_client(cs):
    """Function to read the info of the client and process it"""
    msg = cs.recv(2048).decode("utf-8")

    # Obtain from the client's message a list with the parts of the message
    msg1 = msg.split("\n")
    if msg1[0] == "":
        cs.send(str.encode("Alive"))
        cs.close()
    else:
        for base in msg1[0].upper():
            if base != "A" and base != "C" and base != "G" and base != "T":
                cs.send(str.encode("ERROR"))
                cs.close()
        if len(response1) == 0:
            response1.append("OK")
            sequence = Seq(msg1[0].upper())
            msg1.remove(msg1[0])
            for elem in msg1:
                if elem == "len":
                    response1.append(str(sequence.len()))
                elif elem == "complement":
                    complement = sequence.complement()
                    complement = complement.strbases
                    response1.append(complement)
                elif elem == "reverse":
                    reverse = sequence.reverse()
                    reverse = reverse.strbases
                    response1.append(reverse)
                elif elem == "countA":
                    response1.append(str(sequence.count_bases()))
                elif elem == "countC":
                    response1.append(str(sequence.count_bases()))
                elif elem == "countG":
                    response1.append(str(sequence.count_bases()))
                elif elem == "countT":
                    response1.append(str(sequence.count_bases()))
                elif elem == "percA":
                    response1.append(str(sequence.perc()))
                elif elem == "percC":
                    response1.append(str(sequence.perc()))
                elif elem == "percG":
                    response1.append(str(sequence.perc()))
                elif elem == "percT":
                    response1.append(str(sequence.perc()))
                else:
                    cs.send(str.encode("ERROR"))
                    cs.close()
        # Create an empty message to add the elements of the list of responses
        message = ""
        for element in response1:
            message = message + element + '\n'
        # Send to the client a str, not a list
        cs.send(str.encode(message))
        cs.close()


# -- Main program

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()
    print("Attending client: {}".format(address))

    process_client(clientsocket)