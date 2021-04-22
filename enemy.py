class Enemy:
    def __init__(self, health, position):
        self.health = health
        self.position = position

    def damage(self):
        self.health -= 10

    def get_position(self):
        return self.position

    def move(self, distance):
        self.position += distance