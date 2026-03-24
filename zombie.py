import pygame
import math
from utils import get_tight_hitbox

class zombie:

    def __init__(self, x, y):

        self.x = float(x)
        self.y = float(y)

        self.vx = 0.0
        self.vy = 0.0
        self.accel = 0.3
        self.friction = 0.88
        self.max_speed = 4.5

        self.image = pygame.image.load("zombie.PNG").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.hitbox_offset = get_tight_hitbox(self.image)


    def update(self, player_x, player_y, screen_width, screen_height):

        dx = player_x - self.x
        dy = player_y - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)

        if dist > 0:
            effective_dist = max(dist, 5)
            self.vx += (dx / effective_dist) * self.accel
            self.vy += (dy / effective_dist) * self.accel

        self.vx *= self.friction
        self.vy *= self.friction

        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > self.max_speed:
            self.vx = self.vx / speed * self.max_speed
            self.vy = self.vy / speed * self.max_speed

        self.x += self.vx
        self.y += self.vy

        hb = self.hitbox_offset

        if self.x + hb.x < 0:
            self.x = -hb.x
            self.vx = abs(self.vx) * 0.75
        elif self.x + hb.x + hb.width > screen_width:
            self.x = screen_width - hb.x - hb.width
            self.vx = -abs(self.vx) * 0.75

        if self.y + hb.y < 0:
            self.y = -hb.y
            self.vy = abs(self.vy) * 0.75
        elif self.y + hb.y + hb.height > screen_height:
            self.y = screen_height - hb.y - hb.height
            self.vy = -abs(self.vy) * 0.75


    def on_fry_eaten(self):
        self.max_speed += 0.15
        self.accel += 0.02

    def draw(self, screen):

        screen.blit(self.image, (int(self.x), int(self.y)))


    def get_rect(self):
        hb = self.hitbox_offset
        return pygame.Rect(int(self.x) + hb.x, int(self.y) + hb.y, hb.width, hb.height)
