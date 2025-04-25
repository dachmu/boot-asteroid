import pygame
import pygame.freetype

from circleshape import CircleShape
from constants import SCORE_BOARD_TO_SCREEN_RATIO, SCREEN_HEIGHT

class Score(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
        self.score = 0
        
    def draw(self, screen):
        white = pygame.Color(255,255,255)

        font = pygame.freetype.SysFont('arial', int(SCREEN_HEIGHT * SCORE_BOARD_TO_SCREEN_RATIO))
        font.render_to(screen, self.position, f"Score: {self.score}", white)

