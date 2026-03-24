import pygame
import random
from utils import get_tight_hitbox

class food:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.image = pygame.image.load("fries.PNG").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.hitbox_offset = get_tight_hitbox(self.image)

        self.respawn()


    def respawn(self):

        self.x = random.randint(20, self.screen_width - 20 - self.width)
        self.y = random.randint(50, self.screen_height - 20 - self.height)


    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))


    def get_rect(self):
        hb = self.hitbox_offset
        return pygame.Rect(self.x + hb.x, self.y + hb.y, hb.width, hb.height)
