import pygame
import sys
import math
# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#The formula for calculating the time of flight of a projectile 
# when launched vertically upward or downward is given by:
#t_flight = (2 * y0 / g)
#This formula assumes that the initial vertical velocity is zero. 
# It is derived from the kinematic equation for vertical motion, 
# where the displacement (y0) is equal to zero 
# at the highest point of the trajectory.

# Constants
GROUND_LEVEL = 400  # y-coordinate of the ground
v0 = 1500  # initial velocity in m/s
y0 = 20  # initial height in meters
g = 9.8  # acceleration due to gravity in m/s^2
# Calculate time of flight
#Ao nivel do solo 
#t_flight = 2 * v0 * math.sin(0) / g

#Acima do solo h>0
h=20
t_flight = (v0 * math.sin(math.radians(0)) + 
            math.sqrt((v0 * math.sin(math.radians(0)))**2 + 
                      2 * g + h)) / g
#t_flight = (2 * y0 / g) #Formas abreviadas
#t_flight= 2 * math.sqrt(2 * y0 / g) #Formas abreviadas

# Calculate horizontal distance
x_distance = v0 * t_flight

# Calculate time step and initial position
dt = x_distance / (v0 * 100)  # small time steps for smooth animation
x = 0
y = y0
vx = v0  # initial velocity in the x-direction
vy = 0  # initial velocity in the y-direction

# Pygame loop
while y >= 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update position and velocity
    x += vx * dt
    #y += vy * dt # apenas tendo em conta a velocity
    y += vy * dt + 0.5*g*dt**2 #ja tendo em conta a gravidade

    vy -= g * dt  # update vertical velocity due to gravity

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw bullet
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(GROUND_LEVEL - y)), 5)

    # Draw ground
    pygame.draw.line(screen, (0, 0, 0), (0, GROUND_LEVEL), (800, GROUND_LEVEL), 2)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS
