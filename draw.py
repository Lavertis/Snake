import pygame


def draw(world):
    world.screen.fill((0, 0, 0))
    display_bar(world)
    display_fps(world)
    display_score(world)
    display_highscore(world)
    draw_egg(world)
    draw_snake_elements(world)
    world.clock.tick(60)
    pygame.display.flip()


def draw_egg(self):
    pygame.draw.ellipse(self.screen, self.egg.colour, (self.egg.position.x + 1, self.egg.position.y + 1,
                                                       self.snakeElementSize - 4, self.snakeElementSize - 4))


def draw_snake_elements(world):
    for el in reversed(world.snakeElements):
        pygame.draw.rect(world.screen, el.colour, (el.position.x + 1, el.position.y + 1,
                                                   world.snakeElementSize - 2, world.snakeElementSize - 2))


def display_bar(world):
    border = world.surfaceSize // 5
    border -= border % 20
    pygame.draw.rect(world.screen, (150, 0, 0), (0, 0, world.surfaceSize, 20))


def display_score(world):
    text_surface = world.font.render('SCORE: ' + str(round(world.score)), True, (0, 0, 0))
    world.screen.blit(text_surface, (world.surfaceSize // 2 - world.surfaceSize * 0.05, 0))


def display_highscore(world):
    text_surface = world.font.render('HIGHSCORE: ' + str(round(world.highScore)), True, (0, 0, 0))
    world.screen.blit(text_surface, (world.surfaceSize * 0.01, 0))


def display_fps(world):
    world.fps = world.clock.get_fps()
    text_surface = world.font.render('FPS: ' + str(round(world.fps)), True, (0, 0, 0))
    world.screen.blit(text_surface, (world.surfaceSize - world.surfaceSize * 0.12, 0))
