import pgzrun
from pgzero.screen import Screen
from game import Game

screen: Screen

# Initialize the game
game = Game()


# Pygame Zero hooks
def draw():
    game.draw(screen)


def update(dt):
    game.update(dt)


def on_mouse_down(pos):
    game.on_mouse_down(pos)


pgzrun.go()
