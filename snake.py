class SnakeElement:
    def __init__(self, colour, position, velocity):
        self.colour = colour
        self.position = position
        self.velocity = velocity
        self.moves_to_make = []


class Move:
    def __init__(self, position, velocity):
        self.position = position
        self.new_velocity = velocity
