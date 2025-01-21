from pgzero.actor import Actor
from configuration import Y0

HERO_FRAMES = {
    "idle": [f"player/idle/player-idle-{i}" for i in range(1, 9)],
    "run": [f"player/run/player-run-{i}" for i in range(1, 7)],
    "jump": [f"player/jump/player-jump-{i}" for i in range(1, 5)],
}

# Blank space below the hero in the texture
TEX_OFFSET = 64 / 4

Y0_HERO = Y0


class Hero:
    def __init__(self):
        self.actor = Actor(HERO_FRAMES["idle"][0], (200, Y0_HERO))
        self.idle_index = 0
        self.run_index = 0
        self.jump_index = 0
        self.velocity_y = 0
        self.animation_timer = 0.2
        self.current_timer = 0.0

    def update(self, dt, keys):
        self.current_timer += dt
        if self.current_timer >= self.animation_timer:
            self.current_timer = 0.0
            if self.velocity_y != 0:
                self.jump_index = (self.jump_index + 1) % len(HERO_FRAMES["jump"])
                self.actor.image = HERO_FRAMES["jump"][self.jump_index]
            elif not (keys.left or keys.right):
                self.idle_index = (self.idle_index + 1) % len(HERO_FRAMES["idle"])
                self.actor.image = HERO_FRAMES["idle"][self.idle_index]
            else:
                self.run_index = (self.run_index + 1) % len(HERO_FRAMES["run"])
                self.actor.image = HERO_FRAMES["run"][self.run_index]

        if keys.left:
            self.actor.x -= 2
        if keys.right:
            self.actor.x += 2

        if keys.up and self.velocity_y == 0:
            self.actor.image = HERO_FRAMES["jump"][0]
            self.velocity_y = 8

        if self.velocity_y != 0:
            self.actor.y -= self.velocity_y
            self.velocity_y -= dt * 10
            if self.actor.y >= Y0_HERO:
                self.actor.y = Y0_HERO
                self.velocity_y = 0

    def draw(self, screen):
        self.actor.draw()

    def colliderect(self, other):
        return self.actor.colliderect(other)
