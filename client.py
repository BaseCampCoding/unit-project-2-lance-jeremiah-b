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

# Player text
player_text = font.render("Your Ships", True, WHITE)
player_textRect = player_text.get_rect()
player_textRect.center = (925, 480)

# Confirm text
confirm_text = font.render("Confirm", True, BLACK, RED)
confirm_textRect = player_text.get_rect()
confirm_textRect.center = (925, 550)

# Enemey text
enemy_text = font.render("Enemy Ships", True, WHITE)
enemy_textRect = confirm_text.get_rect()
enemy_textRect.center = (230, 480)

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
done = False
while not done:
    if not setup_start:
        response = n.send("ready")
        print(response)
        if response == "setup start":
            print("Should be true")
            setup_start = True
    if game_start:
        setup_start = False

    # Set the screen background
    screen.fill(BLACK)

    if setup_start:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                if game_start:
                    if pos[0] <= 450 and pos[1] <= 450:
                        # Change the x/y screen coordinates to grid coordinates
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        # Set that location to one
                        if enemy_grid[row][column] == 0:
                            enemy_grid[row][column] = 1
                        print("Grid coordinates: ", column, row)
                        pprint(player_grid)
                        pprint(enemy_grid)
                if setup_start:
                    if (pos[0] > 700 and pos[0] < 1150) and pos[1] <= 450:
                        # Change the x/y screen coordinates to grid coordinates
                        column = (pos[0] - 700) // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        # Set that location to one
                        player_grid[row][column] = 3
                        print("Grid coordinates: ", column, row)
                        pprint(player_grid)
                    # Confirm Button
                    if (pos[0] > 838 and pos[0] < 965) and (
                        pos[1] >= 530 and pos[1] <= 565
                    ):
                        ship_grid = json.dumps(player_grid)
                        print("Confirm")
                        n.send(ship_grid)

    # Display text
    screen.blit(player_text, player_textRect)
    screen.blit(enemy_text, enemy_textRect)
    screen.blit(confirm_text, confirm_textRect)

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