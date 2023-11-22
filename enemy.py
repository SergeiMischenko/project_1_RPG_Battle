from random import randint, choice
from time import sleep
from my_coloram import MAGENTA, BLUE, YELLOW, RED


class Enemy:
    ENEMY_RACES = {"Гоблин": {"Палка": 4, "Кинжал": 7, "Метательные ножи": 5},
                   "Орк": {"Дубина": 10, "Секира": 15, "Молот": 12},
                   "Чернокнижник": {"Посох": 10, "Жезл": 12, "Магический шар": 8}}

    def __init__(self, race):
        self.race = race
        match race:
            case 'Гоблин':
                self.hp = randint(5, 8)
                self.weapon = choice(list(self.ENEMY_RACES[self.race].keys()))
                self.damage = self.ENEMY_RACES[self.race][self.weapon]
                self.armor = 5 + randint(0, 8)
                self.xp = choice([5, 8, 10])
            case 'Орк':
                self.hp = randint(12, 20)
                self.weapon = choice(list(self.ENEMY_RACES[self.race].keys()))
                self.damage = self.ENEMY_RACES[self.race][self.weapon]
                self.armor = 10 + randint(2, 15)
                self.xp = choice([10, 12, 15, 20])
            case 'Чернокнижник':
                self.hp = randint(8, 12)
                self.weapon = choice(list(self.ENEMY_RACES[self.race].keys()))
                self.damage = self.ENEMY_RACES[self.race][self.weapon]
                self.armor = 0 + randint(0, 5)
                self.xp = choice([5, 8, 10, 12])
        self.gold = randint(0, 20)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'race' and hasattr(self, 'race'):
            print(f'{MAGENTA}Вы не можете изменять расу врага')
        else:
            object.__setattr__(self, key, value)

    @classmethod
    def create_enemy(cls, min_e=2, max_e=5):
        enemy_list = []
        for _ in range(randint(min_e, max_e)):
            enemy_list.append(Enemy(choice(list(cls.ENEMY_RACES.keys()))))
        return enemy_list

    @classmethod
    def enemy_attacks(cls, enemy_list, player, pl_buff_armor=0):
        enemy_list = cls._get_list_live_enemy(enemy_list)
        for enemy in enemy_list:
            cls._attack(enemy, player, pl_buff_armor)

    def _attack(self, player, pl_buff_armor=0):
        damage_resist = self.damage * (player.armor + pl_buff_armor) / 100
        damage = round(self.damage - damage_resist)
        player.hp -= damage
        print(
            f"{RED}{self.race}{YELLOW} наносит удар с помощью {BLUE}'{self.weapon}'"
            f"{YELLOW} по герою {BLUE}'{player.name}'{YELLOW}, урон: {RED}{damage}")
        if player.hp < 0:
            player.hp = 0
            print(f"{BLUE}'{player.name}'{YELLOW} погиб в бою от руки {RED}'{self.race}а'")
        else:
            print(f"{BLUE}{player.name}{YELLOW} у вас осталось {RED}{player.hp} {YELLOW}ОЗ")
        print('-' * 20)
        sleep(1)

    @staticmethod
    def _get_list_live_enemy(enemy_list):
        ind = 0
        while ind < len(enemy_list):
            if enemy_list[ind].hp <= 0:
                del enemy_list[ind]
            ind += 1
        return enemy_list

    @staticmethod
    def print_list_enemy(enemy_list):
        print("*" * 20)
        for ind, enemy in enumerate(enemy_list, 1):
            print(f"{RED}{ind}. {enemy.race} ({enemy.hp}) ОЗ")
        print("*" * 20)
