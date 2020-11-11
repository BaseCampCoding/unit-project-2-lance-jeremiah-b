import socket
from _thread import *
import sys
import json

server = "192.168.1.59"
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

ship_grids = {0: [], 1: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}

def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            response = ""

            
            if reply == 'ready':
                response = 'setup start'
            elif reply.startswith('['):
                ship_grids[player] = json.loads(reply)
                response = 'game start'
            else:
                x, y = reply.split(',')
                x, y = int(x), int(y)
                print('coords =', x, y)
                if player == 0:
                    grid = ship_grids[1]
                    print(grid)
                    block = grid[x][y]
                    print('block:', block)
                    if block == 3:
                        response = "1"
                    else:
                        response = "2"
                elif player == 1:
                    grid = ship_grids[0]
                    block = grid[x][y]
                    if block == 3:
                        response = "1"
                    else:
                        response = "2"
                else:
                    response = "9"
                
            print("Received: ", reply, "From", player)
            print("Sending : ", response, "To", player)

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