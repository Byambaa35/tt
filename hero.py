import random

class Hero:
    def __init__(self, name, hp, attack, speed):
        self.name = name
        self.max_hp = hp
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

    def heal(self):
        """Дараагийн тулаанд орохын өмнө цусыг дүүргэх"""
        self._hp = self.max_hp
        
    def __str__(self):
        return f"{self.name} [HP: {self._hp}]"
        
    def hit(self, target):
        target.take_damage(self.attack)


def battle(a, b, show_log=True):    
    a.heal()
    b.heal()

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
        turns += 1
        
        if show_log:
            print(f"{attacker.name} → {defender.name}: {attacker.attack} хохирол. {defender}")
            
        attacker, defender = defender, attacker
        
    winner = a if a.is_alive() else b
    
    if show_log:
        print(f"Тулаан {turns} ээлжинд дууслаа. Ялагч: {winner}\n")
        
    return winner


print("=== ГАНЦААРЧИЛСАН ТУЛААН ===")
a = Hero("Батаа", 100, 25, 7)
b = Hero("Сараа", 80, 35, 9)
battle(a, b)


def tournament(heroes):
    print("=== ТЭМЦЭЭН ЭХЭЛЛЭЭ ===")
    wins = {hero.name: 0 for hero in heroes}
    
    for i in range(len(heroes)):
        for j in range(i + 1, len(heroes)):
            h1 = heroes[i]
            h2 = heroes[j]
            print(f"--- {h1.name} vs {h2.name} ---")
            winner = battle(h1, h2, show_log=True)
            wins[winner.name] += 1

    print("=== ТЭМЦЭЭНИЙ ДҮН ===")
    for name, score in wins.items():
        print(f"{name}: {score} ялалт")
        
    champion = max(wins, key=wins.get)
    print(f"\n Хамгийн олон ялсан аварга: {champion} ({wins[champion]} ялалт)")


heroes_list = [
    Hero("Батаа", 100, 25, 7),
    Hero("Сараа", 80, 35, 9),
    Hero("Дорж", 120, 20, 5),
    Hero("Болд", 90, 30, 8),
    Hero("Тэмүүлэн", 110, 22, 6)
]

tournament(heroes_list)
