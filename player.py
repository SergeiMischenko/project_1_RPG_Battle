from random import randint, choice


class Player:
    def __init__(self, name, class_, weapon):
        self.name = name
        self.class_ = class_
        self.hp = 100
        self.weapon = weapon
        match class_:
            case "Воин":
                match weapon:
                    case "Меч и Щит":
                        self.armor = 20 + randint(5, 15)
                    case _:
                        self.armor = 20
            case "Рейнджер":
                self.armor = 8
            case "Маг":
                self.armor = 5
        self.xp = 0
        self.gold = 0


def create_player():
    classes = {"Воин": ["Двуручный Меч", "Топорик", "Кувалда", "Меч и Щит"],
               "Рейнджер": ["Кинжал", "Меч", "Лук"],
               "Маг": ["Посох", "Жезл", "Магический шар"]}

    print('-' * 35)
    name_player = valid_name(input("Введи имя своего героя: "))

    print('-' * 20)
    for ind, amount in enumerate(classes, 1):
        print(f"\t{ind}. {amount}")
    print('-' * 20)
    class_ = valid_class(input(f"{name_player} выбери свой класс из списка выше: "), classes)

    print('-' * 20)
    for ind, amount in enumerate(classes[class_], 1):
        print(f"\t{ind}. {amount}")
    print('-' * 20)
    weapon = valid_weapon(input(f"{name_player} выбери оружие для своего класса из списка выше: "), classes, class_)

    player = Player(name_player, class_, weapon)
    print()
    print(player.__dict__)


def valid_name(name):
    while True:
        if not name.strip():
            print("\nИмя не может быть пустым")
        elif name.startswith(tuple(str(map(str, range(10))) + ' ')):
            print("\nИмя не может начинаться с цифр или пробела")
        else:
            break
        name = input("Попробуй другое имя: ")
    return name


def valid_class(amount, classes):
    while True:
        if not amount.strip():
            print("\nТы же ничего не ввёл")
        elif amount not in classes and amount not in map(str, range(1, len(classes) + 1)):
            print("\nТакого класса не существует, возможно ты ошибся")
        else:
            break
        amount = input("Попробуй ещё разок: ")
    if amount.isdigit():
        amount = list(classes.keys())[int(amount) - 1]
    return amount


def valid_weapon(amount, classes, class_):
    while True:
        if not amount.strip():
            print("\nТы же ничего не ввёл")
        elif amount not in classes[class_] and amount not in map(str, range(1, len(classes[class_]) + 1)):
            print("\nТакого оружия не существует, возможно ты ошибся")
        else:
            break
        amount = input("Попробуй ещё разок: ")
    if amount.isdigit():
        amount = classes[class_][int(amount) - 1]
    return amount
