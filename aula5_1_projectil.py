import pygame, math, sys
import pygame
import math
WIDTH = 800
HEIGHT = 600
FPS = 60
GRAVITY = 9.806

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define the projectile class
class Projectile:
    def __init__(self, x, y, v0, angle):
        
        self.x = x
        self.y = y
        self.v0 = v0
        self.angle = angle
        self.delta_time = 0.1#setting the time step or time increment used in the numerical integration of the projectile motion equations. The variable self.dt represents the amount of time that passes between each update of the projectile's position and velocity in the update method.
        self.vx = 0#v0 * math.cos(math.radians(angle))
        #self.vy = -v0 * math.sin(math.radians(angle))
        self.vy = 0#-v0 * math.sin(math.radians(angle)) + 0.5 * GRAVITY * self.dt
        self.time = 0
        self.radius=5
       
    def update(self):
        self.time += self.delta_time        
        #x=x0+Vxt
        #x=Vx×t  
        self.x += self.vx*self.delta_time
     
        #y=y0+v0yt-1/2gt2   
        #y=h+Vy*t−(g×t2)/2    no inicio h=y0 altura inicial
        self.y += self.vy*self.delta_time - (GRAVITY*self.delta_time**2)/2
        self.vy += GRAVITY*self.delta_time
        
    def get_position(self):
        return (self.x, self.y)
    
    def is_on_screen(self):
        return 0 <= self.x <= WIDTH and 0 <= self.y <= HEIGHT
    
    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (int(self.x), int(self.y)), self.radius)

# Define the main function
    ##################
    ##################
    ##################

def main():
    projectile = Projectile(0, HEIGHT/2, 80, 10) 

    # Initialize flag variables
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
                elif event.key == pygame.K_SPACE:
                    shoot = True
                    #Vx = V0×cos(α)
                    projectile.vx=projectile.v0*math.cos(math.radians(projectile.angle))
                    
                    #Vy = V0×sin(α)
                    projectile.vy=-projectile.v0*math.sin(math.radians(projectile.angle))

                    #time of flight
                    #t=2V/g(sinα).
                    #t=2*projectile.v0/GRAVITY*math.sin(math.radians(projectile.angle)) 
                    #print("time of flight", t) 
        # Update the projectile and time
        if shoot:
            projectile.update()            
       
        # Check if the projectile is still on the screen
        if projectile.is_on_screen():
            # Add the position to the list
            positions.append(projectile.get_position())
        else:
            # Stop the simulation
            running = False

        # Clear the screen
        screen.fill(BLACK)
     
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