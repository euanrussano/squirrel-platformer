from pgzero.loaders import sounds
from pgzero.rect import Rect


class MainMenuScreen:
    def __init__(self, game):
        self.game = game
        self.buttons = {
            "play": Rect((300, 200), (200, 50)),
            "music": Rect((300, 280), (200, 50)),
            "sound": Rect((300, 360), (200, 50)),
            "exit": Rect((300, 440), (200, 50)),
        }

    def draw(self, screen):
        screen.clear()
        screen.draw.text("MAIN MENU", center=(400, 100), fontsize=50, color="white")
        self._draw_button(screen, self.buttons["play"], "Play")
        self._draw_button(screen, self.buttons["music"], "Music: ON" if self.game.music_on else "Music: OFF")
        self._draw_button(screen, self.buttons["sound"], "Sound: ON" if self.game.sound_on else "Sound: OFF")
        self._draw_button(screen, self.buttons["exit"], "Exit")

    def update(self, dt):
        pass

    def on_mouse_down(self, pos):
        if self.buttons["play"].collidepoint(pos):
            self.game.set_state(self.game.play_state)
        elif self.buttons["music"].collidepoint(pos):
            self.game.set_music_on(not self.game.music_on)
        elif self.buttons["sound"].collidepoint(pos):
            self.game.sound_on = not self.game.sound_on
        elif self.buttons["exit"].collidepoint(pos):
            exit()

    def _draw_button(self, screen, rect, text):
        screen.draw.filled_rect(rect, "blue")
        screen.draw.text(text, center=rect.center, fontsize=30, color="white")
