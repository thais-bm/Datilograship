import pygame 
from screens.screen_base import Screen
from entities.key_listener import KeyListener
from entities.player import Player
from entities.text import Text
from entities.image import Image
from entities.letter_generator import Letter_Generator
from entities.keyboard import Keyboard

from managers.game_manager import Game_Manager
from screens.game_over_screen import Game_Over_Screen

from resource.color import *
from resource.fonts import *
from resource.sound import *


class Game_Screen(Screen):
    def populate(self):
        # If music is being played on background -> Stop music
        if pygame.mixer.get_busy():
            pygame.mixer.stop()


        #Esc Listerner
        self.esc_listener = KeyListener([pygame.K_ESCAPE], [Game_Manager.close_game])

        # Player
        self.player = Player(sprite_path="assets\player_assets\player.png",
                           center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.5),
                           width=Game_Manager.screen_width * 0.100,
                           height=Game_Manager.screen_height * 0.128)
        Game_Manager.player = self.player


        self.letter_generator = Letter_Generator()

        # Score Text
        self.score_text = Text(content=f"Score: "+str(Game_Manager.score),
                          center=(Game_Manager.screen_width * 0.1, Game_Manager.screen_height * 0.1),
                          size=70,
                          font=ANGRY_BIRDS,
                          color=WHITE)
        self.process.append(lambda: self.score_text.change_text(f"Score: "+str(Game_Manager.score)))
        # Combo Text
        self.combo_text = Text(content=f"Combo: "+str(Game_Manager.combo),
                          center=(Game_Manager.screen_width * 0.1, Game_Manager.screen_height * 0.15),
                          size=70,
                          font=ANGRY_BIRDS,
                          color=WHITE)
        self.process.append(lambda: self.combo_text.change_text(f"Combo: "+str(Game_Manager.combo)))
        
        self.hearts = [None, None, None]
        self.process.append(self.update_life)

        # Debug mode:
        # self.enter_listener = KeyListener([pygame.K_RETURN], [lambda: Game_Manager.change_screen(Game_Over_Screen())])

    def update_life(self):
        for i in range(3):
            if i + 1 <= Game_Manager.player.life:
                path = "assets/player_assets/life_0.png"
            else:
                path = "assets/player_assets/life_1.png"
            if self.hearts[i] == None:
                self.hearts[i] = (Image(path = path, 
                                    center = (Game_Manager.screen_width * (0.7 + 0.1 * i), Game_Manager.screen_height * 0.15)))
            elif self.hearts[i].path != path:
                self.hearts[i].destroy()
                self.hearts[i] = (Image(path = path, 
                                    center = (Game_Manager.screen_width * (0.7 + 0.1 * i), Game_Manager.screen_height * 0.15)))
        
        
        
