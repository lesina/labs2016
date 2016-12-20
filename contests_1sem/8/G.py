string = list(input())
print(''.join(sorted(string[:string.index(".")], key = lambda x: ord(x)) + ["."]))
