import pygame

from action import add_next_element, place_egg
from draw import draw
from snake import SnakeElement, Egg
from vector import Vector2D


class World:
    def __init__(self):
        pygame.display.set_caption('Snake')
        self.surfaceSize = get_surface_size()
        self.screen = pygame.display.set_mode((self.surfaceSize, self.surfaceSize))
        self.snakeColour = pygame.Color('red')
        self.eggColour = pygame.Color('blue')
        self.mapSize = 20
        self.snakeElementSize = self.surfaceSize / self.mapSize - 4
        self.speed = 0.125
        self.egg = Egg
        self.snakeElements = []
        self.pushedKeys = []
        self.snakeElementsToBeAdded = 0
        self.score = 0
        self.highScore = 0
        self.paused = True
        self.reset_game()
        s = self
        draw(s.screen, s.surfaceSize, s.mapSize, s.score, s.highScore, s.egg, s.snakeElementSize, s.snakeElements)

    def reset_game(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.snakeElementsToBeAdded = 0
        self.snakeElements.clear()
        self.pushedKeys.clear()
        center = self.mapSize // 2
        head = SnakeElement(self.snakeColour, Vector2D(center, center), Vector2D(0, -1))
        self.snakeElements.append(head)
        for _ in range(2):
            add_next_element(self.snakeElements)
        place_egg(self)


def get_surface_size():
    return int(pygame.display.Info().current_h // 1.5)
