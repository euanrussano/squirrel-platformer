from pgzero.actor import Actor
from pgzero.loaders import sounds

from actors.hero import Hero
from actors.ant import Ant
from actors.acorn import Acorn

from pgzero.keyboard import keyboard
from configuration import WIDTH, HEIGHT, Y0


class PlayScreen:
    """State representing the gameplay."""
    def __init__(self, game):
        self.game = game
        self.reset()

    def update_camera(self):
        """Update the camera offset to center on the hero."""
        self.camera_offset_x = self.hero.actor.x - (WIDTH // 2)
        self.camera_offset_y = self.hero.actor.y - (HEIGHT // 2)

    def draw(self, screen):
        screen.clear()

        # Update camera offsets
        self.update_camera()

        # Draw background
        self.background.draw()

        # Draw tiles
        for tile in self.tiles:
            tile_draw_x = tile.x - self.camera_offset_x
            tile_draw_y = tile.y - self.camera_offset_y
            screen.blit(tile.image, (tile_draw_x, tile_draw_y))

        # Draw hero
        hero_draw_x = self.hero.actor.x - self.camera_offset_x
        hero_draw_y = self.hero.actor.y - self.camera_offset_y
        screen.blit(self.hero.actor.image, (hero_draw_x, hero_draw_y))

        # Draw ant
        for ant in self.ants:
            ant_draw_x = ant.actor.x - self.camera_offset_x
            ant_draw_y = ant.actor.y - self.camera_offset_y
            screen.blit(ant.actor.image, (ant_draw_x, ant_draw_y))

        # Draw acorns
        for acorn in self.acorns:
            acorn_draw_x = acorn.actor.x - self.camera_offset_x
            acorn_draw_y = acorn.actor.y - self.camera_offset_y
            screen.blit(acorn.actor.image, (acorn_draw_x, acorn_draw_y))

        # Draw the score at the top of the screen
        screen.draw.text(f"Score: {self.score}", (10, 10), fontsize=40, color="black")

    def update(self, dt):
        self.hero.update(dt, keyboard)
        for ant in self.ants:
            ant.update(dt)

        for acorn in self.acorns:
            acorn.update(dt)

        # Check for collisions
        for ant in self.ants:
            if self.hero.colliderect(ant.actor):
                self.game.set_state(self.game.game_over_state)  # Transition to Game Over screen
                return

        for acorn in self.acorns[:]:  # Use slicing to avoid issues while modifying the list
            if self.hero.colliderect(acorn.actor):
                self.acorns.remove(acorn)
                self.score += 1
                if self.game.sound_on:
                    sounds.handle_coins.play()

    def on_mouse_down(self, pos):
        pass

    def reset(self):
        self.background = Actor("background.png")
        self.hero = Hero()
        self.ants = []
        for i in range(5):
            x0 = 400 + i * 300
            x1 = 600 + i * 300
            self.ants.append(Ant([x0, x1]))
        self.acorns = [Acorn(600+i*300, Y0) for i in range(5)]
        self.score = 0

        # floor
        self.tiles = []
        for i in range(100):
            x = i*64
            y = Y0+32
            self.tiles.append(Actor("tiles/floor1.png", (x, y)))


        # Camera offset
        self.camera_offset_x = 0
        self.camera_offset_y = 0


