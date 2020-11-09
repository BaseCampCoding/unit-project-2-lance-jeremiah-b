import pygame

class ship_classes:


class Grid_block:
    def __init__(self, pos, size, status):
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        self.color = (0,0,0)
        self.status = status

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h), 2)
    
    def miss(self):
        self.color = (255,255,255)
    
    def hit(self):
        self.color = (255,0,0)
    
    def occupied(self):
        self.color = (180,0,0)