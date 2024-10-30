import pygame

from resource.fonts import *
from resource.color import *
from resource.sound import *

from managers.game_manager import Game_Manager

from entities.entity_base import Entity
from entities.text import Text
from entities.explosion import explosion

class Word(Entity):
    def __init__(self, word, center, layer = 1):
        super().__init__(center, layer)

        self.word = word
        self.current_letter = word[0]

        self.text = Text(content = word,
                         center = center,
                         size = 60,
                         font = ANGRY_BIRDS,
                         color = Game_Manager.get_key_color(self.current_letter))
        
        
    def process(self):
        if Game_Manager.game_started == False:
            return
        diff_tuple = (self.text.center[0] - Game_Manager.player.center[0], self.text.center[1] - Game_Manager.player.center[1])
        diff_vector = pygame.Vector2(diff_tuple)
        normalized_diff_vector = diff_vector.normalize()
        self.text.center = self.text.center - normalized_diff_vector * Game_Manager.game_speed
        self.text.refresh()

        if Game_Manager.player.hitbox.collidepoint(self.text.center):
            Game_Manager.player.take_damage()
            Game_Manager.reset_combo()
            self.destroy()
        
    def destroy(self):
        if Game_Manager.game_started == False:
            return
        explosion(self.text.center)
        self.text.destroy()
        super().destroy()

    def refresh(self):
        if Game_Manager.game_started == False:
            return
        self.text.change_text(self.word)
        self.text.change_color(Game_Manager.get_key_color(self.current_letter))
            
