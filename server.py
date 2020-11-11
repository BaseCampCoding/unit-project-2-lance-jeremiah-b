import socket
from _thread import *
import sys
import json

server = "192.168.1.59"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

ship_grids = {0: [], 1: []}

def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            response = ""

            if data:
                if reply == 'ready':
                    response = 'setup start'
                if reply.startswith('['):
                    ship_grids[player] = json.loads(reply)
                    response = 'game start'
                    print(player, ship_grids[player])
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

currentplayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentplayer))
    currentplayer += 1
    print(f'{currentplayer} Players Connected')