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

grid = [
    [Grid_block(0, 0, 20, 20), Grid_block(20, 0, 20, 20), Grid_block(40, 0, 20, 20), Grid_block(60, 0, 20, 20), Grid_block(80, 0, 20, 20), 
    Grid_block(100, 0, 20, 20), Grid_block(120, 0, 20, 20), Grid_block(140, 0, 20, 20), Grid_block(160, 0, 20, 20), Grid_block(180, 0, 20, 20), ]

    [Grid_block(0, 20, 20, 20), Grid_block(20, 20, 20, 20), Grid_block(40, 20, 20, 20), Grid_block(60, 20, 20, 20), Grid_block(80, 20, 20, 20), 
    Grid_block(100, 20, 20, 20), Grid_block(120, 20, 20, 20), Grid_block(140, 20, 20, 20), Grid_block(160, 20, 20, 20), Grid_block(180, 20, 20, 20), ]

    [Grid_block(0, 40, 20, 20), Grid_block(20, 40, 20, 20), Grid_block(40, 40, 20, 20), Grid_block(60, 40, 20, 20), Grid_block(80, 40, 20, 20), 
    Grid_block(100, 40, 20, 20), Grid_block(120, 40, 20, 20), Grid_block(140, 40, 20, 20), Grid_block(160, 40, 20, 20), Grid_block(180, 40, 20, 20), ]

    [Grid_block(0, 60, 20, 20), Grid_block(20, 60, 20, 20), Grid_block(40, 60, 20, 20), Grid_block(60, 60, 20, 20), Grid_block(80, 60, 20, 20), 
    Grid_block(100, 60, 20, 20), Grid_block(120, 60, 20, 20), Grid_block(140, 60, 20, 20), Grid_block(160, 60, 20, 20), Grid_block(180, 60, 20, 20), ]

    [Grid_block(0, 80, 20, 20), Grid_block(20, 80, 20, 20), Grid_block(40, 80, 20, 20), Grid_block(60, 80, 20, 20), Grid_block(80, 80, 20, 20), 
    Grid_block(100, 80, 20, 20), Grid_block(120, 80, 20, 20), Grid_block(140, 80, 20, 20), Grid_block(160, 80, 20, 20), Grid_block(180, 80, 20, 20), ]

    [Grid_block(0, 100, 20, 20), Grid_block(20, 100, 20, 20), Grid_block(40, 100, 20, 20), Grid_block(60, 100, 20, 20), Grid_block(80, 100, 20, 20), 
    Grid_block(100, 100, 20, 20), Grid_block(120, 100, 20, 20), Grid_block(140, 100, 20, 20), Grid_block(160, 100, 20, 20), Grid_block(180, 100, 20, 20), ]

    [Grid_block(0, 120, 20, 20), Grid_block(20, 120, 20, 20), Grid_block(40, 120, 20, 20), Grid_block(60, 120, 20, 20), Grid_block(80, 120, 20, 20), 
    Grid_block(100, 120, 20, 20), Grid_block(120, 120, 20, 20), Grid_block(140, 120, 20, 20), Grid_block(160, 120, 20, 20), Grid_block(180, 120, 20, 20), ]

    [Grid_block(0, 0, 20, 20), Grid_block(20, 0, 20, 20), Grid_block(40, 0, 20, 20), Grid_block(60, 0, 20, 20), Grid_block(80, 0, 20, 20), 
    Grid_block(100, 0, 20, 20), Grid_block(120, 0, 20, 20), Grid_block(140, 0, 20, 20), Grid_block(160, 0, 20, 20), Grid_block(180, 0, 20, 20), ]

    [Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), 
    Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), ]
    
    [Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), 
    Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), Grid_block(0, 0, 20, 20), ]
]

run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
