import pygame 
from screens.screen_base import Screen
from entities.keyboard import Keyboard
from entities.key_listener import KeyListener
from entities.image import Image

from managers.game_manager import Game_Manager
from screens.game_over_screen import Game_Over_Screen

class Game_Screen(Screen):
    def populate(self):
        # If music is being played on background -> Stop music
        if pygame.mixer.get_busy():
            pygame.mixer.stop()
        
        #Esc Listerner
        self.esc_listener = KeyListener([pygame.K_ESCAPE], [Game_Manager.close_game])
        
        #Keyboard
        self.keyboard = Keyboard(Game_Manager.screen_width * 0.35, Game_Manager.screen_height * 0.65)

        # Player debug image
        self.image = Image(path="assets\player.png",
                           center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.4),
                           width=Game_Manager.screen_width * 0.2,
                           height=Game_Manager.screen_height * 0.3)

        # Debug mode:
        self.enter_listener = KeyListener([pygame.K_RETURN], [lambda: Game_Manager.change_screen(Game_Over_Screen())])
        
        
