import pygame
from vector import *


class SnakeElement:
    def __init__(self, colour, size, position_x, position_y):
        self.colour = colour
        self.size = size
        self.position = Vector2D(position_x, position_y)
        self.velocity = Vector2D(0, -10)
        self.moves_to_make = []
        self.current_direction_key = pygame.K_UP
        self.opposite_direction_key = pygame.K_DOWN


class Move:
    def __init__(self, position, velocity):
        self.position = position
        self.new_velocity = velocity
