class Player:
    def __init__(self, health, stamina, atk_points):
        self.health = health
        self.stamina = stamina
        self.atk_points = atk_points

    def damage(self, health_points):
        self.health -= health_points

    def heal(self, hp):
        self.health += hp

    def stamina_change(self, stamina_points):
        self.stamina += stamina_points

    def reset_stats(self):
        self.health = 100
        self.stamina = 100


class Enemy:
    def __init__(self, type, health, position, size):
        self.type = type
        self.health = health
        self.position = position
        self.size = size

    def damage(self, player):
        self.health -= player.atk_points

    def move(self, distance):
        self.position += distance
