## A* search
from dataclasses import dataclass
import numpy as np

SIZE = 10
MAP = np.zeros((SIZE, SIZE), dtype=np.intp)




START = Point(3, 2)
END = Point(8, 5)


def h(point1: Point, destination: Point = END) -> int:
    """
    Calculates the heuristic score for a given point
    :param point1:
    :param destination:
    :return:
    """
    return abs(point1.x - destination.x) + abs(point1.y - destination.y)


def g(point: Point, source: Point = START) -> float:
    """
    Calculates the cost to reach a point from the source
    :param point:
    :param source:
    :return:
    """
    return 0


if __name__ == "__main__":
    MAP[START] = 1
    MAP[END] = -1
    point = Point(3, 5)
    print(f'H({point}): {h(point)}')
    print(f'G({point}): {g(point)}')
    print(MAP)