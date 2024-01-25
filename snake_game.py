import pygame, sys, random
from snake import Snake
from board import Board
from settings import Settings
from score import Score
from fruits import Fruits
from bombs import Bombs
from game_enums import *
import game_functions as gf



def run_game():
    pygame.init()
    # TODO: create a start menu
    # player can see leaderboard, choice to start game, and select map
    # TODO , bombs, and wall obstacles

    snake_game_settings = Settings(Debug_Mode.ON, Board_Size.LARGE, pygame.font)
    # snake_game_settings.screen = pygame.display.set_mode(
    #     (snake_game_settings.screen_width, snake_game_settings.screen_height))
    pygame.display.set_caption('Snake Game')
    pygame.mixer.music.load('media/main_game_music.mp3')

    # create Score object
    score = Score()

    # create Board object
    board = Board(snake_game_settings)
    # make the snake start at top left corner of screen
    snake_start = [(0,0), (1,0), (2,0)]
    snake = Snake(snake_start, Direction.RIGHT)

    # create Fruit object
    fruits = Fruits(score)

    # create Bomb object
    bomb = Bombs(score)


    gf.update_board(snake_game_settings, score, board, snake, fruits, bomb)
    gf.produce_fruit(snake_game_settings, board, score, snake)
    gf.create_bomb(snake_game_settings, board)

    pygame.mixer.music.play(-1)
    while True:
        gf.check_events(snake_game_settings, board, snake)
        gf.update_screen(snake_game_settings, snake_game_settings.screen, score, board, snake, fruits, bomb)


if __name__ == '__main__':
    run_game()
