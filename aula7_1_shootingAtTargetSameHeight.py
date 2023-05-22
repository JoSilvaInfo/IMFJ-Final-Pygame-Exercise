import pygame, math, sys
import pygame
import math
#
#Example of a physics simulation in Pygame and 
# demonstrates how to calculate the initial velocity and angle
#  required to hit a target with a projectile.
#
#https://www.khanacademy.org/science/physics/two-dimensional-motion/two-dimensional-projectile-mot/v/launching-and-landing-on-different-elevations

#Calculate the horizontal distance (dx) 
# between the character and the projectile.

#Calculate the vertical distance (dy) 
# between the character and the projectile.

#Calculate the total distance (d) 
# between the character and the projectile using the Pythagorean theorem:
#  d = sqrt(dx^2 + dy^2).

#Calculate the angle between the projectile and
#  the character using the arctangent function: angle = atan2(dy, dx).

#Calculate the initial velocity (v0) of the projectile 
# using the following equation:
#v0 = sqrt((d * g) / sin(2 * angle))
#where g is the acceleration due to gravity (GRAVITY in the code).

#Set the initial velocity (v0) and angle (angle) of the projectile 
# to the values calculated in steps 4 and 5.
#

#This code implements a simple physics simulation in Pygame. 
# A character is controlled by the user and 
# a projectile is fired from a starting point towards the character. 
# The program calculates the initial velocity and angle required 
# to hit the character with the projectile.
#The simulation is done by updating 
# the projectile's position and velocity 
# at regular intervals using numerical integration. 
# The projectile's motion is affected by gravity, 
# which is represented by the constant GRAVITY.
#The program uses the Pythagorean theorem 
# to calculate the distance between the projectile and the character, 
# and the arctangent function to calculate the angle between them. 
# It then uses an equation to calculate the initial velocity 
# required to hit the character with the projectile, 
# and sets the projectile's initial velocity and angle to these values.
#The main loop of the program handles user input, 
# updates the projectile's position and velocity, 
# checks if the projectile hits the character or goes off-screen, 
# and adds the projectile's position to a list of positions. 
# The positions are used to draw the projectile's trajectory 
# on the screen.


#Incorrect initial velocity or angle: If the initial velocity or angle of the projectile is not calculated correctly, it may not reach the target. Make sure that the initial velocity and angle are calculated accurately based on the distance and angle between the character and projectile.
#Incorrect gravity value: If the value of the gravity constant is not set correctly, the trajectory of the projectile may be incorrect, causing it to miss the target.
#Inaccurate time step or time increment: The time step used in the numerical integration of the projectile motion equations may be too large, causing inaccuracies in the calculation of the projectile's position and velocity. Try reducing the time step to improve the accuracy of the simulation.

# Set the window dimensions, frames per second, and gravity
WIDTH = 800
HEIGHT = 600
FPS = 60
GRAVITY = 9.81

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
    
    def draw(self):
        pygame.draw.circle(screen, RED, [self.x,self.y], self.radius)

# Define the projectile class
class Projectile:
    def __init__(self, x, y, v0, angle):
        self.x = x
        self.y = y
        self.v0 = v0
        self.angle = angle
        self.dt = 0.1
        self.vx = 0
        self.vy = 0
        self.t = 0
        self.radius=5
    
    def update(self):
        self.t += self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt + 0.5 * GRAVITY * self.dt**2
        self.vy += GRAVITY * self.dt      
    
    def get_position(self):
        return (self.x, self.y)
    
    def is_on_screen(self):
        return 0 <= self.x <= WIDTH and 0 <= self.y <= HEIGHT
    
    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (int(self.x), int(self.y)), self.radius)


# Define the main function
def main():
    # Initialize the character and projectile
    dude = Character(400, HEIGHT/2)
    projectile = Projectile(10, HEIGHT/2, 0, 0)  # Set initial velocity to zero

    # Initialize the time variable and flag variables
    t=0
    shoot = False
    hit = False

    # Create an empty list to store the positions
    positions = []

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    dude.x += 10
                elif event.key == pygame.K_LEFT:
                    dude.x -= 10
                elif event.key == pygame.K_SPACE:
                    dx = dude.x - projectile.x
                    dy = dude.y - projectile.y
                    d = math.sqrt(dx**2 + dy**2)#distance between the starting point and the target point in two-dimensional space.
                    angle = math.degrees(math.atan2(dy, dx))
                    
                    if(angle==0):
                        angle=45
                    #intial velocity
                    v0 = math.sqrt((d * GRAVITY) / (math.sin(2 * math.radians(angle))))                    
                    projectile.vx = v0 * math.cos(math.radians(angle))
                    projectile.vy = -v0 * math.sin(math.radians(angle)) + 0.5 * GRAVITY * projectile.dt
                    projectile.v0 = v0
                    projectile.angle = angle
                    shoot = True

        # Update the projectile and time
        if shoot:
            projectile.update()
            t += projectile.dt

        # Check if the projectile hits the character
        if not hit and math.sqrt((dude.x - projectile.x)**2 + (dude.y - projectile.y)**2) <= dude.radius + projectile.radius:
            hit = True

        # Check if the projectile is still on the screen
        if projectile.is_on_screen():
            # Add the position to the list
            positions.append(projectile.get_position())
        else:
            # Stop the simulation
            running = False

        # Clear the screen
        screen.fill(BLACK)
        pygame.draw.line(screen, (255,0,0), [dude.x, dude.y], [projectile.x, projectile.y])
                    
        # Draw the character
        dude.draw()

        # Draw the positions
        for position in positions:
            pygame.draw.circle(screen, WHITE, position, 2)

        # Draw the projectile
        projectile.draw(screen)

        # Update the screen
        pygame.display.flip()

        # Wait for the next frame
        clock.tick(FPS)

    # Done
    pygame.quit()

# Call the main function
if __name__ == "__main__":
    main()