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

ship_grids = {0: [], 1: []}

turn = "9"
enemy_coords = '["",""]'

def threaded_client(conn, player):
    global turn
    checked_grids = False
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            response = ""

            # sends setup keyword, along with player_id number
            if reply == 'ready':
                response = f'["setup start", {player}]'

            elif reply.startswith('['):
                ship_grids[player] = json.loads(reply)
                response = '["game start", 0]'
            
            elif reply == 'turn status':
                if (ship_grids[0] != [] and ship_grids[1] != []) and not checked_grids:
                    turn = 0
                    checked_grids = True
                response = str(turn)
            elif reply == 'win status':
                pass
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
                        turn = 1
                    else:
                        response = "2"
                        turn = 1
                elif player == 1:
                    grid = ship_grids[0]
                    block = grid[x][y]
                    if block == 3:
                        response = "1"
                        turn = 0
                    else:
                        response = "2"
                        turn = 0
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