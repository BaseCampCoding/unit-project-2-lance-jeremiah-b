import pygame
from pprint import pprint
import network
import json
import db_setup

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

# Not enough ships warning text
ships_text = font.render("Please Place All Ships", True, WHITE)
ships_textRect = ships_text.get_rect()
ships_textRect.center = (925, 600)

### Highscore Info Text

# Highscore header text
hh_text = font.render("---Highscores---", True, WHITE)
hh_textRect = hh_text.get_rect()
hh_textRect.center = (578, 90)

# Highscore #1 text
score_1 = db_setup.display_highscore(0)
hs1_text = font.render(f"1:   {score_1}", True, WHITE)
hs1_textRect = hs1_text.get_rect()
hs1_textRect.center = (578, 130)

# Highscore #2 text
score_2 = db_setup.display_highscore(1)
hs2_text = font.render(f"2:   {score_2}", True, WHITE)
hs2_textRect = hs2_text.get_rect()
hs2_textRect.center = (578, 170)

# Highscore #3 text
score_3 = db_setup.display_highscore(2)
hs3_text = font.render(f"3:   {score_3}", True, WHITE)
hs3_textRect = hs3_text.get_rect()
hs3_textRect.center = (578, 210)

# Highscore #4 text
score_4 = db_setup.display_highscore(3)
hs4_text = font.render(f"4:   {score_4}", True, WHITE)
hs4_textRect = hs4_text.get_rect()
hs4_textRect.center = (578, 250)

# Highscore #5 text
score_5 = db_setup.display_highscore(4)
hs5_text = font.render(f"5:   {score_5}", True, WHITE)
hs5_textRect = hs5_text.get_rect()
hs5_textRect.center = (578, 290)


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

ships_warning = False
ships = 0
max_ships = 17
moves = 0
hits = 0
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
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if game_start and turn:
                if pos[0] <= 450 and pos[1] <= 445:
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    print("Grid coordinates: ", column, row)
                    if enemy_grid[row][column] == 0:
                        grid_coords = f"{row},{column}"
                        print(grid_coords)
                        result = n.send(grid_coords)
                        print("result =", result)
                        # Set that location to result
                        enemy_grid[row][column] = int(result)
                        if int(result) == 1:
                            hits += 1
                        moves += 1
                    pprint(enemy_grid)
            if setup_start:
                if (pos[0] > 700 and pos[0] < 1150) and pos[1] <= 450:
                    # Change the x/y screen coordinates to grid coordinates
                    column = (pos[0] - 700) // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if player_grid[row][column] == 0 and ships < max_ships:
                        player_grid[row][column] = 3
                        ships += 1
                    elif player_grid[row][column] == 3:
                        player_grid[row][column] = 0
                        ships -= 1
                    print("Grid coordinates: ", column, row)
                    pprint(player_grid)
                # Confirm Button
                if (
                    (pos[0] > 838 and pos[0] < 965)
                    and (pos[1] >= 530 and pos[1] <= 565)
                ) and ships == max_ships:
                    ship_grid = json.dumps(player_grid)
                    print("Confirm")
                    # grid_response returns a list: ["game start", 0]
                    grid_response = n.send(ship_grid)
                    grid_response = json.loads(grid_response)
                elif (pos[0] > 838 and pos[0] < 965) and (
                    pos[1] >= 530 and pos[1] <= 565
                ):
                    ships_warning = True

    # update who's turn it is
    check_turn = n.send("turn status")
    if int(check_turn) == player_id:
        turn = True
    else:
        turn = False

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
        if ships_warning:
            screen.blit(ships_text, ships_textRect)
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

    # check if the player has won or lost
    if game_start:
        check_loss = n.send("win status")
        if check_loss != "9":
            break

    if hits == max_ships:
        win = n.send(f"w{player_id}")
        break

# end screen
win = False
lose = False

done = False
while not done:
    check_result = n.send("win status")
    check_result = int(check_result)
    print(check_result)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    if check_result == player_id:
        db_setup.insert_winners_score(moves)
        screen.blit(win_text, win_textRect)
        screen.blit(hh_text, hh_textRect)
        screen.blit(hs1_text, hs1_textRect)
        screen.blit(hs2_text, hs2_textRect)
        screen.blit(hs3_text, hs3_textRect)
        screen.blit(hs4_text, hs4_textRect)
        screen.blit(hs5_text, hs5_textRect)
    else:
        screen.blit(lose_text, lose_textRect)

pygame.quit()