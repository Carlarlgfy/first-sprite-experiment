import pygame
from pygame.locals import *
from character import character

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fry Eats Fries")
# Load the sprite image

clock=pygame.time.Clock()

player = character("player",100,10,200,200)

x = 200
y = 200

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()


    if keys[K_w]:
        player.move("up")
        player.current_frame = 1

    if keys[K_s]:
        player.move("down")
        player.current_frame = 0

    if keys[K_a]:
        player.move("left")
        player.current_frame = 2
        player.facing_right = False

    if keys[K_d]:
        player.move("right")
        player.current_frame = 2
        player.facing_right = True

    screen.fill((255,255,255))

    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()