import pygame
from pygame.math import Vector2
import math

class CannonBall:
    def __init__(self, x, y, radius, mass, angle_degrees, speed, color, water_level, gravity, height):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.angle_rad = math.radians(angle_degrees)
        self.velocity = Vector2(speed * math.cos(self.angle_rad), speed * math.sin(self.angle_rad))
        # Friction factor to gradually slow down the velocity
        self.friction = 0.98 
        self.color = color 
        self.water_level = water_level
        self.gravity = gravity
        self.height = height

    def update(self, time_step):
        self.x += self.velocity.x * time_step
        self.y += self.velocity.y * time_step
        
        # Apply friction to gradually slow down the velocity
        self.velocity *= self.friction
        
        self.falling()

    def falling(self):
        if self.y + self.height < self.water_level:  # Rectangle is in the free-fall phase
                # Calculate the net force
                net_force = self.mass * self.gravity
            

                # Apply the net force to the rectangle's position
                acceleration = net_force / self.mass
                self.y += acceleration
    
    
    def handle_cball_collision(self, player):
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if distance <= self.radius + player.height:
            self.pl_lives -= 1

    def is_offscreen(self):
        print("Delete")
        #return self.y > self.water_level
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
