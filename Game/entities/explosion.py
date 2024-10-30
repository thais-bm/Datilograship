import pygame

frame_1 = pygame.image.load("Game/assets/other_assets/KABOOM-1.png.png")
frame_2 = pygame.image.load("Game/assets/other_assets/KABOOM-2.png.png")
frame_3 = pygame.image.load("Game/assets/other_assets/KABOOM-3.png.png")
frame_4 = pygame.image.load("Game/assets/other_assets/KABOOM-4.png.png")
frame_5 = pygame.image.load("Game/assets/other_assets/KABOOM-5.png.png")
frame_6 = pygame.image.load("Game/assets/other_assets/KABOOM-6.png.png")
frame_7 = pygame.image.load("Game/assets/other_assets/KABOOM-7.png.png")
frame_8 = pygame.image.load("Game/assets/other_assets/KABOOM-8.png.png")
sprite_list_boom = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8]

explosion_square_size = frame_1.get_width()

active_explosions = []

sprite_change_time = 4

class explosion():
    def __init__(self, pos):
        self.rect = pygame.Rect(0, 0, explosion_square_size, explosion_square_size)
        self.rect.center = pos
        self.sprite_index = 0
        self.sprite = sprite_list_boom[self.sprite_index]
        active_explosions.append(self)
        self.frames_to_sprite_change = 0

    def behavior(self):
        global sprite_list_boom
        if self.frames_to_sprite_change <= sprite_change_time:
            self.frames_to_sprite_change += 1
        else:
            if self.sprite_index == 7:
                active_explosions.remove(self)
            else:
                self.sprite_index += 1
        
        self.sprite = sprite_list_boom[self.sprite_index]
    
    def render(self, screen):
        screen.blit(self.sprite, self.rect)

def tick_all_explosions():
    for boom in active_explosions:
        boom.behavior()

def render_all_explosions(screen):
    for boom in active_explosions:
        boom.render(screen)