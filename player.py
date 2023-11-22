import actions
from time import sleep
from string import digits
from random import randint
from my_coloram import MAGENTA, BLUE, YELLOW, RED


class Player:
    CLASSES = {"Воин": {"Двуручный меч": 20, "Топорик": 15, "Кувалда": 18, "Меч и щит": 12},
               "Рейнджер": {"Кинжал": 10, "Меч": 14, "Лук": 16, "Арбалет": 18},
               "Маг": {"Посох": 14, "Жезл": 15, "Магический шар": 12}}

    def __init__(self, name, class_, weapon):
        self.name = name
        self.class_ = class_
        self.max_hp = 100
        self.hp = self.max_hp
        self.weapon = weapon
        self.damage = self.CLASSES[self.class_][self.weapon]
        match class_:
            case "Воин":
                match weapon:
                    case "Меч и Щит":
                        self.armor = 20 + randint(5, 15)
                    case _:
                        self.armor = 20
            case "Рейнджер":
                self.armor = 15
            case "Маг":
                self.armor = 10
        self.xp = 0
        self.level = 1
        self.gold = 0
        self.escaped = False

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    @classmethod
    def create_player(cls):
        name = cls._valid_name(input(f"{YELLOW}Введи имя своего героя: ").strip())
        cls._print_list()
        class_ = cls._valid_class(input(f"{BLUE}{name}{YELLOW} выбери класс из списка выше: ").capitalize())
        cls._print_list(class_=class_)
        weapon = cls._valid_weapon(input(f"{BLUE}{name}{YELLOW} выбери оружие из списка выше: ").capitalize(), class_)
        return Player(name, class_, weapon)

    def attack(self, enemy):
        damage_resist = self.damage * enemy.armor / 100
        damage = round(self.damage - damage_resist)
        enemy.hp -= damage
        print('-' * 20)
        print(f"{BLUE}{self.name}{YELLOW} наносит удар с помощью {BLUE}'{self.weapon}'"
              f"{YELLOW} по {RED}'{enemy.race}у'{YELLOW}, урон: {RED}{damage}")
        if enemy.hp <= 0:
            actions.Action.XP_FOR_FIGHT += enemy.xp
            actions.Action.GOLD_FOR_FIGHT += enemy.gold
            enemy.hp, enemy.xp, enemy.gold = 0, 0, 0
            print(f"{RED}'{enemy.race}' {YELLOW}повержен от вашей руки")
        else:
            print(f"{YELLOW}У {RED}'{enemy.race}а'{YELLOW} осталось {RED}{enemy.hp} {YELLOW}ОЗ")
        print('-' * 20)
        sleep(2)

    @staticmethod
    def _valid_name(name):
        while True:
            if not name:
                print(f"\n{MAGENTA}Имя не может быть пустым")
            elif name.startswith(tuple(digits)):
                print(f"\n{MAGENTA}Имя не может начинаться с цифр")
            else:
                break
            name = input(f"{YELLOW}Попробуй другое имя: ").strip()
        return name

    @classmethod
    def _valid_class(cls, value):
        classes_len = list(map(str, range(1, len(cls.CLASSES) + 1)))
        while True:
            if not value.strip():
                print(f"\n{MAGENTA}Ты же ничего не ввёл")
            elif value not in cls.CLASSES and value not in classes_len:
                print(f"\n{MAGENTA}Такого класса не существует, возможно ты ошибся")
            else:
                break
            value = input(f"{YELLOW}Попробуй ещё разок: ").capitalize()
        if value.isdigit():
            value = list(cls.CLASSES.keys())[int(value) - 1]
        return value

    @classmethod
    def _valid_weapon(cls, value, class_):
        class_weapon_len = list(map(str, range(1, len(cls.CLASSES[class_]) + 1)))
        while True:
            if not value.strip():
                print(f"\n{MAGENTA}Ты же ничего не ввёл")
            elif value not in cls.CLASSES[class_] and value not in class_weapon_len:
                print(f"\n{MAGENTA}Такого оружия не существует, возможно ты ошибся")
            else:
                break
            value = input(f"{YELLOW}Попробуй ещё разок: ").capitalize()
        if value.isdigit():
            value = list(cls.CLASSES[class_].keys())[int(value) - 1]
        return value

    @classmethod
    def _print_list(cls, class_=None):
        match class_:
            case None:
                classes = cls.CLASSES
            case _:
                classes = cls.CLASSES[class_]
        print('-' * 20)
        for ind, value in enumerate(classes, 1):
            print(f"{RED}\t{ind}. {value}")
        print('-' * 20)
        sleep(1)

    def print_stats_player(self):
        sleep(1)
        next_lvl_up = self.get_xp_for_next_lvl() - self.xp
        print(f"\n{BLUE}[{self.name}]{YELLOW} вы вооруженны {BLUE}[{self.weapon}]"
              f"{YELLOW} у него {RED}[{self.damage} ед. урона] {YELLOW}у вас {BLUE}[{self.armor} ед. брони]{YELLOW}, "
              f"{RED}[{self.hp}/{self.max_hp} ОЗ]{YELLOW}")
        print(f"{YELLOW}Вы {BLUE}[{self.level}-го Уровня]{YELLOW} до следующего уровня осталось "
              f"{BLUE}[{next_lvl_up} ед. опыта]\n")
        sleep(1)

    def check_and_change_lvl_up(self):
        self.xp += actions.Action.XP_FOR_FIGHT
        self.gold += actions.Action.GOLD_FOR_FIGHT
        xp_for_lvl_up = self.get_xp_for_next_lvl()
        while self.xp >= xp_for_lvl_up:
            self.xp -= xp_for_lvl_up
            self.level = self.level + 1
            _5_percent = 0.05
            self.max_hp += round(_5_percent * self.max_hp)
            self.hp = self.max_hp
            self.damage += round(_5_percent * self.damage)
            self.armor += round(_5_percent * self.armor)
            print(f"{BLUE}Вы повысили свой уровень на 1")

    def get_xp_for_next_lvl(self):
        percent_for_lvl_up = (self.level - 1) * 0.2
        return round(percent_for_lvl_up * 30 + 30)
