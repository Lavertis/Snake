def wall_collision(head, border, s):
    if head.position.x < 0 or head.position.y < 0 + s or head.position.x + s > border or head.position.y + s > border:
        return True
    return False


def element_collision(snake_elements):
    element_iterator = iter(snake_elements)
    head = next(element_iterator)
    for el in element_iterator:
        if head.position == el.position:
            return True
    return False


def egg_picked(head, egg):
    return head.position == egg.position


def egg_and_snake_collision(snake, egg_position):
    for el in snake:
        if el.position == egg_position:
            return True
    return False
