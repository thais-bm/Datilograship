import pygame, math

from resource.fonts import *
from resource.color import *
from resource.sound import *

from managers.game_manager import Game_Manager

from entities.entity_base import Entity
from entities.key_listener import KeyListener
from entities.text import Text

class Letter(Entity):
    def __init__(self, letter, center, layer = 1):
        super().__init__(center, layer)

        self.text = Text(content = letter,
                         center = center,
                         size = 60,
                         font = RETRO_MARIO,
                         color = Game_Manager.get_key_color(letter))
        self.click_listener = KeyListener([pygame.key.key_code(letter)],
                                          [self.on_letter_clicked])
        
    def process(self):
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
        self.text.destroy()
        self.click_listener.destroy()
        super().destroy()

    def on_letter_clicked(self):
        Game_Manager.player.rotate(self.text.center)
        Game_Manager.increase_combo()
        Game_Manager.increase_score(Game_Manager.combo)
        pygame.mixer.Sound.play(PLAYER_HIT)
        self.destroy()