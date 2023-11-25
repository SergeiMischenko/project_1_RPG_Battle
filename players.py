"""Файл связанный с Главным Героем"""

from random import randint
from string import digits
from time import sleep

from my_coloram import MAGENTA, BLUE, YELLOW, RED
import actions


class Player:
    """
    Класс для представления персонажа игрока.
    Attribute:
        CLASSES: dict[str: dict[str: int]] Словарь ключи это название класса персонажа,
        значение это словарь в котором, ключи - оружие, значение - урон данного оружия.
    Public Methods:
        create_player(cls)
        attack(self, enemy)
        print_stats_player(self)
        check_and_change_lvl_up
    """
    CLASSES = {"Воин": {"Двуручный меч": 20, "Топорик": 15, "Кувалда": 18, "Меч и щит": 12},
               "Рейнджер": {"Кинжал": 10, "Меч": 14, "Лук": 16, "Арбалет": 18},
               "Маг": {"Посох": 14, "Жезл": 15, "Магический шар": 12}}  # Можно добавлять классы и оружие

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
                    case "Меч и щит":
                        self.armor = 20 + randint(5, 15)  # Если класс Воин, оружие - Меч и щит, то даётся доп. броня
                    case _:
                        self.armor = 20
            case "Рейнджер":
                self.armor = 15
            case "Маг":
                self.armor = 10
            case _:
                self.armor = 15
        self.xp = 0
        self.level = 1
        self.gold = 0
        self.escaped = False
        self.stand = False
        self.quest = False

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    @classmethod
    def create_player(cls):
        """
        Возвращает объект класса Player с переданными аргументами: name, class_, weapon.
        Variables:
            name: str
                Имя для Героя после валидации.
            class_: str
                Класс для Героя после валидации.
            weapon: str
                Оружие для Героя после валидации.
        :return: Объект класса Player
        """
        name = cls._valid_name(input(f"{YELLOW}Введите имя для вашего персонажа:").strip())
        cls._print_list()  # Вывод списка классов
        class_ = cls._valid_class(input(f"{BLUE}{name}{YELLOW} выберите класс из списка выше: ").capitalize())
        cls._print_list(class_=class_)  # Вывод списка оружия для класса
        weapon = cls._valid_weapon(input(f"{BLUE}{name}{YELLOW} выберите оружие из списка выше: ").capitalize(), class_)
        sleep(1)
        return Player(name, class_, weapon)

    def attack(self, enemy):
        """
        Метод для объекта который наносит урон противнику после вычета damage resist.
        :param enemy: Enemy
            Живой противник из списка противников
        Variables:
            damage_resist: float
                Сколько урона будет заблокировано после просчёта - (урон Героя * на процент защиты противника)
            damage: int
                Какой урон нанесёт Герой по противнику после вычета damage_resist
        """
        damage_resist = self.damage * enemy.armor / 100
        damage = round(self.damage - damage_resist)
        enemy.hp -= damage
        print('-' * 20)
        print(f"{BLUE}{self.name}{YELLOW} наносит удар с помощью {BLUE}'{self.weapon}'"
              f"{YELLOW} по {RED}'{enemy.race}у'{YELLOW}, урон: {RED}{damage}")
        if enemy.hp <= 0:
            actions.Action.XP_FOR_FIGHT += enemy.xp  # Если противник умер, то его опыт идёт в зачёт за бой
            actions.Action.GOLD_FOR_FIGHT += enemy.gold  # Если противник умер, то его золото идёт в зачёт за бой
            enemy.hp = 0
            print(f"{RED}'{enemy.race}' {YELLOW}повержен от вашей руки")
        else:
            print(f"{YELLOW}У {RED}'{enemy.race}а'{YELLOW} осталось {RED}{enemy.hp} {YELLOW}ОЗ")
        print('-' * 20)
        sleep(1)

    @staticmethod
    def _valid_name(name):
        """
        Валидация входящего имени на пустоту и цифры.
        :param name: str
            Строка содержащая имя Героя
        :return: Имя Героя после проверок в виде строки
        """
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
        """
        Валидация входящего класса на пустоту и цифры.
        :param value: str
            Строка содержащая цифру или строку для класса Героя
        Variables:
            classes_len: list[str]
                Список с цифрами начиная с 1 по последний элемент в классах,
                нужен для проверки если пользователь введёт цифру
        :return: Класс для Героя в виде строки
        """
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
        """
        Валидация входящей строки для оружия на пустоту, цифры и наличия в классе.
        :param value: str
             Строка содержащая цифру или строку для оружия Героя
        :param class_: str
            Строка содержащая класс Героя
        Variables:
            classes_len: list[str]
                Список с цифрами начиная с 1 по последний элемент для оружия в классе,
                нужен для проверки если пользователь введёт цифру
        :return: Оружие Героя в виде строки
        """
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
        """
        Вывод списка классов или оружия для персонажа.
        :param class_: str
            Параметр отвечающий выводить список классов или список оружия для класса (Если None выводит классы,
            если передать класс в виде строки, то выведется список оружия для этого класса)
        """
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
        """
        Вывод характеристик Героя.
        Variables:
            next_lvl_up: int
                Сколько опыта осталось до следующего уровня
        """
        sleep(1)
        next_lvl_up = self._get_xp_for_next_lvl() - self.xp
        armor = self.armor
        if self.stand:
            armor = self.armor + 40  # Если стойка Героя True, то к броне в статистике добавляется 40 единиц
        print(f"\n{BLUE}[{self.name}]{YELLOW} вы вооруженны {BLUE}[{self.weapon}]"
              f"{YELLOW} у него {RED}[{int(self.damage)} ед. урона] {YELLOW}у вас {BLUE}[{int(armor)} ед. брони]"
              f"{YELLOW}, {RED}[{int(self.hp)}/{int(self.max_hp)} ОЗ]{YELLOW}")
        print(f"{YELLOW}Вы {BLUE}[{self.level}-го Уровня]{YELLOW} до следующего уровня осталось "
              f"{BLUE}[{int(next_lvl_up)} ед. опыта]\n")
        sleep(1)

    def _get_xp_for_next_lvl(self):
        """
        Возвращает число опыта для поднятия уровня, после добавления 20% за каждый уровень.
        Variables:
            percent_for_lvl_up: float
                вычисление процента
        :return: Число до след. уровня
        """
        percent_for_lvl_up = (self.level - 1) * 0.2  # Для каждого следующего уровня + 20% опыта
        return round(percent_for_lvl_up * 30 + 30)  # Изначально до второго уровня нужно 30 опыта

    def check_and_change_lvl_up(self):
        """
        Изменение уровня Героя, проверка и изменение характеристик персонажа.
        """
        self.xp += actions.Action.XP_FOR_FIGHT
        self.gold += actions.Action.GOLD_FOR_FIGHT
        xp_for_lvl_up = self._get_xp_for_next_lvl()  # Получение числа опыта до след. уровня
        while self.xp >= xp_for_lvl_up:
            self.xp -= xp_for_lvl_up
            self.level = self.level + 1
            _5_percent = 0.05  # 5% за уровень для характеристики
            self.max_hp += _5_percent * self.max_hp  # +5% к максимальному здоровью
            self.hp += 50  # 50 очков здоровья за поднятый уровень
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.damage += _5_percent * self.damage
            self.armor += _5_percent * self.armor
            print(f"{BLUE}Поздравляю! В бою вам удалось повысить свои навыки.")
