import pygame
import math
import random

# Defining screen/window:
## Define the size/resolution of our window
res_x, res_y = 1400, 1000
## Create a window and a display surface
screen = pygame.display.set_mode((res_x, res_y))
## Set the pygame window name
pygame.display.set_caption("Pirate Escape")
## Load background image and re-size it 
BGImg = pygame.transform.scale(pygame.image.load("img/BG1.png"), (res_x, res_y))


#Player parameters:
## Define the size of the player
pl_with, pl_height = 100, 120
## Load player image and re-size it 
PLImg = pygame.transform.scale(pygame.image.load("img/Player.png"), (pl_with, pl_height))
## Mass of the red rectangle
pl_mass = 1.5  # Smaller mass

# Buoyancy parameters:
## Initial position of the water level
water_level = res_y * 2 // 3  
## Density of water (higher value for denser water)
water_density = 4.5  
gravity = 9.8
buoyant_force = 5

# Draws everything on the scene
def draw():
    # Draw Bckgroung image
    screen.blit(BGImg, (0, 0))
    # Draw player in a determined location
    screen.blit(PLImg, (200, res_y - pl_height))

    # Update screen
    pygame.display.update()



def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    player = pygame.Rect(200, res_y - pl_height, pl_with, pl_height)

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
