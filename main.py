import pygame
import player as p
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    p.Player.containers = (updatable, drawable) 
    player = p.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        screen.fill("black")
        updatable.update(dt)

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
