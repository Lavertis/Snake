from time import sleep

import pygame

from controls import pause

pygame.init()
bar_font = pygame.font.SysFont('Comic Sans MS', 24)


def draw(screen, surfaceSize, mapSize, score, highScore, egg, snakeElementSize, snakeElements):
    screen.fill((0, 0, 0))
    display_score_bar(highScore, score, surfaceSize, mapSize, screen)
    draw_egg(egg, surfaceSize, mapSize, snakeElementSize, screen)
    draw_snake_elements(snakeElements, surfaceSize, mapSize, snakeElementSize, screen)
    pygame.display.flip()


def draw_egg(egg, surfaceSize, mapSize, snakeElementSize, screen):
    position_x = egg.position.x * surfaceSize / mapSize
    position_y = egg.position.y * surfaceSize / mapSize
    egg_size = snakeElementSize
    pygame.draw.ellipse(screen, egg.colour, (position_x, position_y, egg_size, egg_size))


def draw_snake_elements(snakeElements, surfaceSize, mapSize, snakeElementSize, screen):
    for element in reversed(snakeElements):
        position_x = element.position.x * surfaceSize / mapSize + 2
        position_y = element.position.y * surfaceSize / mapSize + 2
        element_size = snakeElementSize
        pygame.draw.rect(screen, element.colour, (position_x, position_y, element_size, element_size))


def display_score_bar(highScore, score, surfaceSize, mapSize, screen):
    display_bar_background(surfaceSize, mapSize, screen)
    display_score(highScore, score, surfaceSize, screen)


def display_bar_background(surfaceSize, mapSize, screen):
    bar_colour = (160, 0, 0)
    bar_position = (0, 0, surfaceSize, surfaceSize / mapSize)
    pygame.draw.rect(screen, bar_colour, bar_position)


def display_score(highScore, score, surfaceSize, screen):
    text = 'HIGHSCORE: ' + str(round(highScore)) + ' ' * 18 + 'SCORE: ' + str(round(score))
    text_surface = bar_font.render(text, True, (0, 0, 0))
    text_position = (surfaceSize * 0.01, 0)
    screen.blit(text_surface, text_position)


def display_end_score(world):
    w = world
    w.screen.fill((0, 0, 0))
    display_score_bar(w.highScore, w.score, w.surfaceSize, w.mapSize, w.screen)
    display_end_score_rect(w.screen, w.surfaceSize, w.surfaceSize // 2)
    display_end_score_text(w.screen, w.surfaceSize, w.score)
    pygame.display.flip()
    sleep(0.3)
    pause(world)
    pygame.event.clear()


def display_end_score_rect(screen, surfaceSize, center):
    width, height = surfaceSize * 0.5, surfaceSize * 0.1
    rect_position_x, rect_position_y = center - width // 2, center - height // 2
    pygame.draw.rect(screen, (180, 0, 0), (rect_position_x, rect_position_y, width, height))


def display_end_score_text(screen, surfaceSize, score):
    font = pygame.font.SysFont('Comic Sans MS', 36)
    text_surface = font.render('Your score: ' + str(round(score)), True, (0, 0, 0))
    text_position = (surfaceSize * 0.345, surfaceSize * 0.465)
    screen.blit(text_surface, text_position)
