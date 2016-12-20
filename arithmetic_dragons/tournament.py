# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from graphics import *


def annoying_input_int(mess):
    answer = None
    try:
        answer = int(mess)
    except ValueError:
        answer = mess
    finally:
        return answer


def game_tournament(hero, enemy_list):
    for enemy in enemy_list:
        if str(enemy) == 'dragon':
            message('Вышел ' + enemy._color + ' дракон!')
        elif str(enemy) == 'troll':
            message('Вышел ' + enemy._size + ' тролль!')
        while enemy.is_alive() and hero.is_alive():
            answer = vopros('Вопрос: ' + enemy.question() + '\nОтвет:')
            answer = annoying_input_int(answer)

            if enemy.check_answer(answer):
                hero.attack(enemy)
                if str(enemy) == 'dragon':
                    message('Верно! \n** дракон кричит от боли **')
                elif str(enemy) == 'troll':
                    message('Верно! \n** тролль кричит от боли **')
            else:
                enemy.attack(hero)
                message('Ошибка! \n** вам нанесён удар... **')
        if enemy.is_alive():
            break
        if str(enemy) == 'dragon':
            message('Дракон ' + enemy._color + ' повержен!\n')
        elif str(enemy) == 'troll':
            message('Тролль ' + enemy._size + ' повержен!\n')

    if hero.is_alive():
        message('Поздравляем! Вы победили!')
        message('Ваш накопленный опыт: ' + str(hero._experience))
    else:
        message('К сожалению, Вы проиграли...')


def start_game():

    try:
        hero = Hero(
            vopros('Добро пожаловать в арифметико-ролевую игру с драконами и троллями! \n Представьтесь, пожалуйста: '))

        enemy_number = 3
        enemy_list = generate_enemy_list(enemy_number)
        assert(len(enemy_list) == 3)
        message('У Вас на пути ' + str(enemy_number) + ' противника!')
        game_tournament(hero, enemy_list)

    except EOFError:
        message('Поток ввода закончился. Извините, принимать ответы более невозможно.')
