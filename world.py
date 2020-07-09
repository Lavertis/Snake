from controls import *
from action import *
from draw import get_center


class World:
    def __init__(self):
        pygame.display.set_caption('Snake')
        self.surfaceSize = get_surface_size()
        self.screen = pygame.display.set_mode((self.surfaceSize, self.surfaceSize))
        self.clock = pygame.time.Clock()
        self.fps = self.clock.get_fps()
        self.snakeColour = pygame.Color('red')
        self.eggColour = pygame.Color('blue')
        self.snakeElementSize = 20
        self.speed = 2.5
        self.egg = Egg
        self.snakeElements = []
        self.pushedKeys = []
        self.snakeElementsToBeAdded = 0
        self.score = 0
        self.highScore = 0
        self.paused = False
        self.reset_game()

    def reset_game(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.snakeElementsToBeAdded = 0
        self.snakeElements.clear()
        self.pushedKeys.clear()
        center = get_center(self)
        head = SnakeElement(self.snakeColour, Vector2D(center, center), Vector2D(0, -self.speed))
        self.snakeElements.append(head)
        for _ in range(2):
            add_next_element(self)
        place_egg(self)


def get_surface_size():
    surface_size = int(pygame.display.Info().current_h // 1.5)
    surface_size -= surface_size % 20
    return surface_size
