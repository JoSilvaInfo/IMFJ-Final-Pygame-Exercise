import pygame
import math
# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Floor Friction Simulation")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Ball parameters
ball_radius = 20
ball_x = ball_radius
ball_y = height // 2
ball_speed = 40

ball_mass = 20  # Mass of the body in kg

floor_y = height // 2 #+ ball_radius  # Y-coordinate of the floor line

force_applied=0
force_increment=10

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
    
    t=0.05
    normal_force = ball_mass * gravity 

    coefficient_of_static_friction=0.2
    static_friction = coefficient_of_static_friction * normal_force
    net_force = force_applied - static_friction
    if(net_force>0):
       #kinetic friction
       coefficient_of_kinetic_friction =0.05
       kinetic_friction = coefficient_of_kinetic_friction * normal_force
       net_force = force_applied - kinetic_friction
       acceleration = net_force / ball_mass
       velocity_x = acceleration * t
    else: velocity_x=0   
    print("Net force ", net_force)
    
    # Update ball position
    if ball_x < width - ball_radius:
        ball_x += velocity_x

    # Check if ball is below the floor
    if ball_y > floor_y - ball_radius:
        ball_y = floor_y - ball_radius
    
    # Draw the scene
    screen.fill(BLACK)

    # Draw floor line
    pygame.draw.line(screen, BLUE, (0, floor_y), (width, floor_y), 3)

    # Draw ball
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)
    
    font = pygame.font.Font(None, 28) 
    string="Up/Down to change Force - Newtons: " + str(force_applied)
    text = font.render(string, True, (255, 255, 255))  # "Your text here" is
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)
    screen.blit(text, text_rect)
    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(20)

# Quit the game
pygame.quit()
