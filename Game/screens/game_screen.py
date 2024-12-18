import pygame 
from screens.screen_base import Screen
from entities.key_listener import KeyListener
from entities.player import Player
from entities.text import Text
from entities.image import Image
from entities.letter_generator import Letter_Generator
from entities.keyboard import Keyboard
from entities.button import Button
import entities.explosion as explosion

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

            pygame.mixer.music.load('assets\\audio_assets\\Airship (Super Mario Bros) LOOP START.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.load('assets\\audio_assets\\Airship (Super Mario Bros) LOOP.mp3')
            pygame.mixer.music.play(-1)

        self.image = Image(path="assets/game_background.jpg",
                            center=(Game_Manager.screen_width * 0.5,Game_Manager.screen_height * 0.5),
                            width=Game_Manager.screen_width,
                            height=Game_Manager.screen_height)


      #Esc Listerner
        self.esc_listener = KeyListener([pygame.K_ESCAPE], [lambda: Game_Manager.pause_game()])
          

        # Player
        self.player = Player(sprite_path="assets\player_assets\player.png",
                           center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.5),
                           width=Game_Manager.screen_width * 0.100,
                           height=Game_Manager.screen_height * 0.128)
        Game_Manager.player = self.player


        self.letter_generator = Letter_Generator()

        #Esc text
        self.enter = Text(content = "Aperte ESC para pausar e despausar",
                              center=(Game_Manager.screen_width * 0.12, Game_Manager.screen_height * 0.97),
                              size = 18,
                              font = SANS,
                              color = WHITE)
        
        #Esc Button
        self.exit_button = Button(content = "Exit",
                                      center = (Game_Manager.screen_width * 0.05, Game_Manager.screen_height * 0.03),
                                      size = 50,
                                      font = SEGA,
                                      color = BLACK
                                    )
    
        
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.text.change_text(self.exit_button.text.content))
        self.exit_button.on_hover_enter.append(lambda: self.exit_button.text.change_color(PINK))
        self.exit_button.on_hover_enter.append(lambda: DECISION.play(0,0))

        self.exit_button.on_hover_exit.append(lambda: self.exit_button.text.change_text(self.exit_button.text.content.replace('- ', '')))
        self.exit_button.on_hover_exit.append(lambda: self.exit_button.text.change_color(BLACK))
        
        self.exit_button.on_click.append(Game_Manager.close_game)
        self.exit_button.on_click.append(lambda: pygame.mixer.music.unload())
        
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

        self.process.append(explosion.tick_all_explosions)
        
        self.indicador_text = Text(content=f"INDICADOR",
                          center=(Game_Manager.screen_width * 0.9, Game_Manager.screen_height * 0.75),
                          size=40,
                          font=ANGRY_BIRDS,
                          color=BLUE)
        self.medio_text = Text(content=f"MEDIO",
                          center=(Game_Manager.screen_width * 0.9, Game_Manager.screen_height * 0.80),
                          size=40,
                          font=ANGRY_BIRDS,
                          color=ORANGE)
        self.anelar_text = Text(content=f"ANELAR",
                          center=(Game_Manager.screen_width * 0.9, Game_Manager.screen_height * 0.85),
                          size=40,
                          font=ANGRY_BIRDS,
                          color=YELLOW)
        self.midinho_text = Text(content=f"MIDINHO",
                          center=(Game_Manager.screen_width * 0.9, Game_Manager.screen_height * 0.90),
                          size=40,
                          font=ANGRY_BIRDS,
                          color=PINK)

        # Debug mode:
        # self.enter_listener = KeyListener([pygame.K_RETURN], [lambda: Game_Manager.change_screen(Game_Over_Screen())])

    def update_life(self):
        if Game_Manager.game_started == False:
            return
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
                
    
        
        
    
