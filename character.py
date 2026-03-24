import pygame
from utils import get_tight_hitbox

class character:

    def __init__(self, name, health, strength, x, y):
        self.name = name
        self.health = health
        self.strength = strength
        self.hunger = 100.0

        self.x = float(x)
        self.y = float(y)

        self.vx = 0.0
        self.vy = 0.0
        self.accel = 0.8
        self.friction = 0.92
        self.max_speed = 12

        self.sheet = pygame.image.load("player_sheet.PNG").convert_alpha()

        self.frames = []
        self.frame_hitboxes = []
        for i in range(4):
            frame = self.sheet.subsurface(pygame.Rect(i * 64, 0, 64, 64))
            self.frames.append(frame)
            self.frame_hitboxes.append(get_tight_hitbox(frame))

        self.current_frame = 0

        self.frame_left = self.frames[2]
        self.frame_right = pygame.transform.flip(self.frames[2], True, False)
        self.facing_right = False

        # Mirror the x offset for the flipped right-facing frame
        hb2 = self.frame_hitboxes[2]
        self.frame_hitbox_right = pygame.Rect(64 - hb2.right, hb2.y, hb2.width, hb2.height)


    def move(self, direction):

        if direction == "up":
            self.vy -= self.accel

        if direction == "down":
            self.vy += self.accel

        if direction == "left":
            self.vx -= self.accel

        if direction == "right":
            self.vx += self.accel


    def _current_hb(self):
        if self.current_frame == 2:
            return self.frame_hitbox_right if self.facing_right else self.frame_hitboxes[2]
        return self.frame_hitboxes[self.current_frame]

    def update(self, screen_width, screen_height):

        self.vx *= self.friction
        self.vy *= self.friction

        speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        if speed > self.max_speed:
            self.vx = self.vx / speed * self.max_speed
            self.vy = self.vy / speed * self.max_speed

        self.x += self.vx
        self.y += self.vy

        hb = self._current_hb()

        if self.x + hb.x < 0:
            self.x = -hb.x
            self.vx = abs(self.vx) * 0.8
        elif self.x + hb.x + hb.width > screen_width:
            self.x = screen_width - hb.x - hb.width
            self.vx = -abs(self.vx) * 0.8

        if self.y + hb.y < 0:
            self.y = -hb.y
            self.vy = abs(self.vy) * 0.8
        elif self.y + hb.y + hb.height > screen_height:
            self.y = screen_height - hb.y - hb.height
            self.vy = -abs(self.vy) * 0.8


    def draw(self, screen):

        if self.current_frame == 2:
            if self.facing_right:
                screen.blit(self.frame_right, (int(self.x), int(self.y)))
            else:
                screen.blit(self.frame_left, (int(self.x), int(self.y)))
        else:
            screen.blit(self.frames[self.current_frame], (int(self.x), int(self.y)))


    def get_rect(self):
        if self.current_frame == 2:
            hb = self.frame_hitbox_right if self.facing_right else self.frame_hitboxes[2]
        else:
            hb = self.frame_hitboxes[self.current_frame]
        return pygame.Rect(int(self.x) + hb.x, int(self.y) + hb.y, hb.width, hb.height)
