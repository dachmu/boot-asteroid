import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    npass, nfail = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = [updatable]
    Asteroid.containers = [updatable, drawable, asteroids]
    Player.containers = [updatable, drawable]
    Shot.containers = [drawable, shots, updatable]
 
    dt = 0
    clock = pygame.time.Clock()
    black = pygame.Color(0,0,0)

    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidf = AsteroidField()

    while True:
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60)/1000
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(p):
                print("Game over!")
                return
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()

if __name__ == "__main__":
    main()
