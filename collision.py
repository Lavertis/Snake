import itertools


def wall_collision(head, border, s):
    if head.position.x < 0 or head.position.y < 0 or head.position.x + s > border or head.position.y + s > border:
        return True
    return False


def element_collision(snake_elements):
    for el1, el2 in itertools.combinations(snake_elements, 2):
        if el1.position == el2.position:
            return True
    return False


def egg_picked(head, egg):
    return head.position == egg.position
