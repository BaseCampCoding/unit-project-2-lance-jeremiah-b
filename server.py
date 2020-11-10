import socket
from _thread import *
import sys

server = "192.168.1.59"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            response = ""

            if data:
                if reply == 'yeet':
                    response = 'skeet'
                else:
                    response = 'that was not a yeet'
                print("Received: ", reply)
                print("Sending : ", response)
            else:
                print("Disconnected")
                break
            

            conn.sendall(str.encode(response))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))