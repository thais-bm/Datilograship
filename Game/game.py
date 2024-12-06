import pygame
pygame.init()

import sys, os

folder_path = os.path.dirname(__file__)
os.chdir(folder_path)

from resource.color import *
from resource.fonts import *
from entities.explosion import render_all_explosions

from managers.game_manager import Game_Manager
from screens.menu_screen import Menu_Screen


# Screen Setup
# setting the game screen to the size of the computer screen
# every size and position have to be a value from 0 to 1 multiplied by screen heigth or width
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w * 1, info_object.current_h * 1))
Game_Manager.update_screen_size()

Game_Manager.change_game_name("DATILOGRASHIP")
Game_Manager.change_screen(Menu_Screen())  # Here we set the screen to be a new Menu_Screen

pause_screen = pygame.image.load("assets/other_assets/pause.jpg")
pause_screen = pygame.transform.scale(pause_screen, screen.get_size())

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
            
    if Game_Manager.game_started:
        render_all_explosions(screen)

    # The third thing that will be checked are what processes are registered on the current screen
    for process in Game_Manager.current_screen.process:
        process()
    if Game_Manager.game_paused == True:
        screen.blit(pause_screen, (0,0))
    
    pygame.display.flip()
    game_clock.tick(60)


pygame.quit()
sys.exit()
