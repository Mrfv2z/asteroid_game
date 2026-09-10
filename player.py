import circleshape
import pygame
from constants import LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SPEED, PLAYER_TURN_SPEED,PLAYER_SHOOT_SPEED
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS,Cooldown=0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = Cooldown
        
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
         
    def triangle(self) -> list[pygame.Vector2]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            a = self.position + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            return [a, b, c]
          
          
    def draw(self, screen: pygame.Surface) -> None:
                self.screen=screen
                lis=self.triangle()
                pygame.draw.polygon(self.screen, "white", lis, width=LINE_WIDTH)
                
                
                
                
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shot()
        self.cooldown -= dt
            
    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def shot(self):
        if self.cooldown >= 0:
            return
        else:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        new_shoot = Shot(self.position.x, self.position.y)
        new_shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED