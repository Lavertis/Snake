from threading import Thread
from time import sleep

from action import move_and_draw
from controls import check_for_user_interaction
from world import World

world = World()

move_and_draw_thread = Thread(target=move_and_draw, args=(world,), daemon=True)
move_and_draw_thread.start()

while True:
    check_for_user_interaction(world)
    sleep(0.002)
