# Unit Project Week 10, By Jeremiah and Lance

## Battleship, But in Python
Our program is a recreation of the popular board game "Battleship" in python.
The game supports two computers that can be placed back to back for maximum immersion.

## Overview
The program runs in a client/server format. 
Once a server is running, two clients can connect to the server.
When a client connects, the player is prompted to create their ship layout grid.
Once both clients have confirmed their grids, the game starts, and the first connected client goes first.
When a player hits all of their opponent's ships, they recieve the win screen and the lose screen is displayed on the opponent's screen.

## Features
- Two player support
- Turn based game
- GUI

## Usage
To start the game, run "server.py", then run two instances of "client.py"

### File Purposes
**server.py**: This file runs the server for the game.
You can ignore the terminal once it pops up.

**client.py**: The client is what allows the player to interact and play the game with another person.

**db_setup.py**: This file sets up the database that stores the highscore table.

**network.py**: Holds the class "Network" for the client to use and communicate with the server.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to 
discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
