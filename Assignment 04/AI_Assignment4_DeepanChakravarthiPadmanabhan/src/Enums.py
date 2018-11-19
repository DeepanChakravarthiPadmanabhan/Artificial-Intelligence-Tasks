from enum import Enum


class Positions(Enum):
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3
    TOP = 4


class Algorithms(Enum):
    GREEDY = 1
    A_STAR = 2


class Heuristics(Enum):
    NUMBER_OF_TILES = 1
    MANHATTAN_DISTANCE = 2