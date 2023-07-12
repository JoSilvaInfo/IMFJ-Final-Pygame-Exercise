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
        player_x = player.x + player.width / 2
        player_y = player.y + player.height

        platform_left = self.x
        platform_right = self.x + self.width

        if self.y <= player_y <= self.y + (self.height + 50) and platform_left <= player_x <= platform_right:
            self.onPlatform = True
        else:
            self.onPlatform = False

        #player_x = (player.x + (player.width / 2)) 
        #player_y = (player.y + player.height)
        #platArea = self.x + self.width
        #distance_y = (platArea / 2) - player_y
        
        print(self.x)

        #if distance_y <= player.height and player_x >= self.x and player_x <= platArea:
            #self.onPlatform = True
            #print("Collide")
        #if distance_y > player_y:
            #self.onPlatform = False


    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))