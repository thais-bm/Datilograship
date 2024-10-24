from screens.screen_base import Screen

class Game_Screen(Screen):
    def populate(self):
        self.keyboard = Keyboard(Game_Manager.screen_width * 0.5, Game_Manager.screen_height * 0.5)

        pass