import random

class Hero:
    def __init__(self, name, hp, attack, speed):
        self.name = name
        self._hp = hp
        self.attack = attack
        self.speed = speed

    @property
    def hp(self):
        return self._hp
    
    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)
        
    def is_alive(self):
        return self._hp > 0
        
    def __str__(self):
        return f"{self.name} [HP: {self._hp}]"
        
    def hit(self, target):
        target.take_damage(self.attack)

def battle(a, b):
    if a.speed > b.speed:
        attacker, defender = a, b
    elif b.speed > a.speed:
        attacker, defender = b, a
    else:
        attacker = random.choice([a, b])
        defender = b if attacker is a else a
        
    turns = 0
    while a.is_alive() and b.is_alive() and turns < 200:
        attacker.hit(defender)
        attacker, defender = defender, attacker
        turns += 1
        
    return a if a.is_alive() else b
        


# Тулаан!
a = Hero("Батаа", 100, 25, 7)
b = Hero("Сараа", 80, 35, 9)
print("Ялагч:", battle(a, b))
