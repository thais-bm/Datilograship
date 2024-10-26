from pygame import sprite
from entities.entity_base import Entity
from entities.text import Text
from entities.image import Image

import pygame

# Just a scope of the player
# -> Life, Skin and position
class Player(Entity):
    def __init__(self, center, sprite_path, hitbox = None, width = None, height = None, layer = 1):
        super().__init__(layer = layer)
        self.life = 3
        self.sprite = Image(path = sprite_path, center = center, width = width, height = height)

        self.angle = -90

        if hitbox == None:
            hitbox = self.sprite.image.get_rect()
            

    def life_Bar(self):
        self.heart_full = pygame.image.load("assets/player_assets/life_0.png").convert_alpha()
        self.heart_empty = pygame.image.load("assets/player_assets/life_1.png").convert_alpha()