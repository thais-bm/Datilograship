from resource.color import *
from entities.entity_base import Entity

from managers.game_manager import Game_Manager

import pygame
import resource.fonts as fonts
import resource.color as colors

class Keyboard(Entity):
    def __init__(self, x, y, layer = 0):
        super().__init__(layer)

        self.x = x
        self.y = y

        self.pressed_keys = {}
        # Add colors to each key latter
        self.key_colors = {}
        self.key_size = (40, 40)
        self.space_size = (280, 40)
        self.caps_size = (30,30)
        self.container_rect = pygame.Rect(100, 100, 500, 200)
        self.keyboard = self.keyboard_layout() 

            
    def event(self, event):
        if event.type == pygame.KEYDOWN:
            # Mods check to see if caps lock is on
            mods = pygame.key.get_mods()

            letters = [
                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                ['CAPS LOCK', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç'],
                ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
                ['SPACE']
            ]

            # Trying to add Unicode char
            if event.unicode and event.unicode is not ' ':
                key_char = event.unicode
            else:
                key_char = pygame.key.name(event.key)

            # debug: key_char
            print(key_char,"Pressed")
            
            if mods and pygame.KMOD_CAPS and key_char.isalpha():
                key_char = key_char.upper()
            else:
                key_char = key_char.lower()

            # Update pressed key
            self.pressed_keys[key_char] = True

        # The key is not being pressed
        elif event.type == pygame.KEYUP:
            if event.unicode and event.unicode is not ' ':
                key_char = event.unicode
            else:
                key_char = pygame.key.name(event.key)

            # debug: key_char
            print(key_char,"Released")

            self.pressed_keys[key_char.lower()] = False
            self.pressed_keys[key_char.upper()] = False

            
    def keyboard_layout(self):
        layout = []
        
        letters = [
                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                ['CAPS LOCK', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç'],
                ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
                ['SPACE']
        ]

        for i, row in enumerate(letters):
            for j, key in enumerate(row):
                # Each i is a row of lists, gives it a stairs look
                # i == 1 is the second list
                if i == 1:  
                    x = self.x - 45 + (j * (self.key_size[0] + 10)) + (self.key_size[0] // 2)
                elif i == 2:  
                    x = self.x + 30 + (j * (self.key_size[0] + 10)) + (self.key_size[0] // 4)
                elif i == 3:
                    x = self.x + 60 + (j * (self.key_size[0] + 10)) + (self.key_size[0] // 4)
                else:
                    x = self.x + j * (self.key_size[0] + 10)

                y = self.y + i * (self.key_size[1] + 10)
                layout.append((key, x, y))
                
        return layout
        
    def draw(self, screen):
        font = pygame.font.SysFont(fonts.SEGA, 30)
        small_font = pygame.font.SysFont(fonts.SEGA, 20) 
        
        for key, x, y in self.keyboard:
            key_x = self.container_rect.x + x
            key_y = self.container_rect.y + y

            color = Game_Manager.get_key_color(key)
            
            if self.pressed_keys.get(key.lower(), False): 
                color = colors.GREEN
            if self.pressed_keys.get(key.upper(), False):
                color = colors.GREEN

            if key == 'SPACE':
                pygame.draw.rect(screen, color, (key_x, key_y, *self.space_size))
                pygame.draw.rect(screen, colors.BLACK, (key_x, key_y, *self.space_size), 2)
                label = font.render(key, True, colors.BLACK)
                label_rect = label.get_rect(center=(key_x + self.space_size[0] // 2, key_y + self.space_size[1] // 2))
                screen.blit(label, label_rect)
                
            elif key == 'CAPS LOCK':
                pygame.draw.rect(screen, color, (key_x, key_y, *self.key_size))
                pygame.draw.rect(screen, colors.BLACK, (key_x, key_y, *self.key_size), 2)

                caps_label = small_font.render("CAPS", True, colors.BLACK)
                lock_label = small_font.render("LOCK", True, colors.BLACK)

                caps_rect = caps_label.get_rect(center=(key_x + self.key_size[0] // 2, key_y + self.key_size[1] // 3))
                lock_rect = lock_label.get_rect(center=(key_x + self.key_size[0] // 2, key_y + 2 * self.key_size[1] // 3))

                screen.blit(caps_label, caps_rect)
                screen.blit(lock_label, lock_rect)
                  

            else:
                # The * symbol unpacks the values
                pygame.draw.rect(screen, color, (key_x, key_y, *self.key_size))
                pygame.draw.rect(screen, colors.BLACK, (key_x, key_y, *self.key_size), 2)
                label = font.render(key, True, colors.BLACK)

                label_rect = label.get_rect(center=(key_x + self.key_size[0] // 2, key_y + self.key_size[1] // 2))
                screen.blit(label, label_rect)     