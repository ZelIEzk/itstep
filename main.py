from berserk import Berserk
from vampyre import Vampyre

player1 = Vampyre('Vasya')
player2 = Berserk('Petya')

print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    character_damage = player1.damage
    berserk_damage = player2.attack(player1)

    print(f'{player1.name} нанёс {character_damage} урона.')
    print(f'{player2.name} нанёс {berserk_damage} урона.')
    print(player1)
    print(player2)