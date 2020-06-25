from world import *

world = World()

while True:
    world.draw()
    world.move_snake_elements()
    check_for_direction_change(world)
    check_for_user_interaction(world)

# elementy znakea dodawane z listy elements to be added, żeby się nie dodawały poza planszę przy szczególnym ustawieniu snakea
