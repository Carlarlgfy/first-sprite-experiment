import pygame
import random

class food:

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.radius = 6

        self.respawn()


    def respawn(self):

        self.x = random.randint(20, self.screen_width - 20)
        self.y = random.randint(20, self.screen_height - 20)


    def draw(self, screen):

        pygame.draw.circle(screen,(0,200,0),(self.x,self.y),self.radius)


    def get_position(self):

        return self.x, self.y
