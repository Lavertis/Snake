def wall_collision(head, borders, s):
    if head.position.x < 0 or head.position.y < 0 \
            or head.position.x + s > borders[0] or head.position.y + s > borders[1]:
        return True
    return False
