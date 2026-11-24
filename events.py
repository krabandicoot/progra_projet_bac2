import random

import pygame
from classes.projectile import ProjectileNormal, ProjectileFort

def handle_events(player, projectiles, bullet_img, bullet_sound, game_over):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not game_over:
                projectiles.append(
                    ProjectileNormal(player.x + 16, player.y + 10, bullet_img)
                )
                bullet_sound.play()

            elif event.key == pygame.K_x and not game_over:
                projectiles.append(
                    ProjectileFort(player.x + 16, player.y + 10, bullet_img)
                )
                bullet_sound.play()

    keys = pygame.key.get_pressed()

    player.x_change = 0

    if keys[pygame.K_LEFT]:
        player.x_change -= player.vitesse

    if keys[pygame.K_RIGHT]:
        player.x_change += player.vitesse

    return True


def update_game(player, enemies, projectiles, screen_width, explosion_sound, game_over=False):

    if game_over:
        return 0, True

    player.update(screen_width=screen_width)

    for enemy in enemies:
        enemy.update(screen_width=screen_width)
        if enemy.y + enemy.image.get_height() >= player.y:
            return 0, True

    # Déplacement des projectiles
    for projectile in projectiles:
        projectile.update()

    # Suppression des projectiles hors écran
    projectiles[:] = [
        projectile for projectile in projectiles
        if projectile.y + projectile.image.get_height() > 0
    ]

    score_gained = 0
    # Collisions
    for projectile in projectiles[:]:
        for enemy in enemies:
            if enemy.collides_with(projectile):
                enemy.take_damage(projectile.degats)
                explosion_sound.play()
                projectiles.remove(projectile)

                if not enemy.is_alive():
                    score_gained += enemy.score_value
                    new_x = random.randint(0,screen_width - enemy.image.get_width())
                    new_y = random.randint(50, 150)
                    enemy.reset(new_x, new_y)
                break

    return score_gained, False