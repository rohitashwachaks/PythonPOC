from dataclasses import dataclass


@dataclass
class Point(tuple):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"