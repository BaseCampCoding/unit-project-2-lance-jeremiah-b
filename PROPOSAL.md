## Core User Workflows

- **Game Setup Logic:** We need to create a database that will store the different ship's information, like the size of each ship.
Then, we can generate the game area grids for the players to start adding their ship positions.
Once the player confirms their ship positions, the program will generate a dictionary to represent that grid.

- **Networking:** Create a server-client style network for the game. 
Two players should be able to connect, send their grid dictionaries to the server, and then take turns firing at the oppenent's grid.
After every turn, the server should send the player's moves to both clients in order to update their grids.

- **High Scores:** Once a game ends, the game will add the number of moves to a highscore table if the player won.
The table will hold the top 5 scores, so if a sixth score is added, the table will drop the lowest score.

## Daily Goals

### Tuesday: Create a database and a table to hold the ship information.
Generate a grid that lets the player place their ships where they want.
Once the player confirms their positions, the game generates a dictionary to represent the grid.

### Wednesday: Create the server-client logic to have two clients play against each other.
The clients should connect to the server, then the server should wait for both players to send their game area dictionaries.
Once the dictionaries are recieved, the game should start and each player will then take turns firing at each other.

### Thursday: Set up highscore table and finalize pygame graphics.
We should create the logic to add highscores to the table and have only the top 5 scores in that table.
The graphics of the game may be sloppy from the past two days, so this will be a clean-up day to make the game look nice.