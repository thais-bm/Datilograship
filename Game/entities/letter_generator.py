import pygame,random, math

from entities.entity_base import Entity
from entities.letter import Word
from entities.key_listener import KeyListener

from resource.sound import *

from managers.game_manager import Game_Manager

class Letter_Generator(Entity):
    def __init__(self, layer = 0):
        super().__init__((0,0), layer)
        self.letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                        'Z', 'X', 'C', 'V', 'B', 'N', 'M']

        self.default_time_to_next_word = 300
        self.time_to_next_word = 0

        self.spawn_distance = Game_Manager.screen_width

        self.current_letters = {}

        for letter in self.letters:
            self.current_letters[letter] = ([],KeyListener([pygame.key.key_code(letter)],
                                                           [lambda pygame_smells = letter: self.on_letter_clicked(pygame_smells)]))
        

    def process(self):
        self.time_to_next_word -= 5 + Game_Manager.combo/50
        if self.time_to_next_word <= 0:
            self.time_to_next_word = self.default_time_to_next_word
            word = random.choice(self.letters)
            # These 2 lines are here just while we don't have a word system, to do multiletter
            for i in range(Game_Manager.combo//10):
                word += random.choice(self.letters)
            self.spawn_word(word)

    def spawn_word(self, text):
        direction = random.choice([random.randint(30,150),random.randint(210,330)])
        x = Game_Manager.player.center[0] + math.sin(math.radians(direction)) * self.spawn_distance
        y = Game_Manager.player.center[1] + math.cos(math.radians(direction)) * self.spawn_distance

        x = min(max(x,0), Game_Manager.screen_width)
        y = min(max(y,0), Game_Manager.screen_height)

        word = Word(text, (x,y))

        self.current_letters[word.current_letter.upper()][0].append(word)
        
    def on_letter_clicked(self, letter):
        pygame.mixer.Sound.play(KEYBOARD_TYPING)
        if len(self.current_letters.get(letter.upper())[0]) > 0:
            pygame.mixer.Sound.play(PLAYER_HIT)
            words = self.current_letters.get(letter.upper())[0].copy()
            for word in words:
                self.current_letters[word.current_letter.upper()][0].remove(word)

                Game_Manager.player.rotate(word.text.center)
                Game_Manager.increase_combo()
                Game_Manager.increase_score(Game_Manager.combo)


                if len(word.word) > 1:
                    word.word = word.word[1:]
                    word.current_letter = word.word[0]
                    self.current_letters[word.current_letter.upper()][0].append(word)
                    word.refresh()
                else:
                    word.destroy()
        else:
            Game_Manager.player.take_damage()
            Game_Manager.reset_combo()
        
