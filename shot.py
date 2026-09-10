import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen: pygame.Surface) -> None:
            pygame.draw.circle(
                screen,
                "white",
                self.position,
                self.radius,
                width=SHOT_RADIUS,
)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt