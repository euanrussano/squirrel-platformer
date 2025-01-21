class GameOverScreen:
    """State representing the game over screen."""
    def __init__(self, game):
        self.game = game

    def draw(self, screen):
        screen.clear()
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=50, color="red")
        screen.draw.text("Click to return to the main menu", center=(400, 350), fontsize=30, color="white")

    def update(self, dt):
        pass

    def on_mouse_down(self, pos):
        self.game.reset()
        self.game.set_state(self.game.main_menu_state)  # Return to the main menu
