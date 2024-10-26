import pygame

from resource.fonts import *
from resource.color import *

from managers.game_manager import Game_Manager

from entities.entity_base import Entity
from entities.key_listener import KeyListener
from entities.text import Text

class Letter(Entity):
    def __init__(self, letter, center, layer = 1):
        super().__init__(layer)
        self.text = Text(content = letter,
                         center = center,
                         size = 20,
                         font = SEGA,
                         color = WHITE)
        self.click_listener = KeyListener([pygame.key.key_code(letter)],
                                          self.on_letter_clicked)
        
    def process(self):
        #making the letter track the player will be kind of dificult
        #so i will do it later
        pass

        
    def on_letter_clicked(self):
        self.destroy()
        Game_Manager.increase_combo()
        Game_Manager.increase_score(Game_Manager.combo)