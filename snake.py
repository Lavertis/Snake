import pygame
from vector import *


class SnakeElement:
    def __init__(self, surface, colour, size, position_x, position_y):
        self.surface = surface
        self.colour = colour
        self.size = size
        self.position = Vector2D(position_x, position_y)
        self.velocity = Vector2D(0, -5)
        self.moves_to_make = []
        self.current_direction_key = pygame.K_UP
        self.opposite_direction_key = pygame.K_DOWN

    def get_copy(self):
        element = SnakeElement(self.surface, self.colour, self.size, self.position.x, self.position.y)
        element.velocity = self.velocity
        element.moves_to_make = self.moves_to_make.copy()
        element.current_direction_key = self.current_direction_key
        element.opposite_direction_key = self.opposite_direction_key
        return element


class Move:
    def __init__(self, position, velocity):
        self.position = position
        self.new_velocity = velocity
