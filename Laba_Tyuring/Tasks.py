
class Tape:

    def __init__(self, tape_string=' ', blank_symbol=' '):
        self.__tape = dict(enumerate(tape_string))
        self.blank_symbol = blank_symbol

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return self.blank_symbol

    def __setitem__(self, index, char):
        self.__tape[index] = char

    def __str__(self):
        a = [self.blank_symbol]*(max(list(self.__tape.keys()))+1)
        for i in self.__tape:
            a[i] = self.__tape[i]
        return "".join(a)


class TuringCar():

    def __init__(self, tape, initial_state, final_states, d_function=None, blank_symbol=' '):
        self.__tape = tape
        self.__head_position = 0
        self.__current_state = initial_state
        self.__d_function = d_function
        self.__final_states = final_states

    def step(self):
        self.__current_state, self.__tape[self.__head_position], new_position =\
            self.__d_function[(self.__current_state, self.__tape[self.__head_position])]
        self.__head_position += new_position

    def is_final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False

    def get_tape(self):
        print(tape)


string = 'bacd'
tape = Tape(string)
initial_state = '0'
final_states = set(['f'])
blank_symbol = ' '
d_function = {('0', 'a'): ('a', ' ', 1),
              ('0', 'b'): ('b', ' ', 1),
              ('0', 'c'): ('c', ' ', 1),
              ('0', 'd'): ('d', ' ', 1),
              ('a', 'a'): ('a', 'a', 1),
              ('a', 'b'): ('a', 'b', 1),
              ('a', 'c'): ('a', 'c', 1),
              ('a', 'd'): ('a', 'd', 1),
              ('b', 'a'): ('b', 'a', 1),
              ('b', 'b'): ('b', 'b', 1),
              ('b', 'c'): ('b', 'c', 1),
              ('b', 'd'): ('b', 'd', 1),
              ('c', 'a'): ('c', 'a', 1),
              ('c', 'b'): ('c', 'b', 1),
              ('c', 'c'): ('c', 'c', 1),
              ('c', 'd'): ('c', 'd', 1),
              ('d', 'a'): ('d', 'a', 1),
              ('d', 'b'): ('d', 'b', 1),
              ('d', 'c'): ('d', 'c', 1),
              ('d', 'd'): ('d', 'd', 1),
              ('a', blank_symbol): ('f', 'a', 0),
              ('b', blank_symbol): ('f', 'b', 0),
              ('c', blank_symbol): ('f', 'c', 0),
              ('d', blank_symbol): ('f', 'd', 0)}
Machine = TuringCar(tape, initial_state, final_states, d_function)
while not Machine.is_final():
    Machine.step()
Machine.get_tape()

string = 'aabbcca'
initial_state = '0'
final_states = set(['f'])
blank_symbol = '_'
tape = Tape(string, blank_symbol)
d_function = {('0', 'a'): ('a', 'a', 1),
              ('0', 'b'): ('b', 'b', 1),
              ('0', 'c'): ('c', 'c', 1),
              ('0', 'd'): ('d', 'd', 1),
              ('a', 'a'): ('a', 'a', 1),
              ('a', 'b'): ('a', 'b', 1),
              ('a', 'c'): ('a', 'c', 1),
              ('a', 'd'): ('a', 'd', 1),
              ('b', 'a'): ('b', 'a', 1),
              ('b', 'b'): ('b', 'b', 1),
              ('b', 'c'): ('b', 'c', 1),
              ('b', 'd'): ('b', 'd', 1),
              ('c', 'a'): ('c', 'a', 1),
              ('c', 'b'): ('c', 'b', 1),
              ('c', 'c'): ('c', 'c', 1),
              ('c', 'd'): ('c', 'd', 1),
              ('d', 'a'): ('d', 'a', 1),
              ('d', 'b'): ('d', 'b', 1),
              ('d', 'c'): ('d', 'c', 1),
              ('d', 'd'): ('d', 'd', 1),
              ('a', blank_symbol): ('fa', blank_symbol, -1),
              ('b', blank_symbol): ('fb', blank_symbol, -1),
              ('c', blank_symbol): ('fc', blank_symbol, -1),
              ('d', blank_symbol): ('fd', blank_symbol, -1),
              ('fa', 'a'): ('delete', blank_symbol, -1),
              ('fb', 'b'): ('delete', blank_symbol, -1),
              ('fc', 'c'): ('delete', blank_symbol, -1),
              ('fd', 'd'): ('delete', blank_symbol, -1),
              ('fa', 'b'): ('f', 'b', 0),
              ('fa', 'c'): ('f', 'c', 0),
              ('fa', 'd'): ('f', 'd', 0),
              ('fb', 'a'): ('f', 'a', 0),
              ('fb', 'c'): ('f', 'c', 0),
              ('fb', 'd'): ('f', 'd', 0),
              ('fc', 'b'): ('f', 'b', 0),
              ('fc', 'a'): ('f', 'a', 0),
              ('fc', 'd'): ('f', 'd', 0),
              ('fd', 'b'): ('f', 'b', 0),
              ('fd', 'c'): ('f', 'c', 0),
              ('fd', 'a'): ('f', 'a', 0),
              ('delete', 'a'): ('delete', blank_symbol, -1),
              ('delete', 'b'): ('delete', blank_symbol, -1),
              ('delete', 'c'): ('delete', blank_symbol, -1),
              ('delete', 'd'): ('delete', blank_symbol, -1),
              ('delete', blank_symbol): ('f', blank_symbol, 0)}
Machine = TuringCar(tape, initial_state, final_states, d_function)
while not Machine.is_final():
    Machine.step()
Machine.get_tape()