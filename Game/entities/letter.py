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
                         size = 60,
                         font = SANS,
                         color = Game_Manager.get_key_color(letter))
        self.click_listener = KeyListener([pygame.key.key_code(letter)],
                                          [self.on_letter_clicked])
        
    def process(self):
        diff_tuple = (self.text.center[0] - Game_Manager.player.center[0], self.text.center[1] - Game_Manager.player.center[1])
        diff_vector = pygame.Vector2(diff_tuple)
        normalized_diff_vector = diff_vector.normalize()
        self.text.rect.center = self.text.rect.center - normalized_diff_vector * Game_Manager.game_speed
        
    def destroy(self):
        self.text.destroy()
        super().destroy()

    def on_letter_clicked(self):
        Game_Manager.player.rotate(self.text.center)
        self.destroy()
        Game_Manager.increase_combo()
        Game_Manager.increase_score(Game_Manager.combo)