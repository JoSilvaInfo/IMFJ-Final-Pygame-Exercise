import pygame
import math
import random
import time
from freefall import CannonBall
from platforms import Platform
#import Menu

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

# Player parameters:
## Player lives
pl_lives = 3
## Define the size of the player
pl_with, pl_height = 100, 120
## Define the speed and jump height of the player
pl_speed, pl_jump = 3, 100 
## Mass of the body in kg
pl_mass = 10
## Load player image and re-size it 
PLImg = pygame.transform.scale(pygame.image.load("img/Player.png"), (pl_with, pl_height))

# Buoyancy parameters:
## Initial position of the water level
water_level = 850 
## Density of water (higher value for denser water)
water_density = 4.5 
buoyant_force = 5 
# Gravitational force
gravity = 9.8

#Objects
## Floatable 
#Plank_Img = pygame.transform.scale(pygame.image.load("img/Wood.png"), (48, 64))

## Sincable 
#Twig_Img = pygame.transform.scale(pygame.image.load("img/Tree.png"), (48, 64))
## Water 
#Water_Img = pygame.transform.scale(pygame.image.load("img/Water.png"), (48, 64))

## Cannon ball
ball_radius = 10

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

    global pl_jump

    # Define initial position
    pl_x, pl_y, pl_j_speed = 200, (water_level - pl_height), pl_jump 

    # Movement key hold confirmations
    move_l, move_r, jumping = False, False, False

    floating = False

    # Event confirmation
    shoot = False

    # List to store CannonBall instances
    cannonballs = []  
    
    clock = pygame.time.Clock()
    # Keeping track of time
    ## Gives the current time
    start_time = time.time()
    ## 
    elapsed_time = 0

    # Initial spawn after 30 seconds
    next_spawn_time = 5

    def spawn_cballs():
        num_balls = random.randint(3, 4)  # Generate a random number of CannonBalls to spawn
        for _ in range(num_balls):
            sp_x = 0
            sp_y = random.randint(ball_radius, res_y - ball_radius)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color for each CannonBall
            ball = CannonBall(sp_x, sp_y, ball_radius, 0, 0, 0, color)
            cannonballs.append(ball)

    # Game loop, runs forever
    while StartGame:
        # Delay while loop for 90 fps
        clock.tick(90)
        # Get the seconds since start of the while loop
        elapsed_time = time.time() - start_time
        
        # Player object
        player = pygame.Rect(pl_x, pl_y, pl_with, pl_height)
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
                    jumping = True
                    pl_j_speed = pl_jump
            else:
                    move_l = False
                    move_r = False

        # Check ifplayer is still alive 
        #if pl_lives <=0:
            #Menu.gameover()

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

        if jumping:
            pl_y -= pl_j_speed 
            pl_j_speed -= gravity
            if pl_j_speed < -pl_jump:
                jumping = False

        # Apply gravity to the player
        pl_y += gravity

        # Check if player exceeds screen boundaries
        if pl_y < 0:
            pl_y = 0
        elif pl_y > water_level - pl_height:
            pl_y = water_level - pl_height

        
        # Check if it's time to cannon balls a ball
        current_time = time.time()
        if elapsed_time >= next_spawn_time:
            shoot = True
            # Schedule next spawn after 30 seconds
            next_spawn_time = next_spawn_time + 5

        if shoot:
            print("Shoot!")
            # Calculate time step based on frame rate to update the Canonballs
            ## Convert milliseconds to seconds
            time_step = clock.get_time() / 1000.0  
            shoot = False

            # Update CannonBalls
            for ball in cannonballs:
                ball.update(time_step)

            # Handle CannonBall collisions
            for ball in cannonballs:
                ball.handle_cball_collision(player)

            # Remove CannonBalls that are offscreen
            cannonballs = [ball for ball in cannonballs if not ball.is_offscreen()]
            # Draw CannonBalls
            for ball in cannonballs:
                ball.draw(screen)

        draw_text (f"Time: {round(elapsed_time)}s", font, TEXT_COL, (res_x / 2) - 110, 20)
        draw_text (f"Lives: {pl_lives}", font, TEXT_COL, 50, 20)

        #platform.update()
        # Draw player in a determined location
        screen.blit(PLImg, player)
        # Draw ground
        pygame.draw.line(screen, (0, 0, 0), (0, water_level), (res_x, water_level), 2)
        # Update screen
        pygame.display.update()
        
main()
