import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Buoyancy Simulation")

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rectangle parameters
rectangle_width = 200
rectangle_height = 100
rectangle_x = width // 2 - rectangle_width // 2
rectangle_y = 0  # Starts at the top

# Buoyancy parameters
water_level = height * 2 // 3  # Initial position of the water level
water_density = 4.5  # Density of water (higher value for denser water)
gravity = 9.8

# Mass of the red rectangle
rectangle_mass = 1.5  # Smaller mass

# Game loop
running = True
clock = pygame.time.Clock()
buoyant_force=0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if rectangle_y + rectangle_height < water_level:  # Rectangle is in the free-fall phase
        # Calculate the net force
        net_force = rectangle_mass * gravity

        # Apply the net force to the rectangle's position
        acceleration = net_force / rectangle_mass
        rectangle_y += acceleration

 
    else:  # Rectangle is in the buoyancy phase
            # Calculate the submerged depth
            submerged_depth = ((rectangle_y + rectangle_height) - water_level)
            
            # Calculate the buoyant force
            #submerged_volume=0.4  # m^3 (dimensions: 1m x 0.4m x 0.1m)
            submerged_volume=0.4*submerged_depth/rectangle_height 
            
            #Version 1
            buoyant_force = water_density * gravity * submerged_volume
            
            #Version 2
            #rect_density = rectangle_mass / submerged_volume
            #if rect_density <= water_density:
            #    buoyant_force += 0.1*rect_density * submerged_volume * gravity
            #    print("up")
            #else:
            #    buoyant_force -=0.1* water_density * submerged_volume * gravity
            #    print("down") 
            
            # Calculate the net force
            net_force = rectangle_mass * gravity - buoyant_force
            # Apply the net force to the rectangle's position
            acceleration = net_force / rectangle_mass
            rectangle_y += acceleration

    # Draw the scene
    screen.fill((0, 0, 0))  # Fill the screen with black color
    pygame.draw.rect(screen, RED, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    pygame.draw.line(screen, BLUE, (0, water_level), (width, water_level), 3)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
