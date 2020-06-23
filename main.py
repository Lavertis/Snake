from world import *

world = World()

while True:
    world.draw()
    world.move_snake_elements()
    check_for_direction_change(world)
    check_for_user_interaction(world)

#Zaifować, żeny jajko nie mogło pojawić się pod Snakiem
