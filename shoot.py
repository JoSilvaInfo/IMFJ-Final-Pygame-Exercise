import pygame
import time
from pygame.math import Vector2

class ShootBullet:
    def __init__(self, x, y, res_x, res_y, v0, angle, gravity):
        self.x = x
        self.y = y
        self.res_x = res_x
        self.res_y = res_y
        self.v0 = v0
        self.angle = angle
        self.dt = 0.1
        self.vx = 0
        self.vy = 0
        self.t = 0
        self.radius=5
        self.gravity = gravity

    def update(self):
        self.t += self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt + 0.5 * self.gravity * self.dt**2
        self.vy += self.gravity * self.dt      
    
    def get_position(self):
        return (self.x, self.y)
    
    def is_on_screen(self):
        return 0 <= self.x <= self.res_x and 0 <= self.y <= self.res_y
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255,160,122), (int(self.x), int(self.y)), self.radius)
