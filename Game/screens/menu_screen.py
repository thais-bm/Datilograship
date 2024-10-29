import pygame

import managers.game_manager as mng

from entities.text import Text
from entities.key_listener import KeyListener
from entities.button import Button
from entities.image import Image

from screens.screen_base import Screen
from screens.tutorial_screen import Tutorial_Screen

from resource.color import *
from resource.fonts import *
from resource.sound import *

class Menu_Screen(Screen):
    def populate(self):
        # Start Background music - use of music for better peformance
        pygame.mixer.music.load('assets/menu_assets/title.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)

        self.image = Image(path="assets/menu_assets/background.png",
                           center=(mng.Game_Manager.screen_width * 0.5, mng.Game_Manager.screen_height * 0.5),
                           width=mng.Game_Manager.screen_width,
                           height=mng.Game_Manager.screen_height)

        # Esc Listener
        self.exit_listener = KeyListener([pygame.K_ESCAPE], [mng.Game_Manager.close_game])

        # Game name in Menu
        self.title = Text(content = mng.Game_Manager.game_name, 
                              center=(mng.Game_Manager.screen_width * 0.2, mng.Game_Manager.screen_height * 0.1),
                              size = 60,
                              font = SEGA,
                              color = WHITE)
        
        # Play button
        self.play_button = Button(content = "Play",
                                      center = (mng.Game_Manager.screen_width * 0.2, mng.Game_Manager.screen_height * 0.4),
                                      size = 50,
                                      font = SEGA,
                                      color = BLACK)
        
        # Registering reactions for starting hovering it
        self.play_button.on_hover_enter.append(lambda: self.play_button.text.change_text("- " + self.play_button.text.content))
        self.play_button.on_hover_enter.append(lambda: self.play_button.text.change_color(PINK))
        self.play_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        # Registering reactions for stopping hovering it
        self.play_button.on_hover_exit.append(lambda: self.play_button.text.change_text(self.play_button.text.content.replace('- ', '')))
        self.play_button.on_hover_exit.append(lambda: self.play_button.text.change_color(BLACK))

        # Registering reactions for clicking it
        self.play_button.on_click.append(lambda: mng.Game_Manager.change_screen(Tutorial_Screen()))
        self.play_button.on_click.append(lambda: pygame.mixer.music.unload())
        
        # Exit button
        self.exit_button = Button(content = "Exit",
                                      center = (mng.Game_Manager.screen_width * 0.2, mng.Game_Manager.screen_height * 0.5),
                                      size = 50,
                                      font = SEGA,
                                      color = BLACK)
        
        # Registering reactions for starting hovering it
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.text.change_text("- " + self.exit_button.text.content))
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.text.change_color(PINK))
        self.exit_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        # Registering reactions for stopping hovering it
        self.exit_button.on_hover_exit.append(lambda: self.exit_button.text.change_text(self.exit_button.text.content.replace('- ', '')))
        self.exit_button.on_hover_exit.append(lambda: self.exit_button.text.change_color(BLACK))
        
        # Registering reactions for clicking it
        self.exit_button.on_click.append(mng.Game_Manager.close_game)
        self.exit_button.on_click.append(lambda: pygame.mixer.music.unload())