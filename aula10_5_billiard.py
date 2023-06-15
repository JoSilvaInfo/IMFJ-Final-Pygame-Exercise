import pygame
from pygame.math import Vector2
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Billiard Simulation")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Ball class
class Ball:
    def __init__(self, x, y, radius, mass, angle_degrees, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.angle_rad = math.radians(angle_degrees)
        self.velocity = Vector2(speed * math.cos(self.angle_rad), speed * math.sin(self.angle_rad))
        self.friction = 0.98  # Friction factor to gradually slow down the velocity

    def update(self, time_step):
        self.x += self.velocity.x * time_step
        self.y += self.velocity.y * time_step
        
        # Apply friction to gradually slow down the velocity
        self.velocity *= self.friction
        
    def handle_wall_collision(self, width, height):
        bounciness = 1
        if self.x <= self.radius or self.x >= width - self.radius:
            self.velocity.x *= -bounciness
        if self.y <= self.radius or self.y >= height - self.radius:
            self.velocity.y *= -bounciness

    def handle_ball_collision(self, other_ball):
        distance = math.sqrt((other_ball.x - self.x) ** 2 + (other_ball.y - self.y) ** 2)
        if distance <= self.radius + other_ball.radius:
            # Calculate the collision normal vector
            normal_vector = Vector2((other_ball.x - self.x) / distance, (other_ball.y - self.y) / distance)

            # Calculate the relative velocity
            relative_velocity = other_ball.velocity - self.velocity

            # Calculate the dot product of relative velocity and collision normal
            dot_product = relative_velocity.dot(normal_vector)

            # Check if the balls are moving towards each other
            if dot_product < 0:
                # Calculate the impulse to determine the change in velocity
                impulse = (2 * dot_product) / (self.mass + other_ball.mass)

                # Update the velocities with the impulse
                self.velocity += impulse * other_ball.mass * normal_vector
                other_ball.velocity -= impulse * self.mass * normal_vector

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), self.radius)


# Create two balls
ball1 = Ball(100, height // 2, 20, 10, 35, 600)
ball2 = Ball(width - 100, height // 2, 20, 10, 130, 200)

# Time step
time_step = 0.05

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball positions
    ball1.update(time_step)
    ball2.update(time_step)

    # Handle collisions with walls and between balls
    ball1.handle_wall_collision(width, height)
    ball2.handle_wall_collision(width, height)
    ball1.handle_ball_collision(ball2)

    # Draw the scene
    screen.fill(BLACK)
    ball1.draw()
    ball2.draw()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
