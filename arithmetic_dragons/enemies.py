# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
from math import sqrt

class Enemy(Attacker):
    pass


def decomposition(x):
    result = ""
    for i in range(2, x):
        while not x%i:
            result += str(i) + ","
            x //= i
    return result[:-1]


def isPrime(x):
    for i in range(2, int(sqrt(x))+1):
        if not x%i:
            return False
    return True


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def get_answer(self):
        return self.__answer

    def check_answer(self, answer):
        return answer == self.__answer

    def __str__(self):
        return "dragon"


class Troll(Enemy):
    _color = 'зеленый'

    def set_answer(self, answer):
        self.__answer = answer

    def get_answer(self):
        return self.__answer

    def check_answer(self,  answer):
        return answer == self.__answer

    def __str__(self):
        return "troll"


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 150
        self._attack = 12
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):  #учит умножению
    def __init__(self):
        self._health = 100
        self._attack = 15
        self._color = 'черный'

    def question(self):
        x = randint(1,15)
        y = randint(1,15)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class SmallTroll(Troll):
    def __init__(self):
        self._size = "маленький"
        self._health = 50
        self._attack = 5

    def question(self):
        a = randint(1,5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(a)
        return self.__quest


class MiddleTroll(Troll):
    def __init__(self):
        self._size = "средний"
        self._health = 200
        self._attack = 20

    def question(self):
        a = randint(2, 50)
        self.__quest = 'Простое ли число ' + str(a) + "?" + "(да/нет)"
        if isPrime(a):
            self.set_answer("да")
        else:
            self.set_answer("нет")
        return self.__quest


class BigTroll(Troll):
    def __init__(self):
        self._size = "большой"
        self._health = 100
        self._attack = 10

    def question(self):
        a = randint(4, 50)
        self.__quest = 'Разложи число на простые множители число ' + str(a) + " (Пример: 2,2,3,7. Если число простое, то нажмите Enter):"
        self.set_answer(decomposition(a))
        return self.__quest


enemy_types = [RedDragon, GreenDragon, BlackDragon, SmallTroll, MiddleTroll, BigTroll]