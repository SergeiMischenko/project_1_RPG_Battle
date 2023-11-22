import enemy
from my_coloram import MAGENTA, YELLOW, RED


class Action:
    ACTIONS = {1: "Атаковать противника", 2: "Встать в защитную стойку (+40 Брони на 1 ход)",
               3: "Осмотреть противника", 4: "О себе", 5: "Сбежать с поля боя"}

    @staticmethod
    def handler_action(value, enemy_list, player):
        match value:
            case "1" | "Атаковать противника" | "Атаковать" | "Атака":
                enemy.Enemy.print_list_enemy(enemy_list)
                Action.do_attack(enemy_list, player)
            case "2" | "Встать в защитную стойку" | "Встать" | "Стойка":
                pl_buff_armor = 40
                player.stand = True
                enemy.Enemy.enemy_attacks(enemy_list, player, pl_buff_armor)
            case "3" | "Осмотреть противника" | "Осмотреть":
                enemy.Enemy.print_stats_enemy(enemy_list)

    @classmethod
    def print_list_actions(cls):
        print("-*" * 20)
        for ind, action in cls.ACTIONS.items():
            print(f"\t{YELLOW}{ind}. {action}")
        print("-*" * 20)

    @staticmethod
    def get_action(enemy_list, player):
        return Action.handler_action(input(f"{YELLOW}Выберите ваше действие из списка выше: ").capitalize(),
                                     enemy_list, player)

    @staticmethod
    def do_attack(enemy_list, player):
        target = Action.valid_target(input(f"{YELLOW}Выберите кого атаковать: ").capitalize(), enemy_list)
        player.attack(enemy_list[target])
        enemy.Enemy.enemy_attacks(enemy_list, player)

    @staticmethod
    def valid_target(value, enemy_list):
        enemy_len = list(map(str, range(1, len(enemy_list) + 1)))
        enemy_race_list = [enemy_.race for enemy_ in enemy_list]
        while True:
            if not value.strip():
                print(f"\n{MAGENTA}Ты же ничего не ввёл")
            elif value not in enemy_race_list and value not in enemy_len:
                print(f"\n{MAGENTA}Такого врага тут нет, возможно ты ошибся")
            else:
                break
            value = input(f"{YELLOW}Попробуй ещё разок: ").capitalize()
        if value.isalpha():
            value = enemy_race_list.index(value) + 1
        return int(value) - 1
