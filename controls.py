import pygame
from vector import *
from snake import *


def check_for_direction_change(world):
    if world.pushed_keys and world.snake_elements[0].position % 20 == 0:
        event = world.pushed_keys.pop(0)
        if event.key == pygame.K_UP:
            go_up(world)
        elif event.key == pygame.K_DOWN:
            go_down(world)
        elif event.key == pygame.K_RIGHT:
            go_right(world)
        elif event.key == pygame.K_LEFT:
            go_left(world)
        elif event.key == pygame.K_a:
            world.add_next_element()
        print(world.snake_elements[0].position)


def go_up(world):
    element_iterator = iter(world.snake_elements)
    head = next(element_iterator)
    if head.velocity.y == 0:
        change_position_cords = head.position
        head.velocity = Vector2D(0, -world.snake_speed)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(0, -world.snake_speed)))


def go_down(world):
    element_iterator = iter(world.snake_elements)
    head = next(element_iterator)
    if head.velocity.y == 0:
        change_position_cords = head.position
        head.velocity = Vector2D(0, world.snake_speed)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(0, world.snake_speed)))


def go_right(world):
    element_iterator = iter(world.snake_elements)
    head = next(element_iterator)
    if head.velocity.x == 0:
        change_position_cords = head.position
        head.velocity = Vector2D(world.snake_speed, 0)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(world.snake_speed, 0)))


def go_left(world):
    element_iterator = iter(world.snake_elements)
    head = next(element_iterator)
    if head.velocity.x == 0:
        change_position_cords = head.position
        head.velocity = Vector2D(-world.snake_speed, 0)
        for element in element_iterator:
            element.moves_to_make.append(Move(change_position_cords, Vector2D(-world.snake_speed, 0)))


def check_for_user_interaction(world):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            world.pushed_keys.append(event)
        if event.type == pygame.VIDEORESIZE:
            world.surface_size = event.size
            event.w = round(event.w, -1)
            event.h = round(event.h, -1)
            world.surface_size = (event.w - event.w % 20, event.h - event.h % 20)
            world.screen = pygame.display.set_mode(world.surface_size, pygame.RESIZABLE)
            print(str(world.surface_size[0]) + 'x' + str(world.surface_size[1]))
        if event.type == pygame.QUIT:
            import sys
            sys.exit()
