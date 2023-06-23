import pygame
import math
import random
import time
pygame.font.init()

StartGame = True

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
## Define the speed and jump height of the player
pl_speed, pl_jump = 3, 5
## Mass of the body in kg
pl_mass = 10
## Load player image and re-size it 
PLImg = pygame.transform.scale(pygame.image.load("img/Player.png"), (pl_with, pl_height))


# Buoyancy parameters:
## Initial position of the water level
water_level = res_y * 2 // 3  
## Density of water (higher value for denser water)
water_density = 4.5 
buoyant_force = 5 
# Gravitational force
gravity = 9.8

# Game UI
## Defining fonts 
font = pygame.font.SysFont("arialblack", 50)
## Define colors
TEXT_COL = (0, 0, 0)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Main game loop
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define initial position
    pl_x, pl_y = 200, (res_y - pl_height) 

    # Movement key hold
    move_l, move_r, jumping = False, False, False
    
    clock = pygame.time.Clock()
    # Keeping track of time
    ## Gives the current time
    start_time = time.time()
    ## 
    elapsed_time = 0

    # Game loop, runs forever
    while StartGame:
        # Delay while loop for 60 fps
        clock.tick(90)
        # Get the seconds since start of the while loop
        elapsed_time = time.time() - start_time
        
        # Clears the screen with the same backgroung image
        screen.blit(BGImg, (0, 0))
        
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
                if (event.key == pygame.K_LEFT):
                    move_l = True
                if (event.key == pygame.K_RIGHT):
                    move_r = True
                if (event.key == pygame.K_UP):
                    # Check if player is grounded
                    if pl_y == res_y - pl_height:
                        jumping = False
                    # Check if player is already jumping
                    if jumping == False:
                        pl_y -= pl_jump
                        jumping = True
            else:
                    move_l = False
                    move_r = False
                    jumping = False

        if(move_r):
            # Check if inside bounds
            if pl_x + pl_speed + pl_with <= res_x:
                # Move player
                pl_x += pl_speed
        if(move_l):
            # Check if inside bounds
            if pl_x - pl_speed >= 50:
                # Move player
                pl_x -= pl_speed

        
        draw_text (f"Time: {round(elapsed_time)}s", font, TEXT_COL, (res_x / 2) - 110, 20)
        # Draw player in a determined location
        screen.blit(PLImg, (pl_x, pl_y))
        # Update screen
        pygame.display.update()
        
main()
