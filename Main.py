import pygame
import math
import random
import time
from freefall import CannonBall
from platforms import Platform
#from menu import MainMenu, GameOver, Pause

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
pl_width, pl_height = 100, 120
## Define the speed and jump height of the player
pl_speed, pl_jump = 3, 100 
## Mass of the body in kg
pl_mass = 10
pl_accel = 0.2
pl_friction = 0.1
# Max speed for the player
pl_max_speed = 5
## Load player image and re-size it 
PLImg = pygame.transform.scale(pygame.image.load("img/Player.png"), (pl_width, pl_height))

# Buoyancy parameters:
## Initial position of the water level
water_level = 850 
## Density of water (higher value for denser water)
water_density = 4.5 
buoyant_force = 5 


# Gravitational force
gravity = 9.8

## Platform
plt_height = 10
plt_width = 30
# Platform mass
plt_mass = 1.5
# List to store Platform instances
platforms = []  
# Max platfomrs on screen
max_platforms = random.randint(4, 5)

## Cannon ball
ball_radius = 10
ball_mass = 30
ball_speed = ball_radius * ball_mass
# Delay between cannonball updates in milliseconds
## Adjust this value to control the refresh rate of the cannonballs
cannonball_delay = 100 
# List to store CannonBall instances
cannonballs = []
remove_list = []  
# Max cannonballs on screen
max_cannonballs = random.randint(2, 4)

# Game UI
## Defining fonts 
font = pygame.font.SysFont("arialblack", 50)
## Define colors
TEXT_COL = (0, 0, 0)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def random_platform():
    global plt_width, plt_height, plt_mass
    # Generate random proportions
    plt_width = random.randint(50, 150)
    plt_height = random.randint(10, 30)
    plt_mass = random.uniform(0.5, 1)
    return plt_width, plt_height, plt_mass


def spawn_platform():
    global plt_width, plt_height, plt_mass
    # Calculate the number of Platforms to spawn
    num_platforms = random.randint(3, max_platforms - len(platforms))
    for _ in range(num_platforms):
        pltp_x = random.randint(plt_width + 50, res_x - ( 50 + plt_width))
        pltp_y = water_level
        plt_width, plt_height, plt_mass = random_platform()
        plt_buoyance = 2 / (plt_width * plt_mass)
        print(plt_buoyance)
        # Include the 'lives' argument when creating a CannonBall instance
        platform = Platform(pltp_x, pltp_y, plt_width, plt_height, water_level, water_density, gravity, plt_mass, plt_buoyance)
        platforms.append(platform)

def random_ball():
    global ball_radius, ball_mass
    # Generate random mass and radius
    ball_radius = random.randint(10, 50)
    ball_mass = random.randint(30, 100)
    return ball_radius, ball_mass


def spawn_cballs():
    global ball_radius, ball_mass
    # Calculate the number of CannonBalls to spawn
    num_balls = random.randint(1, max_cannonballs - len(cannonballs))
    for _ in range(num_balls):
        sp_x = random.randint(ball_radius, res_x - ball_radius)
        sp_y = 10
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ball_radius, ball_mass = random_ball()
        ball_speed = ball_radius * ball_mass
        # Include the 'lives' argument when creating a CannonBall instance
        ball = CannonBall(sp_x, sp_y, ball_radius, ball_mass, 0, ball_speed, color, water_level, gravity, pl_height, pl_lives)
        cannonballs.append(ball)


