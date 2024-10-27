from entities.entity_base import Entity
from entities.image import Image
import math
import pygame

class Player(Entity):
    def __init__(self, center, sprite_path, hitbox = None, width = None, height = None, layer = 1):
        super().__init__(layer = layer)
        self.life = 3
        self.sprite = Image(path = sprite_path, center = center, width = width, height = height)
        self.base_sprite = self.sprite.image

        self.center = center

        self.angle = -90

        if hitbox == None:
            hitbox = self.sprite.image.get_rect()
    #function to rotate player shooty thing sprite to aim for specified coordinates
    def rotate(self, target_pos):
        dx = target_pos[0] - self.center[0]
        dy = target_pos[1] - self.center[1]
        tan = dx/dy
        self.angle = math.degrees(math.atan(tan))

        self.sprite.image = pygame.transform.rotate(self.base_sprite, self.angle)