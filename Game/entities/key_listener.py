from resource.color import *
from entities.entity_base import Entity
from managers.game_manager import Game_Manager
import pygame

class KeyListener(Entity):
    '''
    Do action(s) when a key(s) is(are) pressed

    Attributes
    ----------
    keys:
        A list of keys that when pressed will make the action(s) play out
    actions:
        A list of actions that will happen if one of the registered keys is pressed
    '''
    def __init__(self, keys = [], actions = [], layer = 0):
        super().__init__((0,0), layer)
        self.keys = keys
        self.actions = actions

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.keys:
                for action in self.actions:
                    action()