# Main game loop
def main():

    global pl_jump, cannonballs, remove_list, plt_mass, plt_buoyance

    # Define initial position
    pl_x, pl_y, pl_j_speed = 200, (water_level - pl_height), pl_jump 
    pl_accel_x = 0
    pl_vel_x = 0
    
    # Movement key hold confirmations
    move_l, move_r, jumping = False, False, False
    
    clock = pygame.time.Clock()
    # Keeping track of time
    ## Gives the current time
    start_time = time.time()
    ## 
    elapsed_time = 0

    # Initial spawn after 30 seconds
    next_spawn_time = 30
    
    # Create a Platform object
    #platform = Platform(random.randint(50, res_x - 50), water_level, plt_width, plt_height, water_level, water_density, gravity, plt_mass, buoyant_force)
    spawn_platform()

    # Game loop, runs forever
    while StartGame:
        # Delay while loop for 90 fps
        clock.tick(90)
        # Get the seconds since start of the while loop
        elapsed_time = time.time() - start_time
        
        # Player object
        player = pygame.Rect(pl_x, pl_y, pl_width, pl_height)
        # Clears the screen with the same backgroung image
        screen.blit(BGImg, (0, 0))
        # Draw ground
        pygame.draw.line(screen, (0, 0, 0), (0, water_level), (res_x, water_level), 2)
        # Update and draw the platform
        for platform in platforms:
            platform.update()
            platform.draw(screen)
        
        # Process events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                return
            # checks user input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_LEFT:
                    move_l = True
                if event.key == pygame.K_RIGHT:
                    move_r = True
                if event.key == pygame.K_UP:
                    jumping = True
                    pl_j_speed = pl_jump
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and move_l:
                    move_l = False
                if event.key == pygame.K_RIGHT and move_r:
                    move_r = False

        # Apply friction to the velocity
        if pl_vel_x > 0:
            pl_vel_x -= pl_friction
            if pl_vel_x < 0:
                pl_vel_x = 0
        elif pl_vel_x < 0:
            pl_vel_x += pl_friction
            if pl_vel_x > 0:
                pl_vel_x = 0

        # Check user input for movement
        if move_r:
            pl_accel_x = pl_accel
        elif move_l:
            pl_accel_x = -pl_accel
        else:
            pl_accel_x = 0

        # Update velocity based on acceleration
        pl_vel_x += pl_accel_x

        # Limit the velocity to the maximum speed
        if pl_vel_x > pl_max_speed:
            pl_vel_x = pl_max_speed
        elif pl_vel_x < -pl_max_speed:
            pl_vel_x = -pl_max_speed

        # Apply velocity to player's position
        pl_x += pl_vel_x

        # Check if inside bounds
        if pl_x + pl_width > res_x:
            pl_x = res_x - pl_width
        elif pl_x < 50:
            pl_x = 50

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

        # Check for collision between player and platform
        if player.colliderect(platform.get_rect()):
            print("Collide!")
            plt_mass += pl_mass
            plt_buoyance = 2 / (plt_width * plt_mass)
        else:
            plt_mass -= pl_mass
            # Apply buoyancy to the platform when the player is on top
            platform.set_buoyancy(plt_buoyance, time_step)
            platform.apply_buoyancy()

        
        if elapsed_time >= next_spawn_time:
            # Spawn CannonBalls if the maximum number is not reached
            if len(cannonballs) < max_cannonballs:
                spawn_cballs()
            # Schedule next spawn after 30 seconds
            next_spawn_time += 30
            
        time_step = 0.1

        # Update CannonBalls
        for ball in cannonballs:
            ball.update(time_step)

            # Delay between cannonball updates
            pygame.time.delay(cannonball_delay)

            # Remove CannonBalls that are offscreen or collided with the player
            if ball.offscreen or ball.collided_with_player:
                cannonballs[:] = [ball for ball in cannonballs if ball not in remove_list]

            # Handle CannonBall collisions
            ball.handle_cball_collision(player)

            # Draw CannonBalls
            for ball in cannonballs:
                ball.draw(screen)

        draw_text (f"Time: {round(elapsed_time)}s", font, TEXT_COL, (res_x / 2) - 110, 20)
        draw_text (f"Lives: {pl_lives}", font, TEXT_COL, 50, 20)

        platform.update()
        # Draw player in a determined location
        screen.blit(PLImg, player)
        # Update screen
        pygame.display.update()
        
main()
