class Player:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.vitesse = 5
        self.x_change = 0

    def move(self, screen_width):

        self.x += self.x_change

        if self.x <= 0:
            self.x = 0

        elif self.x >= screen_width - self.image.get_width():
            self.x = screen_width - self.image.get_width()

    def update(self, screen_width=800):
        """Met à jour la position du joueur."""
        self.move(screen_width)

    def draw(self, screen):
        screen.blit(self.image, (round(self.x), round(self.y)))

    def get_rect(self):
        return self.image.get_rect(topleft=(round(self.x), round(self.y)))
    
    def __repr__(self):
        return f"Player(x={self.x}, y={self.y}, vitesse={self.vitesse})"