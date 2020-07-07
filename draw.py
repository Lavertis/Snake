import pygame
from controls import pause

pygame.init()
bar_font = pygame.font.SysFont('Comic Sans MS', 14)


def draw(world):
    world.screen.fill((0, 0, 0))
    display_bar(world)
    draw_egg(world)
    draw_snake_elements(world)
    world.clock.tick(60)
    pygame.display.flip()


def draw_egg(self):
    position_x, position_y = self.egg.position.x + 1, self.egg.position.y + 1
    egg_size = self.snakeElementSize - 4
    pygame.draw.ellipse(self.screen, self.egg.colour, (position_x, position_y, egg_size, egg_size))


def draw_snake_elements(world):
    for element in reversed(world.snakeElements):
        position_x, position_y = element.position.x + 1, element.position.y + 1
        element_size = world.snakeElementSize - 2
        pygame.draw.rect(world.screen, element.colour, (position_x, position_y, element_size, element_size))


def display_bar(world):
    display_bar_background(world)
    display_fps(world)
    display_score(world)
    display_highscore(world)


def display_bar_background(world):
    bar_colour = (160, 0, 0)
    bar_position = (0, 0, world.surfaceSize, 20)
    pygame.draw.rect(world.screen, bar_colour, bar_position)


def display_score(world):
    text_surface = bar_font.render('SCORE: ' + str(round(world.score)), True, (0, 0, 0))
    text_position = (world.surfaceSize // 2 - world.surfaceSize * 0.03, 0)
    world.screen.blit(text_surface, text_position)


def display_highscore(world):
    text_surface = bar_font.render('HIGHSCORE: ' + str(round(world.highScore)), True, (0, 0, 0))
    text_position = (world.surfaceSize * 0.01, 0)
    world.screen.blit(text_surface, text_position)


def display_fps(world):
    world.fps = world.clock.get_fps()
    text_surface = bar_font.render('FPS: ' + str(round(world.fps)), True, (0, 0, 0))
    text_position = (world.surfaceSize - world.surfaceSize * 0.08, 0)
    world.screen.blit(text_surface, text_position)


def display_end_score(world):
    world.screen.fill((0, 0, 0))
    display_bar(world)
    center = get_center(world)
    display_end_score_rect(world, center)
    display_end_score_text(world)
    pygame.display.flip()
    pause(world)


def display_end_score_rect(world, center):
    width, height = world.surfaceSize * 0.5, world.surfaceSize * 0.1
    rect_position_x, rect_position_y = center - width // 2, center - height // 2
    pygame.draw.rect(world.screen, (180, 0, 0), (rect_position_x, rect_position_y, width, height))


def display_end_score_text(world):
    font = pygame.font.SysFont('Comic Sans MS', 36)
    text_surface = font.render('Your score: ' + str(round(world.score)), True, (0, 0, 0))
    text_position = (world.surfaceSize * 0.345, world.surfaceSize * 0.465)
    world.screen.blit(text_surface, text_position)


def get_center(world):
    center = world.surfaceSize // 2
    center -= - center % 20
    return center
