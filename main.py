import pygame
from pygame.locals import *
from character import character
from food import food
from zombie import zombie

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fry Eats Fries")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)


def make_player():
    return character("player", 100, 10, 200, 200)

def make_zombie():
    return zombie(650, 400)

def make_food():
    return food(WIDTH, HEIGHT)


player = make_player()
chaser = make_zombie()
fries = make_food()

score = 0
game_over = False

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if game_over and event.type == KEYDOWN and event.key == K_r:
            player = make_player()
            chaser = make_zombie()
            fries = make_food()
            score = 0
            game_over = False

    if not game_over:

        keys = pygame.key.get_pressed()
        moving = False

        if keys[K_w]:
            player.move("up")
            player.current_frame = 1
            moving = True

        if keys[K_s]:
            player.move("down")
            player.current_frame = 0
            moving = True

        if keys[K_a]:
            player.move("left")
            player.current_frame = 2
            player.facing_right = False
            moving = True

        if keys[K_d]:
            player.move("right")
            player.current_frame = 2
            player.facing_right = True
            moving = True

        # Eating animation when near fries and standing still
        fries_dx = (player.x + 32) - (fries.x + fries.width // 2)
        fries_dy = (player.y + 32) - (fries.y + fries.height // 2)
        if not moving and (fries_dx ** 2 + fries_dy ** 2) ** 0.5 < 150:
            player.current_frame = 3

        player.update(WIDTH, HEIGHT)

        # Aim zombie's character center at player's character center (not raw frame coords)
        target_x = player.get_rect().centerx - chaser.hitbox_offset.centerx
        target_y = player.get_rect().centery - chaser.hitbox_offset.centery
        chaser.update(target_x, target_y, WIDTH, HEIGHT)

        # Hunger drains over time
        player.hunger -= 0.1
        if player.hunger < 0:
            player.hunger = 0

        # Health drains when starving
        if player.hunger == 0:
            player.health -= 0.08

        # Player picks up fries
        if player.get_rect().colliderect(fries.get_rect()):
            score += 1
            player.hunger = min(100.0, player.hunger + 30.0)
            fries.respawn()
            chaser.on_fry_eaten()

        # Zombie damages player on contact
        if player.get_rect().colliderect(chaser.get_rect()):
            player.health -= 0.3

        if player.health <= 0:
            game_over = True

    screen.fill((255, 255, 255))

    if not game_over:
        fries.draw(screen)
        player.draw(screen)
        chaser.draw(screen)

        # HUD
        score_surf = font.render(f"Fries: {score}", True, (20, 20, 20))
        screen.blit(score_surf, (10, 10))

        health_surf = small_font.render(f"HP: {int(player.health)}", True, (180, 0, 0))
        screen.blit(health_surf, (10, 42))

        # Hunger bar
        hunger_label = small_font.render("Hunger:", True, (20, 20, 20))
        screen.blit(hunger_label, (WIDTH - 190, 10))
        pygame.draw.rect(screen, (200, 200, 200), (WIDTH - 110, 13, 100, 18))
        bar_width = int(player.hunger)
        bar_color = (255, 165, 0) if player.hunger > 25 else (200, 0, 0)
        pygame.draw.rect(screen, bar_color, (WIDTH - 110, 13, bar_width, 18))

    else:
        over_surf = font.render(f"GAME OVER  |  Fries Eaten: {score}", True, (180, 0, 0))
        restart_surf = small_font.render("Press R to restart", True, (60, 60, 60))
        screen.blit(over_surf, (WIDTH // 2 - over_surf.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(restart_surf, (WIDTH // 2 - restart_surf.get_width() // 2, HEIGHT // 2 + 14))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
