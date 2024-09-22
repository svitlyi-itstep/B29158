class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

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

    def take_damage(self, damage):
        real_damage = round(damage * ((100 - self.defence) / 100), 2)
        self.health = round(max(self.health - real_damage, 0), 2)
        return real_damage

    def attack(self, target):
        return target.take_damage(self.damage)