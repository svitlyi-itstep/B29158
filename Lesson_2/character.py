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
        print(
            f' -< {self.name} >-\n'
            f' Здоров`я: {self.health}\n'
            f' Шкода: {self.damage}\n'
            f' Захист: {self.defence}\n'
        )
