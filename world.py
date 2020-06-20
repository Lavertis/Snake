from copy import deepcopy
import os
from controls import *


class World:
    def __init__(self):
        if os.name == 'nt':
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
        self.surface_height = 800
        self.surface_width = 800
        pygame.init()
        pygame.display.set_caption('Snake')
        self.surface_size = (self.surface_width, self.surface_height)
        self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = 0.0
        self.fps_font = pygame.font.SysFont('Comic Sans MS', 10)
        self.snake_speed = 10
        self.element_size = 20
        self.pushed_keys = []
        self.snake_elements = [SnakeElement(pygame.Color('red'), 18, 400, 400)]
        self.add_next_element()
        self.add_next_element()

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
        tail.colour = pygame.Color('red')

    def display_fps(self):
        self.clock.tick(10)
        self.fps = self.clock.get_fps()
        if self.fps == math.inf:
            text_surface = self.fps_font.render('FPS: inf', True, (120, 120, 120))
        else:
            text_surface = self.fps_font.render('FPS: ' + str(round(self.fps)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 0))

    def move_snake_elements(self):
        for el in self.snake_elements:
            if el.moves_to_make:
                if el.moves_to_make[0].position == el.position:
                    el.velocity = el.moves_to_make[0].new_velocity
                    el.moves_to_make.pop(0)
            el.position += el.velocity

    def draw_snake_elements(self):
        self.screen.fill((0, 0, 0))
        for el in reversed(self.snake_elements):
            pygame.draw.rect(self.screen, el.colour, (el.position.x, el.position.y, el.size, el.size))
        self.display_fps()
        pygame.display.flip()
