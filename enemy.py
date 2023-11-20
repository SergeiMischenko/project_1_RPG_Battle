from random import randint, choice


class Enemy:
    enemy_races = {"Гоблин": {"Палка": 4, "Кинжал": 7, "Метательные ножи": 5},
                   "Орк": {"Дубина": 10, "Секира": 15, "Молот": 12},
                   "Чародей": {"Посох": 10, "Жезл": 12, "Магический шар": 8}}

    def __init__(self, race):
        self.race = race
        match race:
            case 'Гоблин':
                self.hp = randint(5, 8)
                self.weapon = choice(list(self.enemy_races[self.race].keys()))
                self.damage = self.enemy_races[self.race][self.weapon]
                self.armor = 5 + randint(0, 8)
                self.xp = choice([5, 8, 10])
            case 'Орк':
                self.hp = randint(12, 20)
                self.weapon = choice(list(self.enemy_races[self.race].keys()))
                self.damage = self.enemy_races[self.race][self.weapon]
                self.armor = 10 + randint(2, 15)
                self.xp = choice([10, 12, 15, 20])
            case 'Чародей':
                self.hp = randint(8, 12)
                self.weapon = choice(list(self.enemy_races[self.race].keys()))
                self.damage = self.enemy_races[self.race][self.weapon]
                self.armor = 0 + randint(0, 5)
                self.xp = choice([5, 8, 10, 12])
        self.gold = randint(0, 20)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'race' and hasattr(self, 'race'):
            print('Вы не можете изменять расу врага')
        else:
            object.__setattr__(self, key, value)


def create_enemy():
    enemy1 = Enemy('Гоблин')
    enemy2 = Enemy('Орк')
    enemy3 = Enemy('Чародей')
    print(enemy1.__dict__)
    print(enemy2.__dict__)
    print(enemy3.__dict__)
