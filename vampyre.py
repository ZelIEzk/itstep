from character import Character


class Vampyre(Character):
    max_health = 50

    def __init__(self, name, health=50, damage=2, defence=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = self.health

    def attack(self, target):
        Vamp_heal = self.damage * 0.5
        self.health = self.health + Vamp_heal
        target.take_damage(self.damage)