import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Hitting Wall Simulation")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Ball parameters
ball_radius = 20
ball_x = ball_radius
ball_y = height // 2
ball_velocity = pygame.Vector2(20, 0)  # Initial velocity vector

# Mass of the ball
ball_mass = 10

# Wall parameters
wall_x = width - 500

# Time step
time_step = 0.05

# Calculate the momentum of the ball
#initial_momentum = ball_mass * ball_velocity.x

# Calculate the force required to stop the ball
#force = -initial_momentum / time_step

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update ball position
    ball_x += ball_velocity.x * time_step

    # Check if ball hits the wall
    if ball_x >= wall_x - ball_radius:
        ball_x = wall_x - ball_radius
        ball_velocity.x = 0  # Stop the ball

    # Draw the scene
    screen.fill(BLACK)

    # Draw wall
    pygame.draw.line(screen, WHITE, (wall_x, 0), (wall_x, height), 3)

    # Draw ball
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
