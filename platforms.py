import pygame
from pygame.math import Vector2

class Platform:
    def __init__(self, x, y, width, height, float_range, float_speed, water_level, water_density, gravity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.float_range = float_range
        self.float_speed = float_speed
        self.float_direction = -1
        self.water_level = water_level
        self.water_density = water_density
        self.gravity = gravity
        self.submerged = False
        self.original_y = y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        # Move the platform up and down within the float range
        self.y += self.float_speed * self.float_direction

        # Reverse the float direction if the platform reaches the float range boundaries
        if abs(self.y - self.original_y) >= self.float_range:
            self.float_direction *= -1

        # Check if the platform is submerged in water
        if self.y + self.height >= self.water_level:
            self.submerged = True
        else:
            self.submerged = False

    def calculate_buoyancy_force(self):
        # Calculate the volume of the submerged part of the platform
        submerged_height = self.y + self.height - self.water_level
        volume = self.width * submerged_height

        # Calculate the buoyant force using Archimedes' principle
        buoyant_force = volume * self.water_density * self.gravity

        return buoyant_force

    def apply_buoyancy(self):
        # Calculate the buoyant force
        buoyant_force = self.calculate_buoyancy_force()

        # Apply the buoyant force to the platform
        self.y -= buoyant_force

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))