from player import Player
from enemy import Enemy


def create_player(name_player=None, class_=None, weapon=None):
    classes = ["Воин", "Рейнджер", "Маг"]
    weapons_warrior = ["Двуручный Меч", "Топорик", "Кувалда", "Меч и Щит"]
    weapons_ranger = ["Кинжал", "Меч", "Лук"]
    weapons_wizard = ["Посох", "Жезл", "Магический шар"]
    print(f"Приветствуем вас в игре RPG Battle, сейчас вам предстоит создать своего персонажа.")
    input("Нажмите ENTER чтобы продолжить...")
    print()
    while not name_player:
        amount = input("Введите имя своего героя: ")
        name_player = amount
    for ind, amount in enumerate(classes, 1):
        print(f"\t{ind}. {amount}")
    while not class_ or class_ not in classes and class_ not in map(str, range(1, len(classes) + 1)):
        amount = input("Выберите класс персонажа: ")
        class_ = amount
    match class_:
        case 'Воин' | '1':
            class_ = 'Воин'
            for ind, amount in enumerate(weapons_warrior, 1):
                print(f"\t{ind}. {amount}")
            while not weapon or weapon not in weapons_warrior and weapon not in map(str,
                                                                                    range(1, len(weapons_warrior) + 1)):
                amount = input("Выберите оружие для персонажа: ")
                if amount.isdigit():
                    weapon = weapons_warrior[int(amount) - 1]
                else:
                    weapon = amount
        case 'Рейнджер' | '2':
            class_ = 'Рейнджер'
            for ind, amount in enumerate(weapons_ranger, 1):
                print(f"\t{ind}. {amount}")
            while not weapon or weapon not in weapons_ranger and weapon not in map(str,
                                                                                   range(1, len(weapons_ranger) + 1)):
                amount = input("Выберите оружие для персонажа: ")
                if amount.isdigit():
                    weapon = weapons_ranger[int(amount) - 1]
                else:
                    weapon = amount
        case 'Маг' | '3':
            class_ = 'Маг'
            for ind, amount in enumerate(weapons_wizard, 1):
                print(f"\t{ind}. {amount}")
            while not weapon or weapon not in weapons_wizard and weapon not in map(str,
                                                                                   range(1, len(weapons_wizard) + 1)):
                amount = input("Выберите оружие для персонажа: ")
                if amount.isdigit():
                    weapon = weapons_wizard[int(amount) - 1]
                else:
                    weapon = amount

    player = Player(name_player, class_, weapon)
    print()
    print(player.__dict__)


def create_enemy():
    enemy1 = Enemy('Гоблин')
    enemy2 = Enemy('Орк')
    enemy3 = Enemy('Чародей')
    print(enemy1.__dict__)
    print(enemy2.__dict__)
    print(enemy3.__dict__)


def main():
    create_player()
    create_enemy()


if __name__ == "__main__":
    main()
