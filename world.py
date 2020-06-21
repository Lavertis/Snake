from copy import deepcopy
from controls import *
from collision import *
import random


class World:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        surface_size = int(round(pygame.display.Info().current_h * 0.8, -1))
        surface_size -= surface_size % 20
        self.surface_size = (surface_size, surface_size)
        self.screen = pygame.display.set_mode(self.surface_size)
        self.clock = pygame.time.Clock()
        self.debug_fps = 60
        self.fps = self.clock.get_fps()
        self.fps_font = pygame.font.SysFont('Comic Sans MS', 10)
        self.snake_colour = pygame.Color('red')
        self.element_size = 20
        self.snake_speed = 2
        self.egg_colour = pygame.Color('blue')
        self.egg = Egg
        self.snake_elements = []
        self.pushed_keys = []
        self.reset_game()

    def place_egg(self):
        pos_x = random.randrange(0, self.surface_size[0], 20)
        pos_y = random.randrange(0, self.surface_size[1], 20)
        self.egg = Egg(self.egg_colour, Vector2D(pos_x, pos_y))

    def reset_game(self):
        self.snake_elements.clear()
        self.pushed_keys.clear()
        center = self.surface_size[0] / 2
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
            tail.position -= Vector2D(self.element_size, 0)
        elif tail.velocity.x < 0:
            tail.position += Vector2D(self.element_size, 0)
        elif tail.velocity.y > 0:
            tail.position -= Vector2D(0, self.element_size)
        elif tail.velocity.y < 0:
            tail.position += Vector2D(0, self.element_size)

    def move_snake_elements(self):
        if wall_collision(self.snake_elements[0], self.surface_size[0], self.element_size):
            self.reset_game()
        if element_collision(self.snake_elements):
            self.reset_game()
        if egg_picked(self.snake_elements[0], self.egg):
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
                            (self.egg.position.x, self.egg.position.y, self.element_size - 2, self.element_size - 2))

    def draw_snake_elements(self):
        for el in reversed(self.snake_elements):
            pygame.draw.rect(self.screen, el.colour,
                             (el.position.x, el.position.y, self.element_size - 2, self.element_size - 2))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_egg()
        self.draw_snake_elements()
        self.display_fps()
        pygame.display.flip()

    def display_fps(self):
        self.clock.tick(self.debug_fps)
        self.fps = self.clock.get_fps()
        if self.fps == math.inf:
            text_surface = self.fps_font.render('FPS: inf', True, (120, 120, 120))
        else:
            text_surface = self.fps_font.render('FPS: ' + str(round(self.fps)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 0))
