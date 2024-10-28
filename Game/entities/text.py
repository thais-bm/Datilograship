from resource.color import *

import pygame
from entities.entity_base import Entity
from managers.game_manager import Game_Manager

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
        super().__init__(center, layer)
        # Saving some of the atributes for remote changing
        self.content = content
        self.color = color

        # Setting up a text object
        self.font = pygame.font.Font(font, size)
        self.change_text(content)

    def change_text(self, new_text):
        '''Change and re-setup the text with another content'''
        self.content = new_text
        self.text = self.font.render(new_text, True, self.color)
        self.refresh()

    def change_color(self, new_color):
        '''Change and re-setup the text with another color'''
        self.text = self.font.render(self.content, True, new_color)
        self.refresh()

    def refresh(self):
        self.rect = self.text.get_rect()
        Game_Manager.center_to_rect(self.rect, self.center)

    def draw(self, screen):
        screen.blit(self.text, self.rect)
