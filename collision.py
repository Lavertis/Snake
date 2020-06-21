def wall_collision(head, border, s):
    if head.position.x < 0 or head.position.y < 0 or head.position.x + s > border or head.position.y + s > border:
        return True
    return False
