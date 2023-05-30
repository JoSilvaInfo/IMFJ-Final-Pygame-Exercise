import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Slope Friction Simulation")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Ball parameters
ball_radius = 20
ball_x = ball_radius
ball_y = ball_radius
ball_speed = 0  # Initial velocity

ball_mass = 20  # Mass of the body in kg

friction_coefficient = 0.02
slope_angle = 15  # Angle of the slope in degrees

floor_y = height // 2  # Y-coordinate of the floor line

force_applied = 0
force_increment = 10

# Gravitational force
gravity = 9.8

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                force_applied += force_increment
            elif event.key == pygame.K_DOWN:
                force_applied -= force_increment
    
    t = 0.05

    # Calculate the components of the slope vectors
    theta = math.radians(slope_angle)
    #vector_tangent_x = math.cos(theta)
    #vector_tangent_y = math.sin(theta)
    #vector_normal_x = math.cos(theta + math.pi/2)
    #vector_normal_y = math.sin(theta + math.pi/2)

    # Calculate the normal force on the ball
    normal_force = ball_mass * gravity * math.cos(theta + math.pi/2)

    # Calculate the static friction force
    coefficient_of_static_friction = 0.05
    static_friction = coefficient_of_static_friction * normal_force

    # Calculate the net force on the ball
    net_force = (force_applied + gravity) * math.sin(theta) - static_friction

    # Check if the ball is moving or at rest
    if net_force > 0:
        # Kinetic friction
        coefficient_of_kinetic_friction = 0.2
        kinetic_friction = coefficient_of_kinetic_friction * normal_force
        net_force = force_applied - kinetic_friction

        # Calculate the acceleration of the ball
        acceleration = net_force / ball_mass

        # Calculate the change in velocity
        delta_v = acceleration * t

        # Update the ball's velocity
        ball_speed += delta_v

    else:
        ball_speed = 0  # The ball is at rest

    # Update ball position
    if ball_x < width - ball_radius:
        ball_x += ball_speed * math.tan(theta)

    # Calculate the new y-coordinate based on the slope
    ball_y = floor_y - ball_radius + (ball_x - ball_radius) * math.tan(theta)



    # Draw the scene
    screen.fill(BLACK)

    # Draw slope line
    slope_start_x = ball_radius
    slope_start_y = floor_y - ball_radius
    slope_end_x = width - ball_radius
    slope_end_y = floor_y - ball_radius + (width - 2 * ball_radius) * math.tan(theta)
    pygame.draw.line(screen, BLUE, (slope_start_x, slope_start_y), (slope_end_x, slope_end_y), 2)

    # Draw ball
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    font = pygame.font.Font(None, 28) 
    string="Up/Down to change Force - Newtons: " + str(force_applied)
    text = font.render(string, True, (255, 255, 255))  # "Your text here" is
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)
    screen.blit(text, text_rect)
    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
