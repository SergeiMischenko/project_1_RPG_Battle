from player import Player
from enemy import Enemy
from my_coloram import MAGENTA, GREEN, YELLOW, RED


def main():
    print(f"{GREEN}Приветствуем вас в игре RPG Danger, сейчас вам предстоит создать своего персонажа.")
    input(f"{GREEN}Нажмите " + f"{RED}ENTER" + f"{GREEN} чтобы продолжить...")
    print('-' * 35)
    player = Player.create_player()
    enemy_list = Enemy.create_enemy()
    while True:
        if not player.hp or not enemy_list:
            print(f"\n\t{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
            break
        Enemy.print_list_enemy(enemy_list)
        fight(enemy_list, player)


def fight(enemy_list, player):
    target = valid_target(input(f"{YELLOW}Выберите кого атаковать: ").capitalize(), enemy_list)
    player.attack(enemy_list[target])
    Enemy.enemy_attacks(enemy_list, player)


def valid_target(value, enemy_list):
    enemy_len = list(map(str, range(1, len(enemy_list) + 1)))
    enemy_race_list = [enemy.race for enemy in enemy_list]
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


if __name__ == "__main__":
    main()
