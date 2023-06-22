import pygame
import time
import random

# Define the size/resolution of our window
res_x, res_y = 1400, 1000
# Create a window and a display surface
screen = pygame.display.set_mode((res_x, res_y))
# Give the created window a name
pygame.display.set_caption("Pirate Escape")


def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    run = True

    # Game loop, runs forever
    while run:
        # Process events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            #checks user input
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

      
        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
        
main()
