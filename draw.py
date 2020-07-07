import pygame
import time

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
    positon_x, positon_y = self.egg.position.x + 1, self.egg.position.y + 1
    size = self.snakeElementSize - 4
    pygame.draw.ellipse(self.screen, self.egg.colour, (positon_x, positon_y, size, size))


def draw_snake_elements(world):
    for el in reversed(world.snakeElements):
        positon_x, positon_y = el.position.x + 1, el.position.y + 1
        size = world.snakeElementSize - 2
        pygame.draw.rect(world.screen, el.colour, (positon_x, positon_y, size, size))


def display_bar(world):
    display_bar_background(world)
    display_fps(world)
    display_score(world)
    display_highscore(world)


def display_bar_background(world):
    border = world.surfaceSize // 5
    border -= border % 20
    colour = (150, 0, 0)
    pygame.draw.rect(world.screen, colour, (0, 0, world.surfaceSize, 20))


def display_score(world):
    text_surface = bar_font.render('SCORE: ' + str(round(world.score)), True, (0, 0, 0))
    world.screen.blit(text_surface, (world.surfaceSize // 2 - world.surfaceSize * 0.04, 0))


def display_highscore(world):
    text_surface = bar_font.render('HIGHSCORE: ' + str(round(world.highScore)), True, (0, 0, 0))
    world.screen.blit(text_surface, (world.surfaceSize * 0.01, 0))


def display_fps(world):
    world.fps = world.clock.get_fps()
    text_surface = bar_font.render('FPS: ' + str(round(world.fps)), True, (0, 0, 0))
    positon = (world.surfaceSize - world.surfaceSize * 0.12, 0)
    world.screen.blit(text_surface, positon)


def show_end_score(world):
    world.screen.fill((0, 0, 0))
    display_bar(world)
    center = get_center(world)
    width = world.surfaceSize * 0.5
    height = world.surfaceSize * 0.1
    pygame.draw.rect(world.screen, (180, 0, 0), (center - width // 2, center - height // 2, width, height))
    font = pygame.font.SysFont('Comic Sans MS', 36)
    text_surface = font.render('Your Score: ' + str(round(world.score)), True, (0, 0, 0))
    world.screen.blit(text_surface, (center - width * 0.325, center - height * 0.35))
    pygame.display.flip()
    time.sleep(3)


def get_center(world):
    center = world.surfaceSize // 2
    center -= - center % 20
    return center
