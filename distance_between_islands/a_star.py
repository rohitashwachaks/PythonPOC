## A* search
import numpy as np

from distance_between_islands.common.point_class import Point
from distance_between_islands.common.utils import h, g, read_file

SIZE = 10
MAP = np.zeros((SIZE, SIZE), dtype=np.intp)

START = Point(3, 2)
END = Point(8, 5)

if __name__ == "__main__":
    area_map = read_file()
    MAP[START] = 1
    MAP[END] = -1
    point = Point(3, 5)
    print(f'H({point}): {h(point, END)}')
    print(f'G({point}): {g(point, START)}')
    print(MAP)
