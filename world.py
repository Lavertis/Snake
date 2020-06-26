from copy import deepcopy
from controls import *
from collision import *
import random


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
        self.score = 0
        self.highScore = 999
        self.paused = False
        self.reset_game()

    def place_egg(self):
        pos = Vector2D(random.randrange(0, self.surfaceSize, 20), random.randrange(20, self.surfaceSize, 20))
        while egg_and_snake_collision(self.snakeElements, pos):
            pos = Vector2D(random.randrange(0, self.surfaceSize, 20), random.randrange(20, self.surfaceSize, 20))
        self.egg = Egg(pygame.Color('blue'), pos)

    def reset_game(self):
        self.snakeElements.clear()
        self.pushedKeys.clear()
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        center = self.surfaceSize // 2
        center_x = center_y = center - center % 20
        head = SnakeElement(self.snakeColour, Vector2D(center_x, center_y), Vector2D(0, -self.speed))
        self.snakeElements.append(head)
        for _ in range(2):
            self.add_next_element()
        self.place_egg()

    def add_next_element(self):
        self.snakeElements.append(deepcopy(self.snakeElements[-1]))
        tail = self.snakeElements[-1]
        if tail.velocity.x > 0:
            tail.position -= Vector2D(self.snakeElementSize, 0)
        elif tail.velocity.x < 0:
            tail.position += Vector2D(self.snakeElementSize, 0)
        elif tail.velocity.y > 0:
            tail.position -= Vector2D(0, self.snakeElementSize)
        elif tail.velocity.y < 0:
            tail.position += Vector2D(0, self.snakeElementSize)

    def move_snake_elements(self):
        if wall_collision(self.snakeElements[0], self.surfaceSize, self.snakeElementSize):
            self.reset_game()
        if element_collision(self.snakeElements):
            self.reset_game()
        if egg_picked(self.snakeElements[0], self.egg):
            self.score += 1
            self.place_egg()
            for _ in range(3):
                self.add_next_element()

        for el in self.snakeElements:
            if el.moves_to_make:
                if el.moves_to_make[0].position == el.position:
                    el.velocity = el.moves_to_make[0].new_velocity
                    el.moves_to_make.pop(0)
            el.position += el.velocity

    def draw_egg(self):
        pygame.draw.ellipse(self.screen, self.egg.colour, (self.egg.position.x, self.egg.position.y,
                                                           self.snakeElementSize - 3, self.snakeElementSize - 3))

    def draw_snake_elements(self):
        for el in reversed(self.snakeElements):
            pygame.draw.rect(self.screen, el.colour, (el.position.x + 1, el.position.y + 1,
                                                      self.snakeElementSize - 2, self.snakeElementSize - 2))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.display_bar()
        self.display_fps()
        self.display_score()
        self.display_highscore()
        self.draw_egg()
        self.draw_snake_elements()
        self.clock.tick(60)
        pygame.display.flip()

    def display_bar(self):
        border = self.surfaceSize // 5
        border -= border % 20
        pygame.draw.rect(self.screen, (150, 0, 0), (0, 0, self.surfaceSize, 20))

    def display_score(self):
        text_surface = self.font.render('SCORE: ' + str(round(self.score)), True, (0, 0, 0))
        self.screen.blit(text_surface, (self.surfaceSize // 2 - self.surfaceSize * 0.05, 0))

    def display_highscore(self):
        text_surface = self.font.render('HIGHSCORE: ' + str(round(self.highScore)), True, (0, 0, 0))
        self.screen.blit(text_surface, (self.surfaceSize - self.surfaceSize * 0.18, 0))

    def display_fps(self):
        self.fps = self.clock.get_fps()
        if self.fps == math.inf:
            text_surface = self.font.render('FPS: inf', True, (120, 120, 120))
        else:
            text_surface = self.font.render('FPS: ' + str(round(self.fps)), True, (0, 0, 0))
        self.screen.blit(text_surface, (self.surfaceSize * 0.01, 0))
