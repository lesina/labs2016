# coding: utf-8
# license: GPLv3
from gameunit import *
from enemies import Dragon


class Hero(Attacker):
    def __init__(self, name = 'Player1'):
        self._health = 100
        self._attack = 50
        self._experience = 0
        self._name = name

    def attack(self, target):
        target._health -= self._attack
        if target is Dragon():
            self._experience += 50
        else:
            self._experience += 25

    def gameOver(self):
        if self._health <= 0:
            print('К сожалению, Вы проиграли...')