import pygame
import time
import random

# Define the size/resolution of our window
res_x, res_y = 1400, 1000
# Create a window and a display surface
screen = pygame.display.set_mode((res_x, res_y))
# Set the pygame window name
pygame.display.set_caption("Pirate Escape")
# Load background image
BG = pygame.image.load("img/BG1.png")
# Re-size background image
screenUpdate = pygame.transform.scale(BG, (res_x, res_y))

def draw():
    # Draw Bckgroung image
    screen.blit(screenUpdate, (0, 0))
    # Update screen
    pygame.display.update()

def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Game loop, runs forever
    while (True):
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
        draw()
        # Clears the screen with a very dark blue (0, 0, 20)
        #screen.fill((0,0,0))

      
        # Swaps the back and front buffer, effectively displaying what we rendered
        #pygame.display.flip()
        
main()
