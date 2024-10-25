import pygame 
from screens.screen_base import Screen
from entities.keyboard import Keyboard
from entities.key_listener import KeyListener

from managers.game_manager import Game_Manager

class Game_Screen(Screen):
    def populate(self):
        
        self.keyboard = Keyboard(Game_Manager.screen_width * 0.28, Game_Manager.screen_height * 0.65)
        self.return_listener = KeyListener([pygame.K_ESCAPE], [Game_Manager.close_game])
        
        
