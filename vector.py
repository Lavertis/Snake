import math


class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return self.x, self.y

    def from_points(P1, P2):
        return Vector2D(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude

    def get_distance_to(self, entity):
        return math.sqrt((self.x - entity[0]) ** 2 + (self.y - entity[1]) ** 2)

    # rhs stands for Right Hand Side
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def __add__(self, rhs):
        return Vector2D(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2D(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mod__(self, p):
        return not (self.x % p == 0 and self.y % p == 0)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __lmul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("list index out of range")
