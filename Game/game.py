import pygame
pygame.init()

import sys

from constants.color import *
from constants.fonts import *
from constants.sound import *

import screens
from managers import Game_Manager


# Text setups + sfx setups
play_text = 'PLAY'
exit_text = 'EXIT'
bg = pygame.image.load("assets/menu_assets/img.png")
pygame.mixer.Sound.play(BACKGROUND, loops=-1)

# Screen Setup
# setting the game screen to the size of the computer screen
# every size and position have to be a value from 0 to 1 multiplied by screen heigth or width
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w, info_object.current_h))
Game_Manager.update_screen_size()

Game_Manager.change_screen(screens.Menu_Screen())
Game_Manager.change_game_name("Jogo sem nome aff")

# Game loop setup
Game_Manager.game_loop = True
ins = True
game_clock = pygame.time.Clock()


while Game_Manager.game_loop:
    screen.fill(BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Manager.close_game()
                
        for event_func in Game_Manager.current_screen.event:
            event_func(event)

    for layer in Game_Manager.current_screen.draw:
        for draw in layer:
            draw(screen)

    for process in Game_Manager.current_screen.process:
        process()

    pygame.display.flip()
    game_clock.tick(60)


pygame.quit()
sys.exit()
