import pygame
import time
from pygame.math import Vector2

class Platform:
    def __init__(self, x, y, width, height, water_level, water_density, gravity, mass, buoyant_force):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.float_direction = -1
        self.water_level = water_level
        self.water_density = water_density
        self.gravity = gravity
        self.mass = mass
        self.b_force = buoyant_force
        self.submerged = False
        self.original_y = y
        self.target_buoyancy = buoyant_force

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        # Initial phase to start buoyancy: free-fall phase
        if self.y + self.height < self.water_level:  
            # Calculate the net force
            net_force = self.mass * self.gravity

            # Apply the net force to the rectangle's position
            acceleration = net_force / self.mass
            self.y += acceleration

        # Rectangle is in the buoyancy phase
        else:  
            # Calculate the submerged depth
            submerged_depth = (self.y + self.height) - self.water_level
            
            # Calculate the buoyant force based on the submerged depth and target buoyancy
            target_buoyant_force = (self.target_buoyancy - self.b_force) * submerged_depth / self.height + self.b_force

            # Calculate the net force
            net_force = self.mass * self.gravity - target_buoyant_force

            # Apply the net force to the rectangle's position
            acceleration = net_force / self.mass
            self.y += acceleration

    def set_buoyancy(self, target_buoyancy):
        self.target_buoyancy = target_buoyancy

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))