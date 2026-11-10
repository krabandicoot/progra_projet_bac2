class Display:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, ennemi):
        self.screen.blit(ennemi.image, ennemi.rect)