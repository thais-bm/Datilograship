from pygame import sprite
from entities.entity_base import Entity
from entities.text import Text
from entities.image import Image

import pygame

# Just a scope of the player
# -> Life, Skin and position
class Player():
    def __init__(self, center):
        self.life = 3
        self.score = 0
        self.combo = 10
        # self.rect = self.image.get_rect()
        # self.rect.x = center[0]
        # self.rect.y = center[1]

    def life_Bar(self):
        self.heart_full = pygame.image.load("assets/player_assets/life_0.png").convert_alpha()
        self.heart_empty = pygame.image.load("assets/player_assets/life_1.png").convert_alpha()