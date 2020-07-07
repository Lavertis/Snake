from draw import draw
from world import *

world = World()

while True:
    check_for_user_interaction(world)
    if not world.paused:
        draw(world)
        move(world)
        take_action(world)
        check_for_direction_change(world)
