import random
from pathlib import Path

import pygame
from pygame import mixer

from classes.player import Player
from classes.enemy import BasicEnemy, BossEnemy
from events import handle_events, update_game


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def show_score(screen, font, score_value, x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_game_over(screen, over_font):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def main():
    # -------------------------
    # INITIALISATION
    # -------------------------
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("pictures/ufo.png")
    pygame.display.set_icon(icon)

    # -------------------------
    # ARRIERE-PLAN ET MUSIQUE
    # -------------------------
    background = pygame.image.load("pictures/background.png")
    mixer.music.load("./sounds/background.wav")
    mixer.music.play(-1)
    bullet_sound = mixer.Sound(str("./sounds/laser.wav"))
    explosion_sound = mixer.Sound("./sounds/explosion.wav")

    # -------------------------
    # JOUEUR & POLICES
    # -------------------------
    player_img = pygame.image.load("./pictures/player.png")
    player = Player(370, 480, player_img)

    score_value = 0
    font = pygame.font.Font(None, 32)
    over_font = pygame.font.Font(None, 64)  # Game Over
    text_x, text_y = 10, 10

    # -------------------------
    # ENNEMIS & PROJECTILES
    # -------------------------

    enemy_img = pygame.transform.smoothscale(pygame.image.load("./pictures/enemy.png"), (64, 64))
    boss_img = pygame.transform.smoothscale(pygame.image.load("./pictures/boss.png"), (200, 200))
    bullet_img = pygame.image.load("./pictures/bullet.png")

    enemies = [BasicEnemy(random.randint(0, SCREEN_WIDTH - enemy_img.get_width()), random.randint(50, 150), enemy_img) for _ in range(5)]
    enemies.append(BossEnemy(350, 50, boss_img))
    projectiles = []

    # -------------------------
    # BOUCLE PRINCIPALE (Game Loop)
    # -------------------------
    running = True
    game_over = False
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        screen.blit(background, (0, 0))

        # Gére les entrées et les événements
        running = handle_events(player, projectiles, bullet_img, bullet_sound, game_over)
        if not running:
            break

        score_gained, game_over = update_game(
            player,
            enemies,
            projectiles,
            SCREEN_WIDTH,
            explosion_sound,
            game_over,
        )
        score_value += score_gained

        # Draw the current game state.
        player.draw(screen)
        for projectile in projectiles:
            projectile.draw(screen)
        if not game_over:
            for enemy in enemies:
                enemy.draw(screen)

        show_score(screen, font, score_value, text_x, text_y)
        if game_over:
            show_game_over(screen, over_font)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
