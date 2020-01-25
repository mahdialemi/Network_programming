import socket, sys, random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 1060
max = 65535

if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
    interface = sys.argv[2] if len(sys.argv) == 3 else ''
    s.bind((interface, port))
    print('Listening to', s.getsockname())
    flag = 0
    while True:
        if flag == 0:
            flag = 1
        data, address = s.recvfrom(max)
        print('--->', data, '\n')
        answer_text = input('>> ')
        answer_text = bytes(answer_text, 'utf-8')
        s.sendto(answer_text, address)

elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    hostname = sys.argv[2]
    s.connect((hostname, port))
    flag = 0
    while True:
        if flag == 0:
            flag = 1
        request_text = input(">> ")
        request_text = bytes(request_text, 'utf-8')
        s.send(request_text)
        data = s.recv(max)
        print('--->', data, '\n')

else:
    print('usage ...')