# server UDP

import socket

# creating a object from socket that support ipv4 and UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 1060
MAX = 65535 #buffer size

server.bind(("127.0.0.1", PORT))
print("Listenning to", server.getsockname())

data, address = server.recvfrom(MAX)

answer = "of course".encode("utf-8")
server.sendto(answer, address)
print("The client at", address, "says", str(data))
