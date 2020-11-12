import pygame


class ship_classes:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def __str__(self):
        return f"The {self.name} ship is {self.length} spaces long and {self.width} spaces wide."

    def __repr__(self):
        return f"{self.name}, {self.length}, {self.width}"


Carrier = ship_classes("Carrier", 5, 1)
