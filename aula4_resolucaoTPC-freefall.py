import pygame
import sys
import math

# Pygame Initialization
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CHARACTER_RADIUS = 10
CHARACTER_COLOR = (255, 0, 0)
LINE_COLOR = (0, 255, 0)
GRAVITY = 9.8  # Acceleration due to gravity (m/s^2)
LINE_START_X = 0
LINE_END_X = 100
LINE_Y = 30

# Screen Setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Character Movement")

# Character Setup
character_x = LINE_START_X
character_y = LINE_Y - CHARACTER_RADIUS
character_velocity_x = 0
character_velocity_y = 0
character_in_free_fall = False

# Time Setup
clock = pygame.time.Clock()
delta_time = 0

# Game Loop
while True:
    delta_time = clock.tick(60)  # Limit frame rate to 60 FPS
    # It measures the time elapsed since the last call to clock.tick() and then 
    # delays the game loop for the remaining time necessary to achieve the desired frame rate. 
    #used to control the frame rate or the refresh rate of the game loop. 
    # It limits the number of frames per second (fps) that the game loop will run to a maximum of 60 frames per second.

    screen.fill((255, 255, 255))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move character horizontally to the right by 10 pixels
                if not character_in_free_fall:
                    character_velocity_x = 10

    # Update Character Position
    #delta_time is expressed in miliseconds. 
    timestep =  delta_time/100  #0.05 ideal
   
    if not character_in_free_fall and character_x <= LINE_END_X:
        character_x += character_velocity_x * timestep  # Update horizontal position  
    else:        
        character_in_free_fall = True
# Apply physics equation for free fall in x and y direction
        #FORMA STANDARD
        #x=x0+vt
        character_velocity_x = 0  # No horizontal acceleration during free fall
        character_x += character_velocity_x * timestep  # Update horizontal position  
        #y=y0+v0t+1/2gt^2
        character_velocity_y += GRAVITY * timestep  # Update vertical velocity. Acceleraration is Gravity force
        character_y += character_velocity_y * timestep + 0.5 * GRAVITY * (timestep) ** 2
        
        #FORMA ABREVIADA    
        #character_velocity_y += GRAVITY * timestep 
        #character_y += character_velocity_y*timestep
       
        if character_y >= WINDOW_HEIGHT - CHARACTER_RADIUS:
            character_y = WINDOW_HEIGHT - CHARACTER_RADIUS

    # Draw Line
    pygame.draw.line(screen, LINE_COLOR, (LINE_START_X, LINE_Y), (LINE_END_X, LINE_Y), 2)

    # Draw Character
    pygame.draw.circle(screen, CHARACTER_COLOR, (round(character_x), round(character_y)), CHARACTER_RADIUS)

    pygame.display.flip()