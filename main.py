# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0, 0, 0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers =(updatable)
    asteroid_field = AsteroidField()

    shoots = pygame.sprite.Group()
    Shoot.containers = (shoots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if player.is_colliding(obj):
                print("Game over")
                sys.exit("Game over")
            for shoot in shoots:
                if shoot.is_colliding(obj):
                    pygame.sprite.Sprite.kill(shoot)
                    obj.split()
                
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
    