import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position , self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt
