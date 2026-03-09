import pygame
from pygame.locals import *

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first sprite game")
# Load the sprite image

clock=pygame.time.Clock()

sprite = pygame.image.load("sprite1.PNG").convert_alpha()

x = 200
y = 200

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((30,30,30))

    screen.blit(sprite,(x,y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()