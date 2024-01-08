import numpy as np

from distance_between_islands.common.point_class import Point


def h(point1: Point, destination: Point) -> int:
    """
    Calculates the heuristic score for a given point
    :param point1:
    :param destination:
    :return:
    """
    return abs(point1.x - destination.x) + abs(point1.y - destination.y)


def g(point: Point, source: Point) -> float:
    """
    Calculates the cost to reach a point from the source
    :param point:
    :param source:
    :return:
    """
    return 0


def read_file(filename: str = 'maps/1.txt') -> np.array:
    out = np.genfromtxt(filename, delimiter=',')
    return out
