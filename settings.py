import pygame
from game_enums import *

class Settings():
    def __init__(self, debug_mode, size:Board_Size, font) -> None:
        """"Initialize game settings"""
        # Debug settings
        self.debug_mode = debug_mode
        self.board_size = size

        # self.screen_height = 750 if size.name == 'LARGE' else size.value * 100
        # self.screen_width = size.value * 100
        self.screen_height = size.value[1] * 100
        self.screen_width = size.value[0] * 100

        # screen settings
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background_color = Colors.LIGHT_BLUE.value

        self.valid_key_events = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN,
                                 pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s]

        # timer settings
        self.INACTIVE_EVENT = pygame.USEREVENT + 1
        self.inactive_timeout = 1100 # in milliseconds (1 second)
        pygame.time.set_timer(self.INACTIVE_EVENT, self.inactive_timeout)

        # text attibutes
        self.title_font = font.SysFont('Arial', 60)
        self.score_font = font.SysFont('Arial', 60)
        self.game_over_font = font.SysFont('Arial', 60)

        self.image_scale = 50
        image_scale = 50

        # snake images configuration
        snake_body_image = pygame.image.load('images/snake_body.png').convert_alpha()
        self.scaled_body_image = pygame.transform.scale(snake_body_image, (image_scale, image_scale))

        snake_head_image = pygame.image.load('images/snake_head.xcf').convert_alpha()
        self.scaled_head_image = pygame.transform.scale(snake_head_image, (image_scale, image_scale))

        # different snake heads based on direction
        self.scaled_right_head_image = pygame.transform.rotate(self.scaled_head_image, 0)
        self.scaled_left_head_image = pygame.transform.flip(self.scaled_head_image, True, False)
        self.scaled_up_head_image = pygame.transform.rotate(self.scaled_head_image, 90)
        self.scaled_down_head_image = pygame.transform.rotate(self.scaled_head_image, 270)

        # fruit image configuration
        apple_image = pygame.image.load('images/red_apple.png').convert_alpha()
        self.scaled_apple_image = pygame.transform.scale(apple_image, (image_scale, image_scale))

        pineapple_image = pygame.image.load('images/pineapple.png').convert_alpha()
        self.scaled_pineapple_image = pygame.transform.scale(pineapple_image, (image_scale, image_scale))

        cherry_image = pygame.image.load('images/cherry.png').convert_alpha()
        self.scaled_cherry_image = pygame.transform.scale(cherry_image, (image_scale, image_scale))

        # bomb image configurations
        bomb_image = pygame.image.load('images/bomb.png').convert_alpha()
        self.scaled_bomb_image = pygame.transform.scale(bomb_image, (image_scale, image_scale))

        # sound files configuration
        # self.main_game_music = pygame.mixer.music.load('media/main_game_music.mp3')
        self.game_over_sound = pygame.mixer.Sound('media/game_over_sound.wav')
        self.bomb_sound = pygame.mixer.Sound('media/bomb_sound_effect.flac')