from resource.color import *
from entities.entity_base import Entity
from entities.text import Text
from entities.image import Image

import pygame

class Button(Entity):
    '''
    Shows a Button with image and text on screen that reacts to hover and clicks

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
    image_path:
        The path to the button's image, if not given the base button image will be used
    '''
    def __init__(self, center, size, font, color, content = "", image_path = "assets/Button_Base.png", layer = 2):
        self.image = Image(path = image_path, center = center)
        self.text = Text(content, center, size, font, color)

        super().__init__(layer)

        self.center = center

        self.hovering = False
        self.on_hover_enter = []
        self.on_hover_exit = []
        self.on_hover = []

        self.on_click = []

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        image_rect = self.image.image.get_rect()
        image_rect.center = self.center
        if (image_rect.collidepoint(mouse_pos)):
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
        image_rect = self.image.image.get_rect()
        image_rect.center = self.center
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (image_rect.collidepoint(mouse_pos)):
                for func in self.on_click:
                    func()
