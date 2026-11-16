import math
import random

import pygame
from pygame import mixer

from classes.player import Player
from classes.enemy import BasicEnemy, BossEnemy
from classes.projectile import ProjectileNormal, ProjectileFort

# -------------------------
# INITIALISATION
# -------------------------

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('./pictures/ufo.png')
pygame.display.set_icon(icon)

# -------------------------
# BACKGROUND AND MUSIC
# -------------------------


# Background
background = pygame.image.load('./pictures/background.png')

# Sound
mixer.music.load("./sounds/background.wav")
mixer.music.play(-1)

bulletSound = mixer.Sound("./sounds/laser.wav")
explosionSound = mixer.Sound("./sounds/explosion.wav")

# -------------------------
# PLAYER
# -------------------------

playerImg = pygame.image.load('./pictures/player.png')
player=Player(370, 480, playerImg)

# -------------------------
# ENEMIES
# -------------------------

# Image des ennemis classiques
enemy_image = pygame.image.load("./pictures/enemy.png")
enemy_image = pygame.transform.smoothscale(
    enemy_image, (64, 64)
)

# Image du boss
boss_image = pygame.image.load("./pictures/boss.png")
boss_image = pygame.transform.smoothscale(
    boss_image, (200, 200)
)

enemies = []

# Création des ennemis classiques
for i in range(5):

    x = random.randint(0, 800 - enemy_image.get_width())
    y = random.randint(50, 150)

    enemy = BasicEnemy(x, y, enemy_image)
    enemies.append(enemy)

# Création du boss
boss = BossEnemy(300, 80, boss_image)
enemies.append(boss)

# -------------------------
# BULLET
# -------------------------

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving



bulletImg = pygame.image.load("./pictures/bullet.png")

projectiles=[]

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font("freesansbold.ttf", 64)

game_over = False

# -------------------------
# FONCTIONS
# -------------------------


def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value),
        True,
        (255, 255, 255)
    )
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )
    screen.blit(over_text, (200, 250))


# -------------------------
# GAME LOOP
# -------------------------

running = True

while running:

    # Affichage du fond
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Gestion des événements
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Touches enfoncées
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.x_change -= player.vitesse

            if event.key == pygame.K_RIGHT:
                player.x_change = player.vitesse

            if event.key == pygame.K_SPACE and not game_over:

                projectile= ProjectileNormal(player.x+16, player.y+10, bulletImg)
                
                projectiles.append(projectile)
                
                bulletSound.play()

            if event.key == pygame.K_x and not game_over:

                projectile = ProjectileFort(player.x + 16,player.y+10,bulletImg)

                projectiles.append(projectile)

                bulletSound.play()

                

        # Touches relâchées
        if event.type == pygame.KEYUP:

            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.x_change = 0

    # -------------------------
    # MISE A JOUR DU JEU
    # -------------------------

    if not game_over:

        # Déplacement du player
        player.move(800)

        # Déplacement des ennemis
        for enemy in enemies:

            # Déplacement individuel
            enemy.move(800)

            # Vérification du Game Over
            if enemy.y > 440:
                game_over = True
                break


        if not game_over:

            # Déplacement des projectiles
            for projectile in projectiles:
                projectile.move()

            # Suppression des projectiles hors écran
            projectiles = [
                projectile
                for projectile in projectiles
                if projectile.y + projectile.image.get_height() > 0
            ]

            # Collisions
            for projectile in projectiles[:]:

                for enemy in enemies:

                    if enemy.collides_with(projectile):

                        enemy.take_damage(projectile.degats)

                        explosionSound.play()

                        projectiles.remove(projectile)

                        if not enemy.is_alive():

                            score_value += enemy.score_value

                            new_x = random.randint(
                                0,
                                800 - enemy.image.get_width()
                            )

                            new_y = random.randint(50, 150)

                            enemy.reset(new_x, new_y)

                        break

    # -------------------------
    # AFFICHAGE
    # -------------------------

    # Affichage des ennemis
    if not game_over:
        for enemy in enemies:
            enemy.draw(screen)

    # Affichage du player
    player.draw(screen)

    # Affichage du score
    show_score(textX, textY)

    # Affichage Game Over
    if game_over:
        game_over_text()

    for projectile in projectiles:
        projectile.draw(screen)

    # Actualisation de l'écran
    pygame.display.update()


# -------------------------
# FERMETURE
# -------------------------

pygame.quit()
