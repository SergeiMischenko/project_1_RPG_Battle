"""Файл связанный с разными событиями"""

from random import randint, choice
from time import sleep
import sys

from my_coloram import RED, CYAN, YELLOW, GREEN
import actions
import enemy
import main


class Event:
    WALKS = ["Скитаемся...", "Скитаемся среди холмов...", "Проходим мимо густых зарослей...",
             "Топаем по узкой тропинке...", "Идём вдоль реки...", "Идём по долине мимо старого моста...",
             "Блуждаем среди высоких трав...", "Топаем по пустошам...", "Проходим мимо старого замка...",
             "Скитаемся среди туманных предгорий...", "Идём вдоль берега озера...", "Блуждаем по песчаным дюнам...",
             "Топаем по лабиринту узких улиц...", "Проходим мимо забытых руин...", "Блуждаем...",
             "Блуждаем среди теней старого леса...", "Блуждаем по лесу...", "Проходим мимо леса...",
             "Идём по дороге мимо холмов...", "Идём по полям мимо деревни...", "Следуем по следам...",
             "Проходим мимо заброшенных домов...", "Блуждаем по запутанным тропинкам...", "Идём вдоль дороги...",
             "Идём вдоль извилистой реки...", "Блуждаем среди золотых полей...", "Топаем по дремучему лесу...",
             "Проходим мимо скрытых пещер...", "Идём вдоль высоких скал...", "Блуждаем среди мрака ночи...",
             "Проходим мимо таинственных храмов...", "Идём вдоль берега моря...", "Блуждаем по бескрайним пустошам..."]

    QUEST = ["Вы оказываетесь на таинственном магическом рынке, где таинственный торговец предлагает вам сделку: \n"
             "он предоставит вам золото в обмен на истреблению опасных монстров, которые терроризируют его покупателей",
             "Глубоко в лесу вы обнаруживаете загадочную чашу с огненным светом, из которой появляется древний дух. \n"
             "Дух говорит вам о древнем проклятии, и чтобы его разрушить, вам нужно истребить определенное количество "
             "монстров, стражей леса.",
             "Городские стражники обращаются к вам за помощью в расследовании исчезновения караванов в окрестностях. \n"
             "Вы обнаруживаете, что местные монстры объединились, чтобы создать угрозу для торговых маршрутов,\n"
             "и именно вам предлагают устранить этот источник опасности.",
             "Во время своих приключений вы обнаруживаете древний магический портал, из которого начинают появляться "
             "зловещие твари.\nМудрый волшебник появляется перед вами и просит помочь ему закрыть портал, для чего "
             "необходимо очистить окрестность от монстров.",
             "Вам приходит послание от племени друидов, просящего о помощи в защите священного леса от нашествия "
             "монстров,\nкоторые начали разрушать природу и нарушать баланс.",
             "Исследуя древние подземелья, вы находите группу выживших, которые рассказывают вам о зловещих тварях, "
             "затаившихся в глубинах.\nОни уговаривают вас помочь им избавиться от угрозы в обмен на золото."]

    @staticmethod
    def situation(player, enemy_list=None):
        while True:
            situation = randint(0, 10)
            if player.quest:
                situation = randint(5, 10)
            if not player.hp or player.escaped:
                sleep(1)
                if player.escaped:
                    print(f"\t{RED}!!!---Ты позорно сбежал---!!!\n")
                    player.escaped, enemy_list = False, None
                    main.print_press_enter()
            elif enemy_list or situation > 8:
                if not enemy_list:
                    enemy_list = Event._meet_monster(player)
                actions.Action.print_list_actions()
                actions.Action.get_action(enemy_list, player)
                if not enemy_list:
                    actions.Action.end_fight(player)
            elif situation > 5 and player.hp != player.max_hp and player.gold:
                Event._meet_medic(player)
            elif situation > 4 and not player.quest:
                sleep(1)
                print(f"{CYAN}{choice(Event.QUEST)}")
                Event._meet_quest(player)
            else:
                sleep(1)
                input(f"{YELLOW}{choice(Event.WALKS)}")

    @staticmethod
    def _meet_monster(player):
        sleep(1)
        enemy_list = enemy.Enemy.create_enemy(player)
        print(f"{CYAN}Вы попали в западню, численность противника: {RED}[{len(enemy_list)}]")
        main.print_press_enter()
        return enemy_list

    @staticmethod
    def _meet_medic(player):
        while True:
            select = input(f"{CYAN}Вы обнаружили Хижину Травника на вашем пути, каков ваш следующий шаг? "
                           f"{RED}(Войти/Уйти): ").capitalize()
            if select == "Войти":
                sleep(1)
                print(f"\n{YELLOW}Вы вошли в хижину травника, и он может вас вылечить, но за это придется заплатить.")
                actions.Action.healing_at_the_medic(player)
                print(f"{GREEN}Вы покинули уютную хижину травника и продолжили свое приключение.")
                break
            elif select == "Уйти":
                break
        sleep(1)

    @staticmethod
    def _meet_quest(player):
        while True:
            select = input(f"{GREEN}Вы хотите взять это опасное задание? {RED}(Да/Нет): ").capitalize()
            if select == "Да":
                sleep(1)
                print(f"\n{YELLOW}Вы с некоторой настороженностью приняли на себя задачу по истреблению монстров.")
                player.quest = True
                break
            elif select == "Нет":
                print(f"\n{YELLOW}Вы решаете отказаться от этого рискованного задания. И продолжаете свой путь")
                break
        main.print_press_enter()
        sleep(1)

    @staticmethod
    def die():
        print(f"\n\t{RED}!!!-----ИГРА ОКОНЧЕНА-----!!!")
        sys.exit()
