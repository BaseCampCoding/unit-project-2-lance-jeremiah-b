import pygame
from classes import Grid_block
from pprint import pprint

# Network stuff (later)
# Pull ship classes from database table
# Pygame screen
# Grid setup
# Choose ship locations
# Confirm locations and generate dictionary

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
MARGIN = 5

# Initialize font module
pygame.font.init()

# font object
font = pygame.font.Font('freesansbold.ttf', 32) 

# Player text
player_text = font.render('Your Ships', True, WHITE)
player_textRect = player_text.get_rect()
player_textRect.center = (925, 480)

# Enemey text
enemy_text = font.render('Enemy Ships', True, WHITE)
enemy_textRect = enemy_text.get_rect()
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
done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] <= 450 and pos[1] <= 450:
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                player_grid[row][column] = 1
                print("Grid coordinates: ", column, row)
                # pprint(player_grid)
                # pprint(enemy_grid)


    # Set the screen background
    screen.fill(BLACK)

    # Display text
    screen.blit(player_text, player_textRect)
    screen.blit(enemy_text, enemy_textRect)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if player_grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, 
                [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT], 4)

    for row in range(10):
        for column in range(10):
            color = WHITE
            if enemy_grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, 
                [700 + ((MARGIN + WIDTH) * column + MARGIN), (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT], 4)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()