import pygame

class character:

    def __init__(self, name, health, strength, x, y):
        self.name = name
        self.health = health
        self.strength = strength

        self.x = x
        self.y = y

        self.speed = 5

        self.sprite = pygame.image.load("sprite1.PNG").convert_alpha()


    def move(self, direction):

        if direction == "up":
            self.y -= self.speed

        if direction == "down":
            self.y += self.speed

        if direction == "left":
            self.x -= self.speed

        if direction == "right":
            self.x += self.speed


    def draw(self, screen):
        screen.blit(self.sprite,(self.x,self.y))
