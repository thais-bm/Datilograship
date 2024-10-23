import pygame

import managers as mng
import game_entities as ent

from constants.color import *
from constants.fonts import *
from constants.sound import *

class Screen():
    def __init__(self):
        self.process = []
        self.draw = [[],[],[]] # the draw function have 2 layers, the thing on the botton have to be in layer 0, the things on top on layer 1
        self.event = []

    def add_item(self, item, layer):
        self.process.append(item.process)
        self.draw[layer].append(item.draw)
        self.event.append(item.event)

    def remove_item(self, item, layer):
        try:
            self.process.remove(item.process)
        except:
            print("INFO: Process that is not here tried to me removed")
        try:
            self.draw[layer].remove(item.draw)
        except:
            print("INFO: Draw that is not here tried to me removed")
        try:
            self.event.remove(item.event)
        except:
            print("INFO: Event that is not here tried to me removed")


    def clear_screen(self):
        self.process.clear()
        for layer in self.draw:
            layer.clear()
        self.event.clear()

    def populate(self):
        pass

class Menu_Screen(Screen):
    def populate(self):
        # Esc Listener
        self.exit_listener = ent.KeyListener([pygame.K_ESCAPE], [mng.Game_Manager.close_game])

        # Game name in Menu
        self.title = ent.Text(content = mng.Game_Manager.game_name, 
                              center=(mng.Game_Manager.screen_width//4.5, mng.Game_Manager.screen_height//4),
                              size = 60,
                              font = SEGA,
                              color = WHITE)
        
        # Play button
        self.play_button = ent.Button(content = "Play",
                                      center = (mng.Game_Manager.screen_width//4.5, 420),
                                      size = 50,
                                      font = SEGA,
                                      color = WHITE)
        
        self.play_button.on_hover_enter.append(lambda: self.play_button.change_text("- " + self.play_button.content))
        self.play_button.on_hover_enter.append(lambda: self.play_button.change_color(PINK))
        self.play_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        self.play_button.on_hover_exit.append(lambda: self.play_button.change_text(self.play_button.content.replace('- ', '')))
        self.play_button.on_hover_exit.append(lambda: self.play_button.change_color(WHITE))

        self.play_button.on_click.append(lambda: print("Play"))
        
        # Exit button
        self.exit_button = ent.Button(content = "Exit",
                                      center = (mng.Game_Manager.screen_width//4.5, 480),
                                      size = 50,
                                      font = SEGA,
                                      color = WHITE)
        
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.change_text("- " + self.exit_button.content))
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.change_color(PINK))
        self.exit_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        self.exit_button.on_hover_exit.append(lambda: self.exit_button.change_text(self.exit_button.content.replace('- ', '')))
        self.exit_button.on_hover_exit.append(lambda: self.exit_button.change_color(WHITE))
        
        self.exit_button.on_click.append(mng.Game_Manager.close_game)