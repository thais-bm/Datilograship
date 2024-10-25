from screens.screen_base import Screen

from managers.game_manager import Game_Manager

from entities.keyboard import Keyboard
from entities.image import Image
from entities.text import Text

import pygame
from entities.key_listener import KeyListener
from resource.fonts import *
from resource.color import *


class Tutorial_Screen(Screen):
    def populate(self):
        self.keyboard = Keyboard(Game_Manager.screen_width * 0.2, Game_Manager.screen_height * 0.2)
        self.image = Image(path = "assets\Hand.png", 
                           center = (Game_Manager.screen_width * 0.7, Game_Manager.screen_height * 0.4),
                           width = Game_Manager.screen_width * 0.2,
                           height = Game_Manager.screen_height * 0.3)

        # Return/Enter keyboard Listener -> "Press enter to pass the tutorial"
        # Debug mode: It closes the game
        self.return_listener = KeyListener([pygame.K_RETURN], [Game_Manager.close_game])

        # Text setups
        self.title = Text(content = "Como jogar",
                              center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.1),
                              size = 60,
                              font = SEGA,
                              color = WHITE)
        self.say = Text(content="Teste o funcionamento do teu teclado aqui!",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.2),
                          size=40,
                          font=SEGA,
                          color=WHITE)
        self.enter = Text(content = "Aperte ENTER para prosseguir",
                              center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.8),
                              size = 60,
                              font = SEGA,
                              color = WHITE)