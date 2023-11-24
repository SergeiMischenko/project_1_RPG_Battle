"""Главный исполняемый файл"""

from my_coloram import GREEN, RED
import player
import events


def main():
    print(f"{GREEN}Приветствуем вас в игре RPG Danger, сейчас вам предстоит создать своего персонажа.")
    print_press_enter()
    print('-' * 35)
    player1 = player.Player.create_player()
    events.Event.situation(player1, enemy_list=None)


def print_press_enter():
    input(f"{GREEN}Нажмите " + f"{RED}ENTER" + f"{GREEN} чтобы продолжить...")


if __name__ == "__main__":
    main()
