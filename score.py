import pygame
import pygame.freetype

from circleshape import CircleShape

class Score(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
        self.score = 0
        
    def square(self):
        half_heigh = 1 * self.radius
        half_width = 1.5 * self.radius

        
        p1x = self.position.x - half_width
        p1y = self.position.y - half_heigh
        p1 = pygame.Vector2(p1x, p1y)

        p2x = self.position.x - half_width
        p2y = self.position.y + half_heigh
        p2 = pygame.Vector2(p2x, p2y)

        p3x = self.position.x + half_width
        p3y = self.position.y + half_heigh
        p3 = pygame.Vector2(p3x, p3y)

        p4x = self.position.x + half_width
        p4y = self.position.y - half_heigh
        p4 = pygame.Vector2(p4x, p4y)

        return [p1, p2, p3, p4]

    def draw(self, screen):
        white = pygame.Color(255,255,255)

        font = pygame.freetype.SysFont('arial', 10)
        text = font.render(str(self.score), True, white)

        font.render_to(screen, self.position, f"Score: {self.score}", white)

        pygame.draw.polygon(screen, white, self.square(), 2)
