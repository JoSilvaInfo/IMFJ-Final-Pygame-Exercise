import pygame
import time
from pygame.math import Vector2
import math

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
        self.ogMass = mass
        self.plt_mass = 3
        self.b_force = buoyant_force
        self.submerged = False
        self.onPlatform = False
        self.original_y = y

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
            submerged_depth = ((self.y + self.height) - self.water_level)
            
            # Calculate the buoyant force
            submerged_volume = 0.4 * submerged_depth/self.height 
            
            rect_density = self.mass / submerged_volume

            if self.onPlatform:
                self.mass = self.plt_mass
            else:
                self.mass = self.ogMass

            if rect_density < self.water_density:
                self.b_force += 0.1 * rect_density * submerged_volume * self.gravity
            else:
                self.b_force -= 0.1 * rect_density * submerged_volume * self.gravity
            
            # Calculate the net force
            net_force = self.mass * self.gravity - self.b_force
            # Apply the net force to the rectangle's position
            acceleration = net_force / self.mass
            self.y += 0.1 * acceleration

    def set_buoyancy(self, buoyancy):
        self.buoyancy = buoyancy

    def apply_buoyancy(self):
        if self.y < self.water_level:
            # Calculate the buoyancy force
            buoyancy_force = self.buoyancy * self.water_density * self.width * self.height
            # Apply the buoyancy force in the upward direction
            self.y -= buoyancy_force / self.mass

    def handle_collision(self, player):
        distance_x = math.sqrt(((player.x * 2) - (self.x * 2)) ** 2)
        distance_y = math.sqrt((player.y - self.y) ** 2)

        if distance_y <= player.height and distance_x <= player.width:
            self.onPlatform = True
            #print("Collide")
        else:
            self.onPlatform = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))