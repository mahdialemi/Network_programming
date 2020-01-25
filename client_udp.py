#client UDP

import socket

# creating a object from socket that support ipv4 and UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 1060
MAX = 65535 #buffer size

request = input(">>>")
request = request.encode("utf-8")
client.sendto(request, ("127.0.0.1", PORT))

print("address after sending: ", client.getsockname())

data, address = client.recvfrom(MAX)
