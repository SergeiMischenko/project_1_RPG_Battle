"""Файл связанный с разными событиями"""

from random import randint, choice
from time import sleep
import sys

from my_coloram import RED, CYAN, YELLOW, GREEN
from enemy import Enemy
import actions
import main


class Event:
    WALKS = ["Блуждаем...", "Блуждаем по лесу...", "Проходим мимо леса...", "Идём вдоль дороги...",
             "Идём по дороге мимо холмов...", "Идём по полям мимо деревни..."]

    @staticmethod
    def situation(player, enemy_list=None):
        while True:
            situation = randint(0, 10)
            if not player.hp or player.escaped:
                sleep(1)
                if player.escaped:
                    print(f"\t{RED}!!!---Ты позорно сбежал---!!!\n")
                    player.escaped, enemy_list = False, None
                    main.print_press_enter()
            elif enemy_list or situation > 8:
                if not enemy_list:
                    enemy_list = Event._meet_monster()
                actions.Action.print_list_actions()
                actions.Action.get_action(enemy_list, player)
                if not enemy_list:
                    actions.Action.end_fight(player)
            elif situation > 5 and player.hp != player.max_hp and player.gold:
                Event._meet_medic(player)
            else:
                sleep(1)
                input(f"{YELLOW}{choice(Event.WALKS)}")

    @staticmethod
    def _meet_monster():
        sleep(1)
        enemy_list = Enemy.create_enemy()
        print(f"{CYAN}Вы встретили противников, количество врагов: {RED}[{len(enemy_list)}]")
        main.print_press_enter()
        return enemy_list

    @staticmethod
    def _meet_medic(player):
        while True:
            select = input(f"{CYAN}Вы встретили Хижину Травника на своём пути что будем делать? "
                           f"{RED}(Войти/Уйти): ").capitalize()
            if select == "Войти":
                sleep(1)
                print(f"\n{YELLOW}Вы зашли к травнику в его хижину, он может вас излечить, но это будет стоить денег")
                actions.Action.healing_at_the_medic(player)
                print(f"{GREEN}Вы покинули хижину травника и продолжили свое путешествие")
                break
            elif select == "Уйти":
                break
        sleep(1)

    @staticmethod
    def die():
        print(f"\n\t{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
        sys.exit()
