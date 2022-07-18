import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name =  "192.168.1.147" # sys.argv[1]
server_address = (server_name, 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
ACK = hex('01')
print(type(ACK))
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(48)
            print('received {!r}'.format(data))
            if ACK:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()