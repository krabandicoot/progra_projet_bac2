import pygame


class Projectile:

    def __init__(self, x, y, vitesse, degats, image):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.degats = degats
        self.image = image

        self.mask= pygame.mask.from_surface(self.image) # IA

    @property
    def vitesse(self):
        return self._vitesse
    
    @vitesse.setter
    def vitesse(self, value):
        if value < 0:
            raise ValueError("La vitesse ne peut pas être négative.")
        self._vitesse = value

    def move(self):
        self.y = self.y - self.vitesse

    def draw(self, screen):
        screen.blit(self.image, (round(self.x), round(self.y)))

    def get_rect(self):
        return self.image.get_rect(topleft=(round(self.x), round(self.y)) )
    
    def __repr__(self):
        return f"Projectile(x={self.x}, y={self.y}, vitesse={self.vitesse}, degats={self.degats})"

class ProjectileNormal(Projectile):

    def __init__(self, x, y,image):
        super().__init__(x=x, y=y, vitesse=10, degats=1, image=image)


class ProjectileFort(Projectile):
    def __init__(self, x, y, image):
        super().__init__(x=x, y=y, vitesse=6, degats=2, image=image)


    