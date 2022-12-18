from character import Character


class Berserk(Character):
    max_health = 70

    def __init__(self, name, health=70, damage=3, defence=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = self.health

    def attack(self, target):
        additional_damage = self.damage * (self.max_health - self.health) / self.max_health
        total_damage = self.damage + additional_damage
        target.take_damage(total_damage)

        return total_damage