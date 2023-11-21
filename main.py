from player import create_player
from enemy import Enemy, create_enemy
from my_coloram import GREEN, RED, YELLOW, MAGENTA


def main():
    print(f"{GREEN}Приветствуем вас в игре RPG Danger, тут вам предстоит создать своего персонажа.")
    input(f"{GREEN}Нажмите " + f"{RED}ENTER" + f"{GREEN} чтобы продолжить...")
    print('-' * 35)
    player = create_player()
    enemy_list = create_enemy()
    while True:
        enemy_list = Enemy.get_list_live_enemy(enemy_list)
        if not player.hp or not enemy_list:
            print(f"\n\t{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
            break
        Enemy.print_list_enemy(enemy_list)
        target = valid_target(input(f"{YELLOW}Выберите кого атаковать: ").capitalize(), enemy_list)
        player.attack(enemy_list[target])
        enemy_list[0].attack(player)


def valid_target(amount, enemy_list):
    enemy_len = list(map(str, range(1, len(enemy_list) + 1)))
    enemy_race_list = [enemy.race for enemy in enemy_list]
    while True:
        if not amount.strip():
            print(f"\n{MAGENTA}Ты же ничего не ввёл")
        elif amount not in enemy_race_list and amount not in enemy_len:
            print(f"\n{MAGENTA}Такого врага тут нет, возможно ты ошибся")
        else:
            break
        amount = input(f"{YELLOW}Попробуй ещё разок: ").capitalize()
    if amount.isalpha():
        amount = enemy_race_list.index(amount) + 1
    return int(amount) - 1


if __name__ == "__main__":
    main()
