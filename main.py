from world import *

world = World()

while True:
    world.draw()
    check_for_user_interaction(world)
    check_for_direction_change(world)
    if not world.paused:
        world.move_snake_elements()

# elementy znakea dodawane z listy elements to be added, żeby się nie dodawały poza planszę przy szczególnym ustawieniu snakea
