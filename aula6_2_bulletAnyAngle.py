import pygame
import sys
import math

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Constants
GROUND_LEVEL = 600  # y-coordinate of the ground
v0 = 100  # initial velocity in m/s
theta = math.radians(15)  # launch angle in radians
y0 = 20  # initial height in meters
g = 9.8  # acceleration due to gravity in m/s^2

# Calculate initial velocities
vx0 = v0 * math.cos(theta)
vy0 = v0 * math.sin(theta)

# Calculate time of flight
#t_flight = (2 * vy0 / g)
t_flight = (2 * vy0 * math.sin(theta)) / g

# Calculate horizontal distance
x_distance = vx0 * t_flight
# Calculate time step and initial position
dt = x_distance / (v0 * 100)  # small time steps for smooth animation
x = 0
y = y0

# Pygame loop
while y >= 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Update position
    x += vx0 * dt
    #y += vy0 * dt #Forma abreviada
    y += vy0 * dt + 0.5*g*dt**2
  
    # Update velocities
    vy0 -= g * dt

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw bullet
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(GROUND_LEVEL - y)), 5)

    # Draw ground
    pygame.draw.line(screen, (0, 0, 0), (0, GROUND_LEVEL), (800, GROUND_LEVEL), 2)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS