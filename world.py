from copy import deepcopy
import os
from snake import *


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
        self.snake_elements = []
        self.pushed_keys = []
        self.element_size = 30
        self.snake_elements.append(SnakeElement(pygame.Color('red'), 27, 400, 400))
        self.snake_elements.append(SnakeElement(pygame.Color('red'), 27, 400, 430))
        self.snake_elements.append(SnakeElement(pygame.Color('red'), 27, 400, 460))

    def check_for_user_interaction(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.pushed_keys.append(event)
            if event.type == pygame.VIDEORESIZE:
                self.surface_size = event.size
                self.surface_width = event.w
                self.surface_height = event.h
                self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)
            if event.type == pygame.QUIT:
                import sys
                sys.exit()

    def check_for_direction_change(self):
        if not self.pushed_keys:
            return

        event = self.pushed_keys[-1]
        self.pushed_keys.clear()

        if event.key == self.snake_elements[0].current_direction_key:
            self.add_next_element()
            return
        if event.key == self.snake_elements[0].opposite_direction_key:
            return

        if event.key == pygame.K_UP:
            for element in reversed(self.snake_elements):
                element.current_direction_key = pygame.K_UP
                element.opposite_direction_key = pygame.K_DOWN
                if not element == self.snake_elements[0]:
                    element.moves_to_make.append(Move(self.snake_elements[0].position, Vector2D(0, -self.snake_speed)))
                else:
                    element.velocity *= 0
                    element.velocity.y = -self.snake_speed

        if event.key == pygame.K_DOWN:
            for element in reversed(self.snake_elements):
                element.current_direction_key = pygame.K_DOWN
                element.opposite_direction_key = pygame.K_UP
                if not element == self.snake_elements[0]:
                    element.moves_to_make.append(Move(self.snake_elements[0].position, Vector2D(0, self.snake_speed)))
                else:
                    element.velocity *= 0
                    element.velocity.y = self.snake_speed

        if event.key == pygame.K_LEFT:
            for element in reversed(self.snake_elements):
                element.current_direction_key = pygame.K_LEFT
                element.opposite_direction_key = pygame.K_RIGHT
                if not element == self.snake_elements[0]:
                    element.moves_to_make.append(Move(self.snake_elements[0].position, Vector2D(-self.snake_speed, 0)))
                else:
                    element.velocity *= 0
                    element.velocity.x = -self.snake_speed

        if event.key == pygame.K_RIGHT:
            for element in reversed(self.snake_elements):
                element.current_direction_key = pygame.K_RIGHT
                element.opposite_direction_key = pygame.K_LEFT
                if not element == self.snake_elements[0]:
                    element.moves_to_make.append(Move(self.snake_elements[0].position, Vector2D(self.snake_speed, 0)))
                else:
                    element.velocity *= 0
                    element.velocity.x = self.snake_speed

    def add_next_element(self):
        self.snake_elements.append(deepcopy(self.snake_elements[-1]))
        tail = self.snake_elements[-1]
        if tail.velocity.x > 0:
            self.snake_elements[-1].position -= Vector2D(self.element_size, 0)
        elif tail.velocity.x < 0:
            self.snake_elements[-1].position += Vector2D(self.element_size, 0)
        elif tail.velocity.y > 0:
            self.snake_elements[-1].position -= Vector2D(0, self.element_size)
        elif tail.velocity.y < 0:
            self.snake_elements[-1].position += Vector2D(0, self.element_size)
        self.snake_elements[-1].colour = pygame.Color('yellow')

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
