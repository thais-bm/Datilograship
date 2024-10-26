from screens.screen_base import Screen

from managers.game_manager import Game_Manager

from entities.keyboard import Keyboard
from entities.image import Image
from entities.text import Text
import managers.game_manager as mng


import pygame
from entities.key_listener import KeyListener
from resource.fonts import *
from resource.color import *
from screens.game_screen import Game_Screen


class Tutorial_Screen(Screen):
    def populate(self):
        self.keyboard = Keyboard(Game_Manager.screen_width * 0.2, Game_Manager.screen_height * 0.35)
        self.image = Image(path = "assets\Hand.png", 
                           center = (Game_Manager.screen_width * 0.7, Game_Manager.screen_height * 0.5),
                           width = Game_Manager.screen_width * 0.2,
                           height = Game_Manager.screen_height * 0.3)

        # ESC listener -> Close game
        # Enter keyboard Listener -> Go to game screen
        self.exit_listener = KeyListener([pygame.K_ESCAPE], [Game_Manager.close_game])
        self.enter_listener = KeyListener([pygame.K_RETURN], [lambda: mng.Game_Manager.change_screen(Game_Screen())])

        # Text setups
        self.title = Text(content = "Como jogar",
                              center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.1),
                              size = 60,
                              font = SEGA,
                              color = WHITE)
        self.say = Text(content="Seu objetivo é escrever as palavras e letras antes que",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.18),
                          size=40,
                          font=SANS,
                          color=WHITE)

        self.say2 = Text(content="elas cheguem até voce! Voce tem apenas 3 chances",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.23),
                          size=40,
                          font=SANS,
                          color=WHITE)

        self.say3 = Text(content="Aproveite o momento para testar o seu teclado",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.30),
                          size=40,
                          font=SANS,
                          color=WHITE)

        self.enter = Text(content = "Aperte ENTER para prosseguir",
                              center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.8),
                              size = 60,
                              font = SANS,
                              color = WHITE)

