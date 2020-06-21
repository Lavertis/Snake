from world import *

world = World()

while True:
    world.draw_snake_elements()
    world.move_snake_elements()
    check_for_direction_change(world)
    check_for_user_interaction(world)

#Dodać ramkę dookoła ekranu, zmniejszyć tak, żeby zostało z 20 pikseli dookoła