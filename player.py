from random import randint, choice


class Player:
    def __init__(self, name, class_, weapon):
        self.name = name
        self.class_ = class_
        self.weapon = weapon
        self.hp = 100
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
