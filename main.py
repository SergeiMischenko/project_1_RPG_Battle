from player import create_player
from enemy import create_enemy


def main():
    print(f"Приветствуем вас в игре RPG Battle, сейчас вам предстоит создать своего персонажа.")
    input("Нажмите ENTER чтобы продолжить...")
    create_player()
    create_enemy()


if __name__ == "__main__":
    main()
