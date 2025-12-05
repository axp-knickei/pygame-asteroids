import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # create a new empty `pygame.sprite.Group`



    asteroid_field = AsteroidField()

    # create the a `Player` object and passing values to the constructor to spawn it in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    while True:
        log_state()                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        # player.update(dt) .. This is working initially before using groups
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)
        
        # Call the `.update` method on the "updateables" group! Why we want to call the `.update` method on "updateable" group?
        # player.draw(screen)
               
        pygame.display.flip()

        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()
