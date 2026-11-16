
import pygame


class Enemy:
    def __init__(self, x, y, vitesse, pointvie, image,
                 score_value, distance_descente):
        self.x = x
        self.y = y

        self.vitesse = vitesse
        self.direction = 1
        self.distance_descente = distance_descente

        self.pointvie = pointvie
        self.max_pointvie = pointvie

        self.score_value = score_value

        self.image = image

        # Masque pour les collisions précises
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def pointvie(self):
        return self._pointvie

    @pointvie.setter
    def pointvie(self, value):
        if value < 0:
            raise ValueError("Les points de vie ne peuvent pas être négatifs.")
        self._pointvie = value

    def move(self, screen_width):
        # Déplacement individuel
        self.x += self.vitesse * self.direction

        if self.x >= screen_width - self.image.get_width():
            self.x = screen_width - self.image.get_width()
            self.direction = -1
            self.y += self.distance_descente

        elif self.x <= 0:
            self.x = 0
            self.direction = 1
            self.y += self.distance_descente

    def update(self, screen_width=800):
            """Met à jour la position de l'ennemi."""
            self.move(screen_width)
        

    def take_damage(self, damage=1):
        self.pointvie = max(0, self.pointvie - damage)

    def is_alive(self):
        return self.pointvie > 0

    def reset(self, x, y):
        # Réapparition de l'ennemi
        self.x = x
        self.y = y
        self.pointvie = self.max_pointvie
        self.direction = 1

    def draw(self, screen):
        screen.blit(
            self.image,
            (round(self.x), round(self.y))
        )

    def get_rect(self):
        return self.image.get_rect(
            topleft=(round(self.x), round(self.y))
        )

    def collides_with(self, projectile):
        # Collision pixel par pixel
        offset_x = round(projectile.x) - round(self.x)
        offset_y = round(projectile.y) - round(self.y)

        return self.mask.overlap(
            projectile.mask,
            (offset_x, offset_y)
        ) is not None


class BasicEnemy(Enemy):
    def __init__(self, x, y, image):
        super().__init__(
            x=x,
            y=y,
            vitesse=4,
            pointvie=1,
            image=image,
            score_value=1,
            distance_descente=40
        )


class BossEnemy(Enemy):
    def __init__(self, x, y, image):
        super().__init__(
            x=x,
            y=y,
            vitesse=2,
            pointvie=3,
            image=image,
            score_value=5,
            distance_descente=20
        )
