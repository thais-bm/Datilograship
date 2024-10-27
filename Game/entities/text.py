from resource.color import *

import pygame
from entities.entity_base import Entity

class Text(Entity):
    '''
    Shows Text on screen

    Attributes
    ----------
    content:
        The text to be shown
    center:
        The center position of the textbox
    size:
        The font size
    font:
        Which font should be used on the text
    color:
        The text's color
    '''
    def __init__(self, content, center, size, font, color, layer = 2):
        super().__init__(layer)
        # Saving some of the atributes for remote changing
        self.content = content
        self.color = color
        self.center = center

        # Setting up a text object
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(content, True, color)
        self.rect = self.text.get_rect(center = center)

    def change_text(self, new_text):
        '''Change and re-setup the text with another content'''
        self.text = self.font.render(new_text, True, self.color)
        self.rect = self.text.get_rect(center = self.rect.center)

    def change_color(self, new_color):
        '''Change and re-setup the text with another color'''
        self.text = self.font.render(self.content, True, new_color)
        self.rect = self.text.get_rect(center = self.rect.center)

    def draw(self, screen):
        screen.blit(self.text, self.rect)
