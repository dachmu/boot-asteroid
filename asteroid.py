import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position , self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, score):
        self.kill()
        score.score += self.radius

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rangle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        aste1 = Asteroid(self.position.x, self.position.y, new_radius)
        aste1.velocity = self.velocity.rotate(rangle)

        aste2 = Asteroid(self.position.x, self.position.y, new_radius)
        aste2.velocity = self.velocity.rotate(-1 * rangle)
