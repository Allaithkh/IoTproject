import socket
import threading

PORT = 4033
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(ADDR)

def handle_client(conn, addr):
    while True:
        data = conn.recv(4096)
        msge =data.hex()
        f = open("logs.txt", "a")
        f.write(msge + '\n')
        if (len(data) == 17):
            print( f"received data from {addr}:", data)
            ACK = 1
            ack = ACK.to_bytes(1, byteorder= 'big', signed=True )
            print("we send {}".format(ack))
            conn.sendall(ack)
        elif (len(data)>35):
            print(  f"received data from {addr}:", msge)
            resp = data[9]
            print (resp)
            res = resp.to_bytes(4, byteorder= 'big', signed=True )
            print("we send {}".format(res))
            conn.sendall(res)
        else:
            continue
        if not conn:
            conn.close()
        f.close()
    return msg

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS {addr}] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
