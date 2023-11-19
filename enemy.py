from random import randint, choice


class Enemy:
    def __init__(self, race):
        self.race = race
        self.gold = randint(0, 20)
        match race:
            case 'Гоблин':
                self.hp = randint(5, 8)
                self.weapon = choice(["Палка", "Кинжал", "Метательные ножи"])
                self.armor = 5 + randint(0, 8)
                self.xp = choice([5, 8, 10])
            case 'Орк':
                self.hp = randint(10, 20)
                self.weapon = choice(["Дубина", "Секира", "Молот"])
                self.armor = 10 + randint(2, 15)
                self.xp = choice([10, 12, 15, 20])
            case 'Чародей':
                self.hp = randint(8, 12)
                self.weapon = choice(["Посох", "Жезл", "Магический шар"])
                self.armor = 0 + randint(0, 5)
                self.xp = choice([5, 8, 10, 12])
            case _:
                self.hp = 5
                self.weapon = "Ветка"
                self.armor = 0
                self.xp = 2