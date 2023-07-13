import pygame
import math

class ShootBullet:
    def __init__(self, x, y, res_x, res_y, v0, angle, gravity, lives, water_level):
        # x and ycoordinate of the bullet
        self.x = x
        self.y = y
        # Screen width and height
        self.res_x = res_x
        self.res_y = res_y
        # Initial velocity of the bullet
        self.v0 = v0
        # Angle of projection of the bullet
        self.angle = angle
        # Time step
        self.dt = 0.1
        # x and y component of velocity
        self.vx = 0
        self.vy = 0
        # Time
        self.t = 0
        # Radius of the bullet
        self.radius = 5
        # Acceleration due to gravity
        self.gravity = gravity
        # Remaining lives of the bullet
        self.lives = lives
        # Y-coordinate of the water level
        self.water_level = water_level
        # Flag to indicate if the bullet is offscreen
        self.offscreen = False

    def update(self):
        # Increment time by the time step
        self.t += self.dt
        # Update the x-coordinate based on the x-component of velocity
        self.x += self.vx * self.dt
        # Update the y-coordinate based on the y-component of velocity and gravity
        self.y += self.vy * self.dt + 0.5 * self.gravity * self.dt**2
        # Update the y-component of velocity based on gravity
        self.vy += self.gravity * self.dt      
    
    def get_position(self):
        # Return the current position of the bullet
        return (self.x, self.y)
    
    def handle_collision(self, player):
        # Calculate the distance between the bullet and the player
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        # If the distance is less than or equal to the sum of the radii
        if distance <= self.radius + player.width:
            # Reduce the remaining lives of the bullet
            self.lives -= 1
            # Reset the x-coordinate of the bullet
            self.x = 10
            # Reset the y-coordinate of the bullet to the water level
            self.y = self.water_level
            # Return the updated remaining lives, x-coordinate, and y-coordinate
            return self.lives, self.x, self.y
            

    def is_on_screen(self):
        # Check if the bullet is on the screen
        return 0 <= self.x <= self.res_x and 0 <= self.y <= self.res_y
    
    def is_offscreen(self):
            # Reset the x-coordinate of the bullet
            self.x = 10
            # Reset the y-coordinate of the bullet to the water level
            self.y = self.water_level
            # Return the updated x-coordinate and y-coordinate
            return self.x, self.y
    
    def draw(self, img, screen):
        # Draw the bullet image on the screen at the current coordinates
        screen.blit(img, (self.x - self.radius, self.y - self.radius))
