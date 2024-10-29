import pygame

from resource.color import *

import screens

class Game_Manager():
    '''
    Class that manage everything that happens in game scope

    Attributes
    ----------
    game_started : bool
        True if the game is running, False otherwise
    game_loop : bool
        True if the app is running, False otherwise
    screen_width : float
        Width of the game screen
    screen_height : float
        Height of the game screen
    current_screen : Screen
        The screen being rendered at the moment
    game_name: string
        The title of the game

    Methods
    -------
    start_game()
        Run the game
    change_game_name(name)
        Change the name of the game and the display caption
    change_screen(screen)
        Change the current screen, getting rid of the old and populating the new
    update_screen_size()
        Catch the current screen size
    '''
    game_started = False
    game_loop = True

    screen_width = 0
    screen_height = 0

    current_screen = None

    game_name = ''

    player = None
    HUD = None
    score = 0
    combo = 0

    game_speed = 2

    def change_game_name(name):
        Game_Manager.game_name = name
        pygame.display.set_caption(name)

    def change_screen(screen):
        Game_Manager.current_screen = screen
        Game_Manager.current_screen.populate()

    def start_game():
        '''Run the game'''
        Game_Manager.combo = 0
        Game_Manager.score = 0
        Game_Manager.game_speed = 2

        Game_Manager.game_started = True
        Game_Manager.change_screen(screens.game_screen.Game_Screen())
    
    def game_over():
        '''End the game'''

        Game_Manager.game_started = False
        Game_Manager.change_screen(screens.game_over_screen.Game_Over_Screen())

    def close_game():
        '''Close the game'''
        Game_Manager.game_loop = False

    def update_screen_size():
        '''Catch the current screen size'''

        info = pygame.display.Info()
        Game_Manager.screen_width = info.current_w
        Game_Manager.screen_height = info.current_h

    def convert_to_relative_height(number, height):
        '''Convert a postion in a height to the same position in the screen height'''
        n_per_pixel = number / height
        return n_per_pixel * Game_Manager.screen_height
    
    def convert_to_relative_width(number, width):
        '''Convert a postion in a width to the same position in the screen width'''
        n_per_pixel = number / width
        return n_per_pixel * Game_Manager.screen_width
    
    def increase_combo(value = 1):
        Game_Manager.combo += value
        if Game_Manager.combo % 5 == 0:
            Game_Manager.game_speed += 1

    def increase_score(value):
        Game_Manager.score += value

    def reset_combo():
        Game_Manager.combo = 0
        Game_Manager.game_speed = 2

    def get_key_color(key):
        key = key.upper()  
        if key in 'XSW2LO9':
            return YELLOW
        elif key in 'AZQ1ÇP0': 
            return PINK
        elif key in ['CAPS LOCK', 'SHIFT']: 
            return PINK
        elif key in ['SPACE']:
            return CYAN
        elif key in 'VFR45TGBNHY67UJM':
            return BLUE
        elif key in 'CDE38IK':
            return ORANGE
        else:
            return WHITE  
        
    def center_to_rect(rect, center):
        x = round(center[0])
        y = round(center[1])
        rect.center = (x, y)