## Description and Motivation

In this project, we wanted to build a Battleship game inside of Python.
Our twist will be making the game capable of being played on two different computers using Python.This way you could having a proper game of Battleship with multiple grids for your board and the enemy's board.

## Extras
- Special attacks
Special attacks will be able to hit multiple grids with different patterns, and some will bypass various defensive mearsures.
- Defensive measures
For now, only one ship has a defensive measure. This defensive measure will allow that ship to survive a special attack that would otherwise destroy it.
- Adding different kinds of ships
A varity of spcial ships will be added to give the player more unique choices to make during set up
- If larger ships are added, possibly expand game area grid.
For example, if we add a 2X8 ship, then we could expand the grid as necessary to fit all the ships on the board.

## Prior Art

There are many variations of the classic Battleship game. We wanted to make a version that works with python, and allows you to play on two different computers. 

A Battleship game that is similar to what we envisioned is "Electronic Battleship: Advanced Mission". This game has special weapons that can attack multiple grids, and they even have a scanning system used to approximate the location of an enemy ship. Idealy, we would not only have special attacks and scanning capabilties, but we would have also have defensive measures added to the mix. Our main focus, however, is to make the game multiplayer ready first. Extra ablilties and such wil be added if we are able to establish a solid network for the multiplayer experience.

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

## Students

- Jeremiah Bass
- Lance Easley

## GitHub Repository

https://https://github.com/BaseCampCoding/unit-project-2-lance-jeremiah-b
