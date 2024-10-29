from entities.entity_base import Entity
from entities.image import Image

from managers.game_manager import Game_Manager

from resource.sound import *

import math
import pygame

class Player(Entity):
    def __init__(self, center, sprite_path, hitbox = None, width = None, height = None, layer = 1):
        super().__init__(center, layer = layer)
        pygame.mixer.init()
        self.life = 3
        self.sprite = Image(path = sprite_path, center = center, width = width, height = height)
        self.base_sprite = self.sprite.image
        self.angle = -90
        self.hitbox = hitbox
        if self.hitbox == None:
            self.hitbox = self.sprite.image.get_rect()
        Game_Manager.center_to_rect(self.hitbox, center)

    #function to rotate player shooty thing sprite to aim for specified coordinates
    def rotate(self, target_pos):
        if Game_Manager.game_started == False:
            return
        dx = target_pos[0] - self.center[0]
        dy = target_pos[1] - self.center[1]
        self.angle = math.degrees(math.atan2(dx, dy))

        self.sprite.image = pygame.transform.rotate(self.base_sprite, self.angle)
        self.hitbox = self.sprite.image.get_rect()
        Game_Manager.center_to_rect(self.hitbox, self.center)

    def take_damage(self):
        if Game_Manager.game_started == False:
            return
        self.life -= 1
        pygame.mixer.Sound.play(PLAYER_DMG)
        if self.life <= 0:
            pygame.mixer.Sound.play(PLAYER_DEFEAT)
            Game_Manager.game_over()

    # Uncomment this code if you want to vizualize player hitbox
    #
    #def draw(self, screen):
    #    pygame.draw.rect(screen,(255,255,255),self.hitbox)
        