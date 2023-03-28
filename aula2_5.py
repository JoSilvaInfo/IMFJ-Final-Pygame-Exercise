
import pygame
from pygame.math import Vector2

# Define the size/resolution of our window
res_x = 800
res_y = 600
start_time=0
vFORWARD=Vector2(0.01,0)
HEADWIND_FORCE = float(-0.005)
GRAVITY_FORCE =  9.81 * 0.001  #y is increasing down (not -9.81) 
MASS=4
bForcesAreActive=False

class Character:
    def __init__(self, currentPosition, size):
        self.position = Vector2(currentPosition)        
        self.size=size
        self.velocity=Vector2(0,0)
        self.acceleration=vFORWARD
        self.mass=MASS

    def draw (self, screen):         
         pygame.draw.circle(screen, (255,0,0), self.position, self.size)
        
    def move(self):
        global start_time, HEADWIND_FORCE, vFORWARD, GRAVITY_FORCE
        #self.velocity=vFORWARD
        #time in seconds - get_ticks() returns time in miliseconds
        elapsed_time=(pygame.time.get_ticks()-start_time)/1000 
   
        if(bForcesAreActive):            
            headwind_force=Vector2(HEADWIND_FORCE,0)
            gravity_force=Vector2(0,GRAVITY_FORCE)
            total_force= headwind_force + vFORWARD + gravity_force
            #calculate acceleration and speed 
            self.acceleration=total_force/self.mass 
        #calculate new position
        self.position += self.velocity * elapsed_time + 0.5 * self.acceleration * elapsed_time**2
       
      

def showMessages(screen):
     myfont = pygame.font.SysFont("monospace", 15)
     WHITE = (255, 255, 255)
     label = myfont.render("Press SPACE to activate Wind", 1, WHITE)
     screen.blit(label, (10, 400))

def main():
    global bForcesAreActive, start_time, vFORWARD
    # Initialize pygame, with the default parameters
    pygame.init()
    clock=pygame.time.Clock()
    start_time=pygame.time.get_ticks()
    
    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    dude = Character( [10,100], 10)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):                   
                    bForcesAreActive=True
                elif (event.key == pygame.K_ESCAPE):
                    return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:  
                    vFORWARD.x+=0.00001
                    vFORWARD.y+=-0.00001
        if keys[pygame.K_DOWN] and bForcesAreActive:
                    vFORWARD.x=0
                    vFORWARD.y=0
        #else:
        #            vFORWARD.x=0

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))
        
        dude.draw(screen)
        dude.move()

        showMessages(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
main()

