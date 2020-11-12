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

# 9 is a None value
turn = "9"
fire_coords = {0: [], 1: []}
player_won = "9"
currentplayer = 0

def threaded_client(conn, player):
    global currentplayer
    global turn
    global ship_grids
    global fire_coords
    global player_won
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
                response = player_won
                print("win status", player_won)
            elif reply.startswith('w'):
                player_won = reply[1]
                print("startswith", player_won)
                response = player_won
            elif reply == 'fire status':
                if player == 0:
                    response = str(fire_coords[1])
                elif player == 1:
                    response = str(fire_coords[0])
            else:
                x, y = reply.split(',')
                x, y = int(x), int(y)
                print('coords =', x, y)
                if player == 0:
                    grid = ship_grids[1]
                    block = grid[x][y]
                    if block == 3:
                        turn = 1
                        response = "1"
                    else:
                        response = "2"
                        turn = 1
                    fire_coords[0] = [x, y, int(response)]
                elif player == 1:
                    grid = ship_grids[0]
                    block = grid[x][y]
                    if block == 3:
                        response = "1"
                        turn = 0
                    else:
                        response = "2"
                        turn = 0
                    fire_coords[1] = [x, y, int(response)]
                else:
                    response = "9"
                
            # print("Received: ", reply, "From", player)
            # print("Sending : ", response, "To", player)

            conn.sendall(str.encode(response))
        except:
            break

    print("Lost connection")
    conn.close()
    currentplayer -= 1

# Listens for connections
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentplayer))
    currentplayer += 1
    print(f'{currentplayer} Players Connected')