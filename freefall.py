import pygame
from pygame.math import Vector2
import math

class CannonBall:
    def __init__(self, x, y, radius, mass, angle_degrees, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.angle_rad = math.radians(angle_degrees)
        self.velocity = Vector2(speed * math.cos(self.angle_rad), speed * math.sin(self.angle_rad))
        # Friction factor to gradually slow down the velocity
        self.friction = 0.98 
        self.color = color 

    def update(self, time_step):
        self.x += self.velocity.x * time_step
        self.y += self.velocity.y * time_step
        
        # Apply friction to gradually slow down the velocity
        self.velocity *= self.friction

    def falling(self):
        if self.y + self.height < self.water_level:  # Rectangle is in the free-fall phase
                # Calculate the net force
                net_force = self.mass * self.gravity
            

                # Apply the net force to the rectangle's position
                acceleration = net_force / self.mass
                rectangle_y += acceleration
    
    
    def handle_cball_collision(self, player):
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if distance <= self.radius + player.radius:
            self.pl_lives -= 1

    def is_offscreen(self):
        return self.x > self.res_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
