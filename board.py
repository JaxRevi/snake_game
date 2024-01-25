import pygame
from settings import Settings
import game_functions as gf

class Board():
    def __init__(self, settings):
        self.rows = settings.screen_height // 100 * 2
        self.cols = settings.screen_width // 100 * 2
        self.board = [[None for i in range(self.cols)] for j in range(int(self.rows))]
        self.game_over = False
        self.fruit_list = gf.create_fruit_list(settings.board_size)