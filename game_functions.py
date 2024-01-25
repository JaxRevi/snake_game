import sys, time, random
import pygame
from game_enums import *
from settings import Settings
# from snake import Snake
# from apple import Apple
# from board import Board


# game over functions
def set_game_over(settings, board, snake):
    head = snake.get_head()
    if board.board[head[1]][head[0]] == 0:
        board.game_over = True
    elif board.board[head[1]][head[0]] == Obstacles.BOMB:
        settings.bomb_sound.play()
        board.game_over = True

def game_over(settings, score):
    # stop main game music from playing
    pygame.mixer.music.stop()

    # play losing sound
    settings.game_over_sound.play()

    # pause for a second so player can see their action
    time.sleep(1)


    # TODO: add sound effect for game over
    # fill screen with a 'game over'
    game_over_text = settings.game_over_font.render('GAME OVER', True, Colors.DARK_GREY.value)
    score_text = settings.score_font.render('SCORE: ' + str(score.score), True, Colors.WHITE.value)
    settings.screen.fill(Colors.BLACK.value)
    settings.screen.blit(game_over_text, (settings.screen_width / 2 - game_over_text.get_width() / 2, 
                                            settings.screen_height / 2 - game_over_text.get_height() / 2))
    settings.screen.blit(score_text, (settings.screen_width / 2 - score_text.get_width() / 2,
                                            settings.screen_height / 2 + score_text.get_height() / 2))
    pygame.display.flip()
    # wait so player can see their progress and close out game
    # TODO: give option for player to start again
    time.sleep(3)
    pygame.quit()
    sys.exit()

# timer functions
def set_inactive_timer(settings):
    pygame.time.set_timer(settings.INACTIVE_EVENT, settings.inactive_timeout)

# input functions
def check_keydown_event(event, settings, board, snake):
    """Respond to keyboard presses"""
    key = event.key
    if key == pygame.K_RIGHT or key == pygame.K_d:
        snake.set_direction(Direction.RIGHT)
    elif key == pygame.K_LEFT or key == pygame.K_a:
        snake.set_direction(Direction.LEFT)
    elif key == pygame.K_UP or key == pygame.K_w:
        snake.set_direction(Direction.UP)
    elif key == pygame.K_DOWN or key == pygame.K_s:
        snake.set_direction(Direction.DOWN)
    elif key == pygame.K_q:
        pygame.quit()
        sys.exit()
    else:
        return
    
def check_keyup_event(event, settings, board, snake):
    if event.key in settings.valid_key_events:
        snake.take_step(board)
        set_inactive_timer(settings)

def check_events(settings, board, snake):
    """Respond to keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, settings, board, snake)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, settings, board, snake)
        elif event.type == settings.INACTIVE_EVENT:
            snake.take_step(board)
            set_inactive_timer(settings)

# board functions
def create_fruit_list(board_size):
        fruits_list = [Fruit_Type.APPLE, Fruit_Type.CHERRY, Fruit_Type.PINAPPLE]
        if board_size == Board_Size.LARGE:
            weights = [5,3,1]
            return random.choices(fruits_list, weights, k=18)
        else:
            weights = [5,3,0]
            return random.choices(fruits_list, weights, k=18)

def update_screen(settings, screen, score, board, snake, fruits, bomb):
    screen.fill(settings.background_color)
    update_board(settings, score, board, snake, fruits, bomb)
    draw_board(screen, settings, board, snake)
    pygame.display.flip()

def update_board(settings, score, board, snake, fruits, bomb): 
    # check to see if snake is out of bound or has eatan self
    if check_snake_outbound(board, snake) or is_game_over(board):
        game_over(settings, score)

    # check to see if we just ate a fruit, is not we need to
    # set the previous tail to None value
    if check_if_fruit(board, snake):
        snake.extend_body()

    # fill board with snake's body
    for body in snake.body[:len(snake.body) - 1]:
        x_position = body[0]
        y_position = body[1]
        board.board[y_position][x_position] = 0
    
    # mark the snake's head
    head = snake.get_head()
    set_game_over(settings, board, snake)
    if check_if_fruit(board, snake):
        produce_fruit(settings, board, score, snake)
        add_score(score, board, snake)

    board.board[head[1]][head[0]] = 1 

    if fruits.passed_threshold():
        fruits.update_threshold()
        produce_fruit(settings, board, score, snake)

    if bomb.passed_threshold():
        bomb.update_threshold()
        create_bomb(settings, board)

def draw_board(screen, settings, board, snake):
    image_scale = settings.image_scale
    for row, rows in enumerate(board.board):
        for col, element in enumerate(rows):
            if element == 0:
                screen.blit(settings.scaled_body_image, (col * image_scale, row * image_scale))
            elif element == 1:
                snake_direction = snake.get_direction()
                if snake_direction == Direction.RIGHT:
                    screen.blit(settings.scaled_right_head_image, (col * image_scale, row * image_scale))
                elif snake_direction == Direction.LEFT:
                    screen.blit(settings.scaled_left_head_image, (col * image_scale, row * image_scale))
                elif snake_direction == Direction.UP:
                    screen.blit(settings.scaled_up_head_image, (col * image_scale, row * image_scale))
                elif snake_direction == Direction.DOWN:
                    screen.blit(settings.scaled_down_head_image, (col * image_scale, row * image_scale))
            elif element == Fruit_Type.APPLE:
                screen.blit(settings.scaled_apple_image, (col * image_scale, row * image_scale))
            elif element == Fruit_Type.CHERRY:
                screen.blit(settings.scaled_cherry_image, (col * image_scale, row * image_scale))
            elif element == Fruit_Type.PINAPPLE:
                screen.blit(settings.scaled_pineapple_image, (col * image_scale, row * image_scale))
            elif element == Obstacles.BOMB:
                screen.blit(settings.scaled_bomb_image, (col * image_scale, row * image_scale))

# snake functions
def check_snake_outbound(board, snake):
    head = snake.get_head()
    return not (head[0] < board.cols and head[0] >= 0 and head[1] < board.rows and head[1] >= 0) 

def is_game_over(board):
    return board.game_over

# Fruit functions
def produce_fruit(settings, board, score, snake):
    fruit_x = random.randint(0, board.cols - 1)
    fruit_y = random.randint(0, board.rows - 1)
    while board.board[fruit_y][fruit_x] is not None:
        fruit_x = random.randint(0, board.cols - 1)
        fruit_y = random.randint(0, board.rows - 1)
    # debug mode
    # if settings.debug_mode == Debug_Mode.ON:
    #     print('(x,y): ', fruit_x, fruit_y)
    #     for b in board.board:
    #         print(b)

    fruit = random.choice(board.fruit_list)
    board.board[fruit_y][fruit_x] = fruit

def check_if_fruit(board, snake):
    head = snake.get_head()
    return isinstance(board.board[head[1]][head[0]], Fruit_Type)

# Obstacles functions

def create_bomb(settings, board):
    bomb_x = random.randint(0, board.cols - 1)
    bomb_y = random.randint(0, board.rows - 1)
    while board.board[bomb_y][bomb_x] is not None:
        bomb_x = random.randint(0, board.cols - 1)
        bomb_y = random.randint(0, board.rows - 1)
    board.board[bomb_y][bomb_x] = Obstacles.BOMB

# Score functions
def add_score(score, board, snake):
    head = snake.get_head()
    score.add_score(board.board[head[1]][head[0]])