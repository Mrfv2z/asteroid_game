import circleshape
import pygame
from constants import *
from logger import log_event
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            width=LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            log_event("asteroid_split")
            new_angle= random.uniform(0, 360)
            new_ast1=pygame.Vector2(0, 1).rotate(new_angle)
            new_ast2=pygame.Vector2(0, 1).rotate(new_angle + 45)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1=Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2=Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity=(new_ast1 + self.velocity) * 1.2
            asteroid2.velocity=(new_ast2 + self.velocity) * 1.2
            return [asteroid1, asteroid2]
            