import pygame


class ship_classes:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width


class Grid_block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.color = (0,0,0)

    def miss(self):
        self.color = (255, 255, 255)

    def hit(self):
        self.color = (255, 0, 0)

    def occupied(self):
        self.color = (180, 0, 0)

    def draw(self,win):
        #Call this method to draw the block on the screen
        pygame.draw.rect(win, self.color, (self.x,self.y,self.w,self.h))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.w:
            if pos[1] > self.y and pos[1] < self.y + self.h:
                return True
        return False

