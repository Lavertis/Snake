import random
from copy import deepcopy
from time import sleep

from collision import *
from controls import check_for_direction_change
from draw import display_end_score, draw
from snake import Egg
from vector import Vector2D


def move_and_draw(world):
    while True:
        if not world.paused:
            sleep(world.speed)
            check_for_direction_change(world)
            move(world)
            draw(world)
            take_action(world)


def move(self):
    for element in self.snakeElements:
        if element.moves_to_make:
            if element.moves_to_make[0].position == element.position:
                element.velocity = element.moves_to_make[0].new_velocity
                element.moves_to_make.pop(0)
        element.position += element.velocity


def take_action(world):
    if world.snakeElementsToBeAdded:
        add_next_element(world)
        world.snakeElementsToBeAdded -= 1
    if wall_collision(world.snakeElements[0], world.mapSize):
        display_end_score(world)
        world.reset_game()
    elif itself_collision(world.snakeElements):
        display_end_score(world)
        world.reset_game()
    elif egg_picked(world.snakeElements[0], world.egg):
        world.score += 1
        world.snakeElementsToBeAdded += 3
        place_egg(world)


def new_egg_position(world):
    return Vector2D(random.randrange(0, world.mapSize), random.randrange(1, world.mapSize))


def place_egg(world):
    position = new_egg_position(world)
    while egg_and_snake_collision(world.snakeElements, position):
        position = new_egg_position(world)
    world.egg = Egg(world.eggColour, position)


def add_next_element(world):
    world.snakeElements.append(deepcopy(world.snakeElements[-1]))
    tail = world.snakeElements[-1]

    if tail.colour[2] < 255:
        tail.colour[2] = tail.colour[2] + 1

    if tail.velocity.x > 0:
        tail.position -= Vector2D(1, 0)
    elif tail.velocity.x < 0:
        tail.position += Vector2D(1, 0)
    elif tail.velocity.y > 0:
        tail.position -= Vector2D(0, 1)
    elif tail.velocity.y < 0:
        tail.position += Vector2D(0, 1)
