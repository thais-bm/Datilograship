from pygame import sprite
from entities.entity_base import Entity
from entities.text import Text
from entities.image import Image


# Just a scope of the player
# -> Life, Skin and position
class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.life = 3
        self.image = Image(path=image_path, center=center)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y