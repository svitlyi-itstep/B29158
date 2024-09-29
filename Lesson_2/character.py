import random

class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0
    damage_offset = 0.2

    def __init__(self, name, health, damage, defence):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def show_stats(self):
        print(self)

    def __str__(self):
        return f' -< {self.name} >-\n' \
               f' Здоров`я: {self.health}\n'\
               f' Шкода: {self.damage}\n'\
               f' Захист: {self.defence}\n'

    def count_incoming_damage(self, damage):
        return round(max(damage * ((100 - self.defence) / 100), 0), 2)

    def count_damage_offset(self):
        return random.randint(0, int(self.damage * self.damage_offset)) * random.choice((-1, 1))

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        real_damage = self.count_incoming_damage(damage)
        self.health = round(max(self.health - real_damage, 0), 2)
        return real_damage

    def attack(self, target):
        return target.take_damage(self.damage + self.count_damage_offset())