from player import create_player, valid_target
from enemy import create_enemy, get_list_enemy, get_status_enemy
from my_coloram import GREEN, RED, YELLOW


def main():
    print(f"{GREEN}Приветствуем вас в игре RPG Danger, тут вам предстоит создать своего персонажа.")
    input(f"{GREEN}Нажмите " + f"{RED}ENTER" + f"{GREEN} чтобы продолжить...")
    player = create_player()
    enemy_list = create_enemy()
    while True:
        print()
        enemy_list = get_status_enemy(enemy_list)
        if not player.hp or not enemy_list:
            print(f"{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
            break
        get_list_enemy(enemy_list)
        target = valid_target(input(f"\n{YELLOW}Выберите кого атаковать: "), enemy_list)
        player.get_attack(enemy_list[target])
        enemy_list[0].get_attack(player)


if __name__ == "__main__":
    main()
