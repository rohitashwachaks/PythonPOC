## A* search
import numpy as np

from distance_between_islands.common.point_class import Point
from distance_between_islands.common.utils import h, g, read_file


if __name__ == "__main__":
    area_map, start, end = read_file()
    print(area_map)
    print(start, end)
