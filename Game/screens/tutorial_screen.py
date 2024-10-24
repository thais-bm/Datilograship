from screens.screen_base import Screen

from managers.game_manager import Game_Manager

from entities.keyboard import Keyboard
from entities.image import Image
from entities.text import Text

class Tutorial_Screen(Screen):
    def populate(self):
        self.keyboard = Keyboard(Game_Manager.screen_width * 0.2, Game_Manager.screen_height * 0.2)
        self.image = Image(path = "assets\Hand.png", 
                           center = (Game_Manager.screen_width * 0.7, Game_Manager.screen_height * 0.4),
                           width = Game_Manager.screen_width * 0.2,
                           height = Game_Manager.screen_height * 0.3)