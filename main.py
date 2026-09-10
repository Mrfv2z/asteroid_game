import sys

from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_RADIUS
import pygame
import player
import circleshape
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots= pygame.sprite.Group()
    
    
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable, drawable)


    me = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        
        for sprite in asteroids:
            if me.collides_with(sprite):
                log_event("player_hit")
                print("Game over!")
                sys.exit(0)  # Exit the program if collision occurs
                return
            for shot in shots:
                if sprite.collides_with(shot):
                    log_event("asteroid_shot")
                    sprite.split()
                    shot.kill()
                    sprite.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
