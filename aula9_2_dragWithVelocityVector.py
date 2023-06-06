import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Square Motion with Drag Simulation - using velocity vector")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Square parameters
square_size = 40
square_x = square_size
square_y = height // 2

# Velocity vector components
velocity_x = 5
velocity_y = 0

# Drag status
drag_active = False

# Air drag parameters
drag_coefficient = 0.1
air_density = 1.225

# Square mass
square_mass = 20

# Font
font = pygame.font.Font(None, 28)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                drag_active = True

    # Calculate the drag force
    drag_force = pygame.Vector2(0, 0)
    if drag_active:
        velocity_squared = velocity_x ** 2 + velocity_y ** 2 #magnitude da velocidade - pitagoras 
        drag_magnitude = 0.5 * drag_coefficient * air_density * velocity_squared
        drag_force = pygame.Vector2(-drag_magnitude * velocity_x, -drag_magnitude * velocity_y)

    # Calculate the acceleration based on drag force
    acceleration = drag_force / square_mass

    # Update velocity and position using the velocity vector
    velocity_x += acceleration.x
    velocity_y += acceleration.y
    square_x += velocity_x
    square_y += velocity_y

    # Check if the square reaches the right side of the screen
    if square_x > width - square_size:
        square_x = square_size
        velocity_x = 5
        velocity_y = 0
        drag_active = False

    # Draw the scene
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, pygame.Rect(square_x, square_y, square_size, square_size))

    # Draw message
    message = "Drag Force activates when space key is pressed"
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
