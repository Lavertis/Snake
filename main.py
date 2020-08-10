from draw import draw
from world import *
from threading import Thread

world = World()

movement_thread = Thread(target=manage_movement, args=(world,), daemon=True)
movement_thread.start()

drawing_thread = Thread(target=draw, args=(world,), daemon=True)
drawing_thread.start()

while True:
    check_for_user_interaction(world)
    sleep(0.002)
