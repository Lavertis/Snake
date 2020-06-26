from world import *

world = World()

while True:
    world.draw()
    check_for_user_interaction(world)
    if not world.paused:
        check_for_direction_change(world)
        world.snake_action()
        world.move_snake_elements()
