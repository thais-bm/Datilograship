from managers.game_manager import Game_Manager
import pygame, os

from screens.screen_base import Screen

from entities.text import Text
from entities.image import Image
from entities.key_listener import KeyListener

from resource.fonts import *
from resource.color import *
class Score_Screen(Screen):

    def populate(self):
        # If music is being played on background -> Stop music
        if pygame.mixer.get_busy():
            pygame.mixer.stop()

        score_file = open("assets/sc_rec","r")
        scores = score_file.readlines()

        self.name = "_______"

        letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                        'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        for letter in letters:
            KeyListener([pygame.key.key_code(letter)],
                [lambda pygame_smells = letter: self.add_letter(pygame_smells)])

        self.ordened_scores = [(Game_Manager.score, self.name)]
        for line in scores:
            separated = line.split(";")
            self.ordened_scores.append((int(separated[1]),separated[0]))
        self.ordened_scores.sort(reverse = True)

        self.player_name = None

        score_start_y = 0.15
        spacing = 0.07

        self.position = ""

        Text(content="LEADERBOARD",
                    center=(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * (score_start_y - spacing * 1.5)),
                    size=70,
                    font=SEGA,
                    color=WHITE)

        for i in range(10):
            if len(self.ordened_scores) > i:
                if(self.ordened_scores[i][1] == "_______"):
                    self.position = str(i+1) + ". " 
                    self.player_name = Text(content=self.position + "_______",
                                            center=(Game_Manager.screen_width * 0.4, Game_Manager.screen_height * (score_start_y + spacing * i)),
                                            size=70,
                                            font=SEGA,
                                            color=WHITE)
                else:
                    Text(content=str(i+1) + ". " + self.ordened_scores[i][1],
                        center=(Game_Manager.screen_width * 0.4, Game_Manager.screen_height * (score_start_y + spacing * i)),
                        size=70,
                        font=SEGA,
                        color=WHITE)
                Text(content=str(self.ordened_scores[i][0]),
                    center=(Game_Manager.screen_width * 0.7, Game_Manager.screen_height * (score_start_y + spacing * i)),
                    size=70,
                    font=SEGA,
                    color=WHITE)
            else:
                Text(content="-------",
                        center=(Game_Manager.screen_width * 0.4, Game_Manager.screen_height * (score_start_y + spacing * i)),
                        size=70,
                        font=SEGA,
                        color=WHITE)
                Text(content="---",
                    center=(Game_Manager.screen_width * 0.7, Game_Manager.screen_height * (score_start_y + spacing * i)),
                    size=70,
                    font=SEGA,
                    color=WHITE)
            
        if self.player_name == None:
            self.player_name = Text(content="_______",
                                            center=(Game_Manager.screen_width * 0.4, Game_Manager.screen_height * (score_start_y + spacing * 11)),
                                            size=70,
                                            font=SEGA,
                                            color=WHITE)
            
            Text(content=str(Game_Manager.score),
                        center=(Game_Manager.screen_width * 0.7, Game_Manager.screen_height * (score_start_y + spacing * 11)),
                        size=70,
                        font=SEGA,
                        color=WHITE)

        self.return_listener = KeyListener([pygame.K_RETURN],
                                           [self.confirm])

    def add_letter(self, letter):
        new_name = ""
        imputed = False
        for old_letter in self.name:
            if old_letter != "_" or imputed:
                new_name += old_letter
            else:
                new_name += letter
                imputed = True
        self.name = new_name
        self.player_name.change_text(self.position + self.name)

    def confirm(self):
        # Trying to run away from circular import
        str_final = ""
        for score in self.ordened_scores:
            value = str(score[0])
            if score[1] == "_______":
                name = ""
                for old_letter in self.name:
                    if old_letter != "_":
                        name += old_letter
            else:
                name = score[1]
            str_final += name + ";" + value + "\n"
        file = open("assets/sc_rec","w")
        file.write(str_final.strip())

        from screens.menu_screen import Menu_Screen
        Game_Manager.change_screen(Menu_Screen())