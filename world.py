from copy import deepcopy
from controls import *
from collision import *
import random


class World:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.surface_size = int(round(pygame.display.Info().current_h * 0.8, -1))
        self.surface_size -= self.surface_size % 20
        self.screen = pygame.display.set_mode((self.surface_size, self.surface_size))
        self.clock = pygame.time.Clock()
        self.debug_fps = 60
        self.fps = self.clock.get_fps()
        self.fps_font = pygame.font.SysFont('Comic Sans MS', 14)
        self.snake_colour = pygame.Color('red')
        self.egg_colour = pygame.Color('blue')
        self.snake_element_size = 20
        self.snake_speed = 2
        self.egg = Egg(0, 0)
        self.snake_elements = []
        self.pushed_keys = []
        self.score = 0
        self.highscore = 0
        self.reset_game()

    def place_egg(self):
        pos_x = random.randrange(0, self.surface_size, 20)
        pos_y = random.randrange(0, self.surface_size, 20)
        self.egg = Egg(pygame.Color('blue'), Vector2D(pos_x, pos_y))

    def reset_game(self):
        self.snake_elements.clear()
        self.pushed_keys.clear()
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        center = self.surface_size / 2
        center_x = center_y = center - center % 20
        head = SnakeElement(self.snake_colour, Vector2D(center_x, center_y), Vector2D(0, -self.snake_speed))
        self.snake_elements.append(head)
        for _ in range(2):
            self.add_next_element()
        self.place_egg()

    def add_next_element(self):
        self.snake_elements.append(deepcopy(self.snake_elements[-1]))
        tail = self.snake_elements[-1]
        if tail.velocity.x > 0:
            tail.position -= Vector2D(self.snake_element_size, 0)
        elif tail.velocity.x < 0:
            tail.position += Vector2D(self.snake_element_size, 0)
        elif tail.velocity.y > 0:
            tail.position -= Vector2D(0, self.snake_element_size)
        elif tail.velocity.y < 0:
            tail.position += Vector2D(0, self.snake_element_size)

    def move_snake_elements(self):
        if wall_collision(self.snake_elements[0], self.surface_size, self.snake_element_size):
            self.reset_game()
        if element_collision(self.snake_elements):
            self.reset_game()
        if egg_picked(self.snake_elements[0], self.egg):
            self.score += 1
            self.place_egg()
            for _ in range(3):
                self.add_next_element()

        for el in self.snake_elements:
            if el.moves_to_make:
                if el.moves_to_make[0].position == el.position:
                    el.velocity = el.moves_to_make[0].new_velocity
                    el.moves_to_make.pop(0)
            el.position += el.velocity

    def draw_egg(self):
        pygame.draw.ellipse(self.screen, self.egg.colour,
                            (self.egg.position.x, self.egg.position.y, self.snake_element_size - 2, self.snake_element_size - 2))

    def draw_snake_elements(self):
        for el in reversed(self.snake_elements):
            pygame.draw.rect(self.screen, el.colour,
                             (el.position.x + 1, el.position.y + 1, self.snake_element_size - 2, self.snake_element_size - 2))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.display_border()
        self.draw_egg()
        self.draw_snake_elements()
        self.display_fps()
        self.display_score()
        self.display_highscore()
        pygame.display.flip()
        self.clock.tick(self.debug_fps)

    def display_border(self):
        border = self.surface_size // 10
        border -= border % 20
        pygame.draw.rect(self.screen, pygame.Color('brown'), (0, 0, self.surface_size, self.surface_size), border - 2)

    def display_score(self):
        text_surface = self.fps_font.render('SCORE: ' + str(round(self.score)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 20))

    def display_highscore(self):
        text_surface = self.fps_font.render('HIGHSCORE: ' + str(round(self.highscore)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 40))

    def display_fps(self):
        self.fps = self.clock.get_fps()
        if self.fps == math.inf:
            text_surface = self.fps_font.render('FPS: inf', True, (120, 120, 120))
        else:
            text_surface = self.fps_font.render('FPS: ' + str(round(self.fps)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 0))
