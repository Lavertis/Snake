from snake import *


def check_for_user_interaction(world):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            world.pushed_keys.append(event)
        if event.type == pygame.VIDEORESIZE:
            world.surface_size = event.size
            world.surface_width = event.w
            world.surface_height = event.h
            world.screen = pygame.display.set_mode(world.surface_size, pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            import sys
            sys.exit()


def check_for_direction_change(world):
    if world.pushed_keys:
        event = world.pushed_keys[-1]
        world.pushed_keys.clear()
    else:
        return

    if event.key == world.snake_elements[0].current_direction_key:
        world.add_next_element()
        return
    elif event.key == world.snake_elements[0].opposite_direction_key:
        return

    if event.key == pygame.K_UP:
        go_up(world)
    elif event.key == pygame.K_DOWN:
        go_down(world)
    elif event.key == pygame.K_RIGHT:
        go_right(world)
    elif event.key == pygame.K_LEFT:
        go_left(world)


def go_up(world):
    for element in reversed(world.snake_elements):
        element.current_direction_key = pygame.K_UP
        element.opposite_direction_key = pygame.K_DOWN
        if not element == world.snake_elements[0]:
            element.moves_to_make.append(Move(world.snake_elements[0].position, Vector2D(0, -world.snake_speed)))
        else:
            element.velocity *= 0
            element.velocity.y = -world.snake_speed


def go_down(world):
    for element in reversed(world.snake_elements):
        element.current_direction_key = pygame.K_DOWN
        element.opposite_direction_key = pygame.K_UP
        if not element == world.snake_elements[0]:
            element.moves_to_make.append(Move(world.snake_elements[0].position, Vector2D(0, world.snake_speed)))
        else:
            element.velocity *= 0
            element.velocity.y = world.snake_speed


def go_right(world):
    for element in reversed(world.snake_elements):
        element.current_direction_key = pygame.K_RIGHT
        element.opposite_direction_key = pygame.K_LEFT
        if not element == world.snake_elements[0]:
            element.moves_to_make.append(Move(world.snake_elements[0].position, Vector2D(world.snake_speed, 0)))
        else:
            element.velocity *= 0
            element.velocity.x = world.snake_speed


def go_left(world):
    for element in reversed(world.snake_elements):
        element.current_direction_key = pygame.K_LEFT
        element.opposite_direction_key = pygame.K_RIGHT
        if not element == world.snake_elements[0]:
            element.moves_to_make.append(Move(world.snake_elements[0].position, Vector2D(-world.snake_speed, 0)))
        else:
            element.velocity *= 0
            element.velocity.x = -world.snake_speed
