import pygame
from pygame.math import Vector2
import math
import Main

class CannonBall():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.mass = 1.5
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
		#get position
        pygame.draw.rect(surface, "red", self.rect.topleft, self.width, self.height)
    
    def handle_cball_collision(self, player):
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if distance <= self.radius + player.radius:
            # Calculate the collision normal vector
            normal_vector = Vector2((player.x - self.x) / distance, (player.y - self.y) / distance)

            # Calculate the relative velocity
            relative_velocity = player.velocity - self.velocity

            # Calculate the dot product of relative velocity and collision normal
            dot_product = relative_velocity.dot(normal_vector)

            # Check if the balls are moving towards each other
            if dot_product < 0:
                Main.pl_lives -= 1