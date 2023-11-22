from time import sleep
from enemy import Enemy
from player import Player
from actions import Action
from my_coloram import GREEN, RED


def main():
    print(f"{GREEN}Приветствуем вас в игре RPG Danger, сейчас вам предстоит создать своего персонажа.")
    Action.print_press_enter()
    print('-' * 35)
    player = Player.create_player()
    enemy_list = Enemy.create_enemy()
    while True:
        if not player.hp:
            sleep(1)
            Action.die()
        elif not enemy_list:
            Action.end_fight(player)
            enemy_list = Enemy.create_enemy()
        elif player.escaped:
            sleep(1)
            print(f"\t{RED}!!!---Ты позорно сбежал---!!!", end="")
            Action.die()
        Action.print_list_actions()
        Action.get_action(enemy_list, player)


if __name__ == "__main__":
    main()
