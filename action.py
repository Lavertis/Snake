import random
from copy import deepcopy
from collision import *
from draw import show_end_score
from snake import Egg
from vector import Vector2D


def move_snake_elements(self):
    for element in self.snakeElements:
        if element.moves_to_make:
            if element.moves_to_make[0].position == element.position:
                element.velocity = element.moves_to_make[0].new_velocity
                element.moves_to_make.pop(0)
        element.position += element.velocity


def snake_action(world):
    if world.snakeElements[0].position % 20 == 0 and world.snakeElementsToBeAdded:
        add_next_element(world)
        world.snakeElementsToBeAdded -= 1
    if wall_collision(world.snakeElements[0], world.surfaceSize, world.snakeElementSize):
        show_end_score(world)
        world.reset_game()
    elif element_collision(world.snakeElements):
        show_end_score(world)
        world.reset_game()
    elif egg_picked(world.snakeElements[0], world.egg):
        world.score += 1
        world.snakeElementsToBeAdded += 3
        place_egg(world)


def place_egg(world):
    position = Vector2D(random.randrange(0, world.surfaceSize, 20), random.randrange(20, world.surfaceSize, 20))
    while egg_and_snake_collision(world.snakeElements, position):
        position = Vector2D(random.randrange(0, world.surfaceSize, 20), random.randrange(20, world.surfaceSize, 20))
    world.egg = Egg(world.eggColour, position)


def add_next_element(world):
    world.snakeElements.append(deepcopy(world.snakeElements[-1]))
    tail = world.snakeElements[-1]
    if tail.velocity.x > 0:
        tail.position -= Vector2D(world.snakeElementSize, 0)
    elif tail.velocity.x < 0:
        tail.position += Vector2D(world.snakeElementSize, 0)
    elif tail.velocity.y > 0:
        tail.position -= Vector2D(0, world.snakeElementSize)
    elif tail.velocity.y < 0:
        tail.position += Vector2D(0, world.snakeElementSize)
