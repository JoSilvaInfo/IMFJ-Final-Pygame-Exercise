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
            #submerged_volume=0.4  # m^3 (dimensions: 1m x 0.4m x 0.1m)
            submerged_volume=0.4*submerged_depth/self.height 
            
            rect_density = self.mass / submerged_volume
            if rect_density <= self.water_density:
                self.b_force += 0.1* rect_density * submerged_volume * self.gravity
                #time.sleep(0.1) 
                #print("up")
            else:
                self.b_force -= 0.1* self.water_density * submerged_volume * self.gravity
                #time.sleep(0.1) 
                #print("down") 
            
            # Calculate the net force
            net_force = self.mass * self.gravity - self.b_force
            # Apply the net force to the rectangle's position
            acceleration = net_force / self.mass
            self.y += acceleration

    def set_buoyancy(self, buoyancy):
        self.buoyancy = buoyancy

    def apply_buoyancy(self):
        if self.y < self.water_level:
            # Calculate the buoyancy force
            buoyancy_force = self.buoyancy * self.water_density * self.width * self.height
            # Apply the buoyancy force in the upward direction
            self.y -= buoyancy_force / self.mass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))