from resource.color import *
from entities.text import Text

import pygame

class Button(Text):
    '''
    Shows Text on screen that reacts to hover and clicks

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
        super().__init__(content, center, size, font, color, layer)
        
        self.hovering = False
        self.on_hover_enter = []
        self.on_hover_exit = []
        self.on_hover = []

        self.on_click = []

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        if (self.rect.collidepoint(mouse_pos)):
            if not self.hovering:
                self.hovering = True
                for func in self.on_hover_enter:
                    func()
            for func in self.on_hover:
                func()
        elif self.hovering:
            self.hovering = False
            for func in self.on_hover_exit:
                func()

    def event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.rect.collidepoint(mouse_pos)):
                for func in self.on_click:
                    func()
