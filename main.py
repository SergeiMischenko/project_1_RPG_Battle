"""Главный исполняемый файл"""

from my_coloram import GREEN, RED
import players
import events


def main():
    """Главная исполняемая функция через которую запускается программа."""
    print(f"{GREEN}Добро пожаловать в мир RPG Battle! Следуйте подсказкам в тексте, "
          f"чтобы начать свое увлекательное приключение. \nВ начале вас ждет создание собственного персонажа "
          f"перед стартом вашего незабываемого путешествия.\n")
    print_press_enter()
    print('-' * 33)
    player = players.Player.create_player()  # Создание объекта player
    print(f"\n{GREEN}Теперь твоё путешествие начинается и ты отправляешь в путь, на встречу приключениям...\n")
    events.Event.situation(player, enemy_list=None)  # Запуск цикла событий с переданным объектом player


def print_press_enter():
    """Функция для отображения надписи - нажмите Enter, чтобы продолжить."""
    input(f"{GREEN}Нажмите {RED}ENTER, {GREEN}чтобы продолжить...")
    print()


if __name__ == "__main__":
    main()
