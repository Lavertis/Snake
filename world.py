from controls import *
from action import *


class World:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.surfaceSize = int(pygame.display.Info().current_h // 1.5)
        self.surfaceSize -= self.surfaceSize % 20
        self.screen = pygame.display.set_mode((self.surfaceSize, self.surfaceSize))
        self.clock = pygame.time.Clock()
        self.fps = self.clock.get_fps()
        self.font = pygame.font.SysFont('Comic Sans MS', 14)
        self.snakeColour = pygame.Color('red')
        self.eggColour = pygame.Color('blue')
        self.snakeElementSize = 20
        self.speed = 2.5
        self.egg = Egg(0, 0)
        self.snakeElements = []
        self.pushedKeys = []
        self.snakeElementsToBeAdded = 0
        self.score = 0
        self.highScore = 0
        self.paused = False
        self.reset_game()

    def reset_game(self):
        self.snakeElements.clear()
        self.pushedKeys.clear()
        self.snakeElementsToBeAdded = 0
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        center = self.surfaceSize // 2
        center_x = center_y = center - center % 20
        head = SnakeElement(self.snakeColour, Vector2D(center_x, center_y), Vector2D(0, -self.speed))
        self.snakeElements.append(head)
        for _ in range(2):
            add_next_element(self)
        place_egg(self)
