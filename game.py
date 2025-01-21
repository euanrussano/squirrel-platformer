from pgzero.loaders import sounds

from screens.game_screen import PlayScreen
from screens.main_menu import MainMenuScreen
from screens.game_over import GameOverScreen


class Game:
    def __init__(self):

        self.sound_on = True
        self.__music_on = True
        self.set_music_on(True)
        self.main_menu_state = MainMenuScreen(self)
        self.play_state = PlayScreen(self)
        self.game_over_state = GameOverScreen(self)  # Add this line to initialize game_over_state
        self.current_state = self.main_menu_state

    def reset(self):
        self.play_state.reset()

    @property
    def music_on(self):
        return self.__music_on

    def set_music_on(self, bool):
        self.__music_on = bool
        if bool:
            sounds.exploration.play(-1)
        else:
            sounds.exploration.stop()

    def set_state(self, state):
        self.current_state = state

    def draw(self, screen):
        self.current_state.draw(screen)

    def update(self, dt):
        self.current_state.update(dt)

    def on_mouse_down(self, pos):
        self.current_state.on_mouse_down(pos)
