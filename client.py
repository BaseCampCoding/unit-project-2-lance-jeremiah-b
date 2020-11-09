import pygame
from classes import Grid_block

# Network stuff (later)
# Pull ship classes from database table
# Pygame screen
# Grid setup
# Choose ship locations
# Confirm locations and generate dictionary

pygame.init()

screen_x, screen_y = (1000, 600)

win = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Battleship")

game_area = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
]

run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
