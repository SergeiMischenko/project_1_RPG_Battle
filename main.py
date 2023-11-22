from player import Player
from enemy import Enemy
from actions import Action
from my_coloram import GREEN, RED


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
        # Enemy.print_list_enemy(enemy_list)
        Action.print_list_actions()
        Action.get_action(enemy_list, player)
        # Action.do_attack()


if __name__ == "__main__":
    main()
