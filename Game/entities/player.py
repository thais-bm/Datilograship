from pygame import sprite
from entities.entity_base import Entity
from entities.text import Text
from entities.image import Image


# Just a scope of the player
# -> Life, Skin and position
class Player(sprite.Sprite):
    def __init__(self, center):
        sprite.Sprite.__init__(self)
        self.life = 3
        self.image = Image(path='./assets/player.png', center=center)
        self.rect = self.image.get_rect()
        self.rect.x = center[0]
        self.rect.y = center[1]