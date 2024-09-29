from Lesson_2.character import Character


class Berserk(Character):
    max_health = 100
    last_chance = True

    def __init__(self, name, health, damage, defence):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = health

    def __str__(self):
        return Character.__str__(self) + \
                f' Дод. шкода: {self.count_additional_damage()}'

    def count_additional_damage(self):
        return round(max(self.damage * (1 - self.health / self.max_health), 0), 2)

    def take_damage(self, damage):
        real_damage = Character.take_damage(self, damage)

        if self.health <= 0 and self.last_chance:
            self.health = 1
            self.last_chance = False

        return real_damage

    def attack(self, target):
        return target.take_damage(
            self.damage + self.count_damage_offset() + self.count_additional_damage()
        )

