import random
import re

__author__ = 'Aleksei Lesovoi'
# -*- coding: utf8 -*-


class Monoalphabet:
    alphabet = "оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё"
    key      = "цщэгюбшжоячсматизхрйьлывнефёъкпуд"
    #key     = "цщэгюбшжоячс.а.изхр...ы.неф.ъ.п.."

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {self._encode[x]: x for x in self._encode}
        lowercase_code2 = {x: y for y, x in zip(self.alphabet, self.key)}
        uppercase_code2 = {x.upper(): y.upper() for y, x in zip(self.alphabet, self.key)}
        self._normDecode = dict(lowercase_code2)
        self._normDecode.update(uppercase_code2)
        self._normEncode = {self._normDecode[x]: x for x in self._normDecode}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])

    def normDecode(self, text):
        return ''.join([self._normDecode.get(char, char) for char in text])

    def normEncode(self, text):
        return ''.join([self._normEncode.get(char, char) for char in text])


def keyTable(text):
    keytable = {x: 0 for x in Monoalphabet.alphabet[:]}
    for char in text:
        if char.lower() in Monoalphabet.alphabet[:]:
            keytable[char.lower()] += 1
    keytable = sorted(keytable.items(), key=lambda x: x[1], reverse=True)
    keytable = [x[0] for x in keytable]
    return keytable

key = Monoalphabet.alphabet[:]
line = input()
cipher = Monoalphabet(keyTable(line))
print(cipher.encode(line))
print(keyTable(line))