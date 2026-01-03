import pygame
import player as p
import asteroid as a
import asteroidfield as af
import shot
from constants import *
from logger import log_state

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    astroids_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable) 
    p.Player.containers = (updatable, drawable) 
    player = p.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
    a.Asteroid.containers = (astroids_group, updatable, drawable) 
    af.AsteroidField.containers = (updatable)
    astroid_field = af.AsteroidField()

    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)

        for astroid in astroids_group:
            for s in shots:
                if s.did_collide(astroid):
                    s.kill()
                    astroid.split()

            if astroid.did_collide(player):
                print("Game over!")
                exit(0)

        for thing in drawable:
            thing.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # renders all the stuff above to the screen
        pygame.display.flip()
        # converts amount of time that has passed
        # since the last time it was called to milliseconds
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
