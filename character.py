import pygame

class character:

    def __init__(self, name, health, strength, hunger, x, y):
        self.name = name
        self.health = health
        self.strength = strength
        self.hunger = hunger

        self.x = x
        self.y = y

        self.speed = 5

        self.sheet = pygame.image.load("player_sheet.PNG").convert_alpha()

        self.frames = []
        for i in range(4):
            frame = self.sheet.subsurface(pygame.Rect(i*64,0,64,64))
            self.frames.append(frame)

        self.current_frame = 0

        self.frame_left = self.frames[2]
        self.frame_right = pygame.transform.flip(self.frames[2], True, False)
        self.facing_right = False


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

        if self.current_frame == 2:
            if self.facing_right:
                screen.blit(self.frame_right,(self.x,self.y))
            else:
                screen.blit(self.frame_left,(self.x,self.y))
        else:
            screen.blit(self.frames[self.current_frame],(self.x,self.y))
