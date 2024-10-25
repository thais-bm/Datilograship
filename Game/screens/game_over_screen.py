from managers.game_manager import Game_Manager
import pygame

from screens.screen_base import Screen

from entities.text import Text
from entities.image import Image
from entities.key_listener import KeyListener

from resource.fonts import *
from resource.color import *
class Game_Over_Screen(Screen):

    def populate(self):

        self.defeat = Text(content="DERROTA",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.30),
                          size=70,
                          font=SEGA,
                          color=WHITE)

        self.image = Image(path="assets\player_defeat.png",
                           center=(Game_Manager.screen_width * 0.7, Game_Manager.screen_height * 0.5),
                           width=Game_Manager.screen_width * 0.2,
                           height=Game_Manager.screen_height * 0.3)

        self.go_back = Text(content = "Aperte ENTER para voltar ao menu principal",
                              center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.8),
                              size = 40,
                              font = SANS,
                              color = WHITE)

        # Trying to run away from circular import
        from screens.menu_screen import Menu_Screen
        self.return_listener = KeyListener([pygame.K_RETURN],
                                           [lambda: Game_Manager.change_screen(Menu_Screen())])

