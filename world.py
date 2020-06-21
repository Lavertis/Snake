from copy import deepcopy
from controls import *
from collision import *


class World:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.surface_size = (800, 800)
        self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = self.clock.get_fps()
        self.fps_font = pygame.font.SysFont('Comic Sans MS', 10)
        self.snake_speed = 2
        self.element_size = 20
        self.snake_elements = []
        self.pushed_keys = []
        self.reset_game()

    def reset_game(self):
        center_x = self.surface_size[0] / 2
        center_y = self.surface_size[1] / 2
        self.snake_elements.clear()
        self.snake_elements.append(
            SnakeElement(pygame.Color('red'), Vector2D(center_x, center_y), Vector2D(0, -self.snake_speed)))
        for _ in range(6):
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

    def move_snake_elements(self):
        if wall_collision(self.snake_elements[0], self.surface_size, self.element_size):
            self.reset_game()
        for el in self.snake_elements:
            if el.moves_to_make:
                if el.moves_to_make[0].position == el.position:
                    el.velocity = el.moves_to_make[0].new_velocity
                    el.moves_to_make.pop(0)
            el.position += el.velocity

    def draw_snake_elements(self):
        self.screen.fill((0, 0, 0))
        for el in reversed(self.snake_elements):
            pygame.draw.rect(self.screen, el.colour,
                             (el.position.x, el.position.y, self.element_size - 2, self.element_size - 2))
        self.display_fps()
        pygame.display.flip()

    def display_fps(self):
        self.clock.tick(60)
        self.fps = self.clock.get_fps()
        if self.fps == math.inf:
            text_surface = self.fps_font.render('FPS: inf', True, (120, 120, 120))
        else:
            text_surface = self.fps_font.render('FPS: ' + str(round(self.fps)), True, (120, 120, 120))
        self.screen.blit(text_surface, (2, 0))
