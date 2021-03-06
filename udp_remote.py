import random, sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
    interface = sys.argv[2] if len(sys.argv) > 2 else ''
    s.bind((interface, PORT))
    print('Listenig at', s.getsockname())
    while True:
        data, address = s.recvfrom(MAX)
        if a.randint(0, 1):
            print('The client at', address, 'says', repr(data))
            s.sendto(b'Your data was %d bytes' %len(data), address)
        else:
            print('Pretending to drop packet from', address)

elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    hostname = sys.argv[2]
    s.connect((hostname, PORT))
    print('Client socket name is', s.getsockname())
    delay = 0.1
    while True:
        s.send(b'This is another message')
        print('Waiting up to', delay, 'second for a reply')
        s.settimeout(delay)
        try:
            data = s.recv(MAX)
        except socket.timeout:
            delay *= 2    # wait even longer for the next request
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
        except:
            raise         # a real error, so we let the user to see it
        else:
            break         # we are done, snd we can stop it

    print('The server says', repr(data))

else:
    print('usage: udp_remote server [<interface>]')
    print('usage: udp_remote client <host>')
    sys.exit(2)
