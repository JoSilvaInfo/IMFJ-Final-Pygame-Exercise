import pygame
import time
from pygame.math import Vector2
import math

class Platform:
    def __init__(self, x, y, width, height, water_level, water_density, gravity, mass, buoyant_force):
        # x and y coordinate of the platform
        self.x = x
        self.y = y
        # Width and height of the platform
        self.width = width
        self.height = height
        # Direction of float (upward or downward)
        self.float_direction = -1
        # Y-coordinate of the water level
        self.water_level = water_level
        # Density of water
        self.water_density = water_density
        # Acceleration due to gravity
        self.gravity = gravity
        # Mass of the platform
        self.mass = mass
        # Original mass of the platform
        self.ogMass = mass
        # Mass of the platform when a player is on it
        self.plt_mass = 3
        # Buoyant force experienced by the platform
        self.b_force = buoyant_force
        # Flag to indicate if the platform is submerged in water
        self.submerged = False
        # Flag to indicate if a player is on the platform
        self.onPlatform = False
        # Original y-coordinate of the platform
        self.original_y = y

    def get_rect(self):
        # Return the rectangle object representing the platform
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        # Initial phase to start buoyancy: free-fall phase
        if self.y + self.height < self.water_level:  
            # Calculate the net force
            net_force = self.mass * self.gravity

            # Apply the net force to the rectangle's position
            acceleration = net_force / self.mass
            self.y += acceleration

        # Platform is in the buoyancy phase
        else:  
            # Calculate the submerged depth
            submerged_depth = ((self.y + self.height) - self.water_level)
            
            # Calculate the submerged volume based on submerged depth
            submerged_volume = 0.4 * submerged_depth/self.height 
            
            # Calculate the density of the platform based on its mass and submerged volume
            rect_density = self.mass / submerged_volume

            if self.onPlatform:
                # Set the mass of the platform to plt_mass when a player is on it
                self.mass = self.plt_mass
            else:
                # Set the mass of the platform to its original mass
                self.mass = self.ogMass

            if rect_density < self.water_density:
                # Increase buoyant force if the density is less than water density
                self.b_force += 0.1 * rect_density * submerged_volume * self.gravity
            else:
                # Decrease buoyant force if the density is greater than water density
                self.b_force -= 0.1 * rect_density * submerged_volume * self.gravity
            
            # Calculate the net force
            net_force = self.mass * self.gravity - self.b_force

            # Apply the net force to the rectangle's position
            acceleration = net_force / self.mass
            # Update the y-coordinate of the platform
            self.y += 0.1 * acceleration

    def set_buoyancy(self, buoyancy):
        # Set the buoyancy of the platform
        self.buoyancy = buoyancy

    def apply_buoyancy(self):
        if self.y < self.water_level:
            # Calculate the buoyancy force
            buoyancy_force = self.buoyancy * self.water_density * self.width * self.height
            # Apply the buoyancy force in the upward direction
            self.y -= buoyancy_force / self.mass

    def handle_collision(self, player):
        # Calculate player's width and height middle
        player_x = player.x + player.width / 2
        player_y = player.y + player.height
        # Calculate the surface area of the platfrom
        platArea = self.x + self.width
        # Calculate the distance between the paltform and the player
        distance_y = (platArea / 2) - player_y

        platform_left = self.x
        platform_right = self.x + self.width

        if distance_y <= player.height and platform_left <= player_x <= platform_right:
            # Set the onPlatform flag to True if the player is on the platform
            self.onPlatform = True
        else:
            # Set the onPlatform flag to False if the player is not on the platform
            self.onPlatform = False


    def draw(self, img, screen):
        # Draw the platform image on the screen at the current coordinates
        screen.blit(img, (self.x, self.y))