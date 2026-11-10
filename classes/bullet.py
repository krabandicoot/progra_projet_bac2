class Bullet:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.state = "ready"  # "ready" - ready to fire, "fire" - bullet is moving

    def fire(self):
        self.state = "fire"

    def reset(self):
        self.state = "ready"