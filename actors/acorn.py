from pgzero.actor import Actor

ACORN_FRAMES = [f"items/acorn/acorn-{i}" for i in range(1, 4)]


class Acorn:
    def __init__(self, x, y):
        self.actor = Actor(ACORN_FRAMES[0], (x, y))
        self.index = 0
        self.animation_timer = 0.2
        self.current_timer = 0.0

    def update(self, dt):
        self.current_timer += dt
        if self.current_timer >= self.animation_timer:
            self.current_timer = 0.0
            self.index = (self.index + 1) % len(ACORN_FRAMES)
            self.actor.image = ACORN_FRAMES[self.index]

    def draw(self, screen):
        self.actor.draw()

    def colliderect(self, other):
        return self.actor.colliderect(other)
