import managers as mng
from constants.color import *

import pygame

class Base():
    def __init__(self, layer):
        self.layer = layer
        mng.Game_Manager.current_screen.add_item(self, layer)

    def event(self, event):
        pass
    
    def destroy(self):
        mng.Game_Manager.current_screen.remove_item(self, self.layer)

    def process(self):
        pass
    
    def draw(self, screen):
        pass

class Text(Base):
    def __init__(self, content, center, size, font, color, layer = 2):
        super().__init__(layer)
        self.content = content
        self.color = color

        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(content, True, color)
        self.rect = self.text.get_rect(center = center)

    def change_text(self, new_text):
        self.text = self.font.render(new_text, True, self.color)
        self.rect = self.text.get_rect(center = self.rect.center)

    def change_color(self, new_color):
        self.text = self.font.render(self.content, True, new_color)
        self.rect = self.text.get_rect(center = self.rect.center)

    def draw(self, screen):
        screen.blit(self.text, self.rect)

class Button(Text):
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

class KeyListener(Base):
    def __init__(self, keys = [], actions = [], layer = 0):
        super().__init__(layer)
        self.keys = keys
        self.actions = actions

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.keys:
                for action in self.actions:
                    action()