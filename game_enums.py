import pygame
from enum import Enum, auto

class Debug_Mode(Enum):
    ON = auto()
    OFF = auto()

class Board_Size(Enum):
    SMALL = (6,6)
    MEDIUM = (8,7.5)
    LARGE = (12,7.5)

class Direction(Enum):
    LEFT = (-1,0)
    RIGHT = (1,0)
    UP = (0,-1)
    DOWN = (0,1)

class Colors(Enum):
    LIGHT_BLUE = (144, 238, 144)
    DARK_GREY = (168, 168, 168)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class Fruit_Type(Enum):
    APPLE = 1
    PINAPPLE = 4
    CHERRY = 2

class Obstacles(Enum):
    BOMB = auto()
    WALL = auto()