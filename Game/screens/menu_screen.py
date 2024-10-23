import pygame

import managers.game_manager as mng

from entities.text import Text
from entities.key_listener import KeyListener
from entities.button import Button

from screens.screen_base import Screen

from resource.color import *
from resource.fonts import *
from resource.sound import *

class Menu_Screen(Screen):
    def populate(self):
        # Start Background music
        pygame.mixer.Sound.play(BACKGROUND, loops=-1)

        # Esc Listener
        self.exit_listener = KeyListener([pygame.K_ESCAPE], [mng.Game_Manager.close_game])

        # Game name in Menu
        self.title = Text(content = mng.Game_Manager.game_name, 
                              center=(mng.Game_Manager.screen_width//4.5, mng.Game_Manager.screen_height//4),
                              size = 60,
                              font = SEGA,
                              color = WHITE)
        
        # Play button
        self.play_button = Button(content = "Play",
                                      center = (mng.Game_Manager.screen_width//4.5, 420),
                                      size = 50,
                                      font = SEGA,
                                      color = WHITE)
        
        # Registering reactions for starting hovering it
        self.play_button.on_hover_enter.append(lambda: self.play_button.change_text("- " + self.play_button.content))
        self.play_button.on_hover_enter.append(lambda: self.play_button.change_color(PINK))
        self.play_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        # Registering reactions for stopping hovering it
        self.play_button.on_hover_exit.append(lambda: self.play_button.change_text(self.play_button.content.replace('- ', '')))
        self.play_button.on_hover_exit.append(lambda: self.play_button.change_color(WHITE))

        # Registering reactions for clicking it
        self.play_button.on_click.append(lambda: print("Play"))
        
        # Exit button
        self.exit_button = Button(content = "Exit",
                                      center = (mng.Game_Manager.screen_width//4.5, 480),
                                      size = 50,
                                      font = SEGA,
                                      color = WHITE)
        
        # Registering reactions for starting hovering it
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.change_text("- " + self.exit_button.content))
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.change_color(PINK))
        self.exit_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        # Registering reactions for stopping hovering it
        self.exit_button.on_hover_exit.append(lambda: self.exit_button.change_text(self.exit_button.content.replace('- ', '')))
        self.exit_button.on_hover_exit.append(lambda: self.exit_button.change_color(WHITE))
        
        # Registering reactions for clicking it
        self.exit_button.on_click.append(mng.Game_Manager.close_game)