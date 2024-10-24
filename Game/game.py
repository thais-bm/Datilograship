import pygame
pygame.init()

import sys, os
from resource.color import *
from resource.fonts import *

from screens.menu_screen import Menu_Screen
from managers.game_manager import Game_Manager

folder_path = os.path.dirname(__file__)
os.chdir(folder_path)

# Screen Setup
# setting the game screen to the size of the computer screen
# every size and position have to be a value from 0 to 1 multiplied by screen heigth or width
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w * 1, info_object.current_h * 1))
Game_Manager.update_screen_size()

Game_Manager.change_game_name("Jogo sem nome aff")
Game_Manager.change_screen(Menu_Screen()) # Here we set the screen to be a new Menu_Screen

# Game loop setup
Game_Manager.game_loop = True
game_clock = pygame.time.Clock()

while Game_Manager.game_loop:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Manager.close_game()
        
        # The first thing that will be checked are what events are registered on the current screen
        for event_func in Game_Manager.current_screen.event:
            event_func(event)

    # The second thing that will be checked are what drawings are registered on the current screen
    # The drawings will be read in layer order, 0 -> 1 -> 2, with the rightest coming on top
    for layer in Game_Manager.current_screen.draw:
        for draw in layer:
            draw(screen)

    # The third thing that will be checked are what processes are registered on the current screen
    for process in Game_Manager.current_screen.process:
        process()

    pygame.display.flip()
    game_clock.tick(60)


pygame.quit()
sys.exit()
