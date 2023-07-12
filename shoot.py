import pygame
import math

class ShootBullet:
    def __init__(self, x, y, res_x, res_y, v0, angle, gravity, lives, water_level):
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
        self.radius = 5
        self.gravity = gravity
        self.lives = lives
        self.water_level = water_level
        self.offscreen = False

    def update(self):
        self.t += self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt + 0.5 * self.gravity * self.dt**2
        self.vy += self.gravity * self.dt      
    
    def get_position(self):
        return (self.x, self.y)
    
    def handle_collision(self, player):
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        if distance <= self.radius + player.width:
            self.lives -= 1
            self.x = 10
            self.y = self.water_level
            #print(self.x)
            #print(self.y)
            #print(self.lives)
            return self.lives, self.x, self.y
            

    def is_on_screen(self):
        return 0 <= self.x <= self.res_x and 0 <= self.y <= self.res_y
    
    def is_offscreen(self):
            self.x = 10
            self.y = self.water_level
            return self.x, self.y
    
    def draw(self, img, screen):
        #pygame.draw.circle(screen, (0,0,0), (int(self.x), int(self.y)), self.radius)
        screen.blit(img, (self.x - self.radius, self.y - self.radius))
