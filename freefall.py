import pygame
from pygame.math import Vector2
import math

class CannonBall:
    def __init__(self, x, y, radius, mass, angle_degrees, speed, color, water_level, gravity, height, lives, res_y):
        # x and y coordinate of the cannonball
        self.x = x
        self.y = y
        # Radius of the cannonball
        self.radius = radius
        # Mass of the cannonball
        self.mass = mass
        # Angle of projection in radians
        self.angle_rad = angle_degrees 
        # Initial velocity vector
        self.velocity = Vector2(0, speed * math.sin(self.angle_rad))
        # Friction factor to gradually slow down the velocity
        self.friction = 0.98
        # Color of the cannonball
        self.color = color 
        # Y coordinate of the water level
        self.water_level = water_level
        # Acceleration due to gravity
        self.gravity = gravity
        # Height of the cannonball above the ground
        self.height = height
        # Remaining lives of the cannonball
        self.lives = lives
        # Screen height
        self.screen_y = res_y
        # Flag to indicate if the cannonball collided with the player
        self.collided_with_player = False
        # Flag to indicate if the cannonball is offscreen
        self.offscreen = False

    def update(self, time_step, cannonballs):
        # Update the y-coordinate based on the vertical velocity
        self.y += self.velocity.y * time_step

        # Apply friction to gradually slow down the velocity
        self.velocity *= self.friction
        # Check if the cannonball is falling
        self.falling()

        if self.y > self.water_level:
            # Check if the cannonball is offscreen
            self.is_offscreen(cannonballs)

    def falling(self):
        # If the cannonball is above the ground
            if self.y + self.height < self.screen_y:  # Rectangle is in the free-fall phase
                # Calculate the net force acting on the cannonball
                net_force = self.mass * self.gravity
                
                # Calculate the acceleration based on the net force
                acceleration = net_force / self.mass
                # Update the y-coordinate of the cannonball based on the acceleration
                self.y += acceleration
    
    
    def handle_cball_collision(self, player, cannonballs):
        # Calculate the distance between the cannonball and the player
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        # If the distance is less than or equal to the sum of the radii
        if distance <= self.radius + player.height:
            # Reduce the remaining lives of the cannonball
            self.lives -= 1
            # Set the collided_with_player flag to True
            self.collided_with_player = True
            # Remove the cannonball from the list of cannonballs
            cannonballs.remove(self)

    def is_offscreen(self, cannonballs):
        # Set the offscreen flag to True
        self.offscreen = True
        # Remove the cannonball from the list of cannonballs
        cannonballs.remove(self)
    
    def draw(self, img, screen):
        # Draw the cannonball image on the screen at the current coordinates
        screen.blit(img, (self.x, self.y))