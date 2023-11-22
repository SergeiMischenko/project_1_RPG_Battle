from player import Player
from enemy import Enemy
from actions import Action
from my_coloram import GREEN, RED
from time import sleep


def main():
    print(f"{GREEN}Приветствуем вас в игре RPG Danger, сейчас вам предстоит создать своего персонажа.")
    Action.print_press_enter()
    print('-' * 35)
    player = Player.create_player()
    enemy_list = Enemy.create_enemy()
    while True:
        if not player.hp or not enemy_list:
            print(f"\n\t{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
            break
        if player.escaped:
            sleep(1)
            print(f"\n\t{RED}!!!---Ты позорно сбежал---!!!")
            print(f"\t{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
            break
        Action.print_list_actions()
        Action.get_action(enemy_list, player)


if __name__ == "__main__":
    main()
