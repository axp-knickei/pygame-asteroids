import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    while True:                    # Correction from Boots for infinite loop 
        log_state()                # Call log_state(). No arguments needed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")       # black without quotes is treated as variable.
        pygame.display.flip()      # Use pygame's `display.flip()` method to refresh the screen.

if __name__ == "__main__":
    main()
