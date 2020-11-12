import pygame
from pprint import pprint
import network
import json

n = network.Network()

# 0 is empty sea
# 1 is a hit
# 2 is a miss
# 3 is a ship

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SEA_BLUE = (0, 175, 255)
GREY = (128, 128, 128)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
MARGIN = 5

# Initialize font module
pygame.font.init()

# font object
font = pygame.font.Font("freesansbold.ttf", 32)
l_font = pygame.font.Font("freesansbold.ttf", 48)

# Player text
player_text = font.render("Your Ships", True, WHITE)
player_textRect = player_text.get_rect()
player_textRect.center = (925, 480)

# Enemy text
enemy_text = font.render("Enemy Ships", True, WHITE)
enemy_textRect = enemy_text.get_rect()
enemy_textRect.center = (230, 480)

# Confirm text
confirm_text = font.render("Confirm", True, BLACK, RED)
confirm_textRect = player_text.get_rect()
confirm_textRect.center = (925, 550)

# Turn text
turn_text = font.render("Your Turn", True, WHITE)
turn_textRect = turn_text.get_rect()
turn_textRect.center = (230, 550)

# Win text
win_text = l_font.render("You Win", True, WHITE)
win_textRect = win_text.get_rect()
win_textRect.center = (575, 40)

# Lose text
lose_text = l_font.render("You Lose", True, WHITE)
lose_textRect = lose_text.get_rect()
lose_textRect.center = (575, 40)

# Create a 2 dimensional array
player_grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    player_grid.append([])
    for column in range(10):
        player_grid[row].append(0)  # Append a cell
pprint(player_grid)

enemy_grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    enemy_grid.append([])
    for column in range(10):
        enemy_grid[row].append(0)  # Append a cell
pprint(enemy_grid)

pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1155, 700]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Battleship")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
setup_start = False
game_start = False
grid_response = "  "
turn = False
# ready response returns a list: ["setup start, {player_id}"]
response = n.send("ready")
response = json.loads(response)
print(response)
player_id = response[1]
if response[0] == "setup start":
    setup_start = True

moves = 0
done = False
while not done:
    if grid_response[0] == "game start":
        setup_start = False
        game_start = True
    # Set the screen background
    screen.fill(BLACK)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if game_start and turn:
                if pos[0] <= 450 and pos[1] <= 450:
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    print("Grid coordinates: ", column, row)
                    grid_coords = f"{row},{column}"
                    print(grid_coords)
                    result = n.send(grid_coords)
                    print('result =', result)
                    # Set that location to one
                    if enemy_grid[row][column] == 0:
                        enemy_grid[row][column] = int(result)
                        moves += 1
                    pprint(enemy_grid)
            if setup_start:
                ships = 0
                if (pos[0] > 700 and pos[0] < 1150) and pos[1] <= 450:
                    # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0] - 700) // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_grid[row][column] == 0 and ships <= 15:
                        player_grid[row][column] = 3
                        ships += 1
                    elif player_grid[row][column] == 3:
                        player_grid[row][column] = 0
                        ships -= 1
                    print("Grid coordinates: ", column, row)
                    pprint(player_grid)
                # Confirm Button
                if (pos[0] > 838 and pos[0] < 965) and (
                    pos[1] >= 530 and pos[1] <= 565
                ):
                    ship_grid = json.dumps(player_grid)
                    print("Confirm")
                    # grid_response returns a list: ["game start", 0]
                    grid_response = n.send(ship_grid)
                    grid_response = json.loads(grid_response)
    
    # update who's turn it is
    check_turn = n.send("turn status")
    if int(check_turn) == player_id:
        turn = True
    else:
        turn = False

    # check if the player has won or lost
    # check_win = n.send("win status")

    # check if the enemy has fired and where
    check_fire = n.send("fire status")
    check_fire = json.loads(check_fire)
    if check_fire:
        print(check_fire)
        x, y, r = check_fire
        player_grid[x][y] = r
        pprint(player_grid)

    # Display text
    screen.blit(player_text, player_textRect)
    screen.blit(enemy_text, enemy_textRect)
    if setup_start:
        screen.blit(confirm_text, confirm_textRect)
    if turn:
        screen.blit(turn_text, turn_textRect)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = SEA_BLUE
            if enemy_grid[row][column] == 1:
                color = RED
            elif enemy_grid[row][column] == 2:
                color = WHITE
            pygame.draw.rect(
                screen,
                color,
                [
                    (MARGIN + WIDTH) * column + MARGIN,
                    (MARGIN + HEIGHT) * row + MARGIN,
                    WIDTH,
                    HEIGHT,
                ],
                4,
            )

    for row in range(10):
        for column in range(10):
            color = SEA_BLUE
            if player_grid[row][column] == 3:
                color = GREY
            elif player_grid[row][column] == 2:
                color = WHITE
            elif player_grid[row][column] == 1:
                color = RED
            pygame.draw.rect(
                screen,
                color,
                [
                    700 + ((MARGIN + WIDTH) * column + MARGIN),
                    (MARGIN + HEIGHT) * row + MARGIN,
                    WIDTH,
                    HEIGHT,
                ],
                4,
            )

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()