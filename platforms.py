import pygame
from pygame.math import Vector2
import math

class Platform:
    def __init__(self, x, y, width, height, float_range, float_speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.float_range = float_range
        self.float_speed = float_speed
        self.float_direction = -1

    def update(self):
        # Move the platform up and down within the float range
        self.y += self.float_speed * self.float_direction

        # Reverse the float direction if the platform reaches the float range boundaries
        if abs(self.y - self.original_y) >= self.float_range:
            self.float_direction *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))