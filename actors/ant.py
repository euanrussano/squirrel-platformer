from pgzero.actor import Actor

from configuration import Y0

ANT_FRAMES = [f"enemies/ant/ant-{i}" for i in range(1, 9)]


class Ant:
    def __init__(self, patrol_points, speed=1):
        self.actor = Actor(ANT_FRAMES[0], (patrol_points[0], Y0))
        self.index = 0
        self.animation_timer = 0.2
        self.current_timer = 0.0
        self.patrol_points = patrol_points
        self.current_patrol_index = 0
        self.speed = speed

    def update(self, dt):
        self.current_timer += dt
        if self.current_timer >= self.animation_timer:
            self.current_timer = 0.0
            self.index = (self.index + 1) % len(ANT_FRAMES)
            self.actor.image = ANT_FRAMES[self.index]

        target_x = self.patrol_points[self.current_patrol_index]
        dx = target_x - self.actor.x
        distance = abs(dx)

        if distance > self.speed:
            self.actor.x += self.speed * (dx / distance)
        else:
            self.current_patrol_index = (self.current_patrol_index + 1) % len(self.patrol_points)

    def draw(self, screen):
        self.actor.draw()

    def colliderect(self, other):
        return self.actor.colliderect(other)
