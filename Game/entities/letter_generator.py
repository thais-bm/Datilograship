import random, math

from entities.entity_base import Entity
from entities.letter import Letter

from managers.game_manager import Game_Manager

class Letter_Generator(Entity):
    def __init__(self, layer = 0):
        super().__init__((0,0), layer)

        self.default_time_to_next_letter = 300
        self.time_to_next_letter = 0

        self.spawn_distance = Game_Manager.screen_width

    def process(self):
        self.time_to_next_letter -= Game_Manager.game_speed
        if self.time_to_next_letter <= 0:
            self.time_to_next_letter = self.default_time_to_next_letter
            self.spawn_letter()

    def spawn_letter(self):
        letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                    'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        letter = random.choice(letters)

        direction = random.randint(0,359)
        x = Game_Manager.player.center[0] + math.sin(math.radians(direction)) * self.spawn_distance
        y = Game_Manager.player.center[1] + math.cos(math.radians(direction)) * self.spawn_distance

        x = min(max(x,0), Game_Manager.screen_width)
        y = min(max(y,0), Game_Manager.screen_height)

        Letter(letter, (x,y))

