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
        # If music is being played on background -> Stop music
        if pygame.mixer.get_busy():
            pygame.mixer.stop()

        #Esc Listerner
        self.esc_listener = KeyListener([pygame.K_ESCAPE], [Game_Manager.close_game])

        self.defeat = Text(content="VOCE MORREU",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.20),
                          size=70,
                          font=SEGA,
                          color=WHITE)
        
        self.points = Text(content="VOCE MARCOU "+str(Game_Manager.score)+" PONTOS",
                          center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.30),
                          size=70,
                          font=SEGA,
                          color=WHITE)

        self.image = Image(path="assets\player_assets\player_defeat.png",
                           center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.5),
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

