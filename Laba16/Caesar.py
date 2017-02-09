__author__ = 'Aleksei Lesovoi'
# -*- coding: utf8 -*-


class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        self._encode = dict()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


key = int(input('Введите ключ:')) # 19
cipher = Caesar(key)
line = input()
while line!='.':
    print(cipher.decode(line))
    line = input()