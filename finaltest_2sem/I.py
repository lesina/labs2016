string = input()
numbers = list()
for i in range(len(string)):
    length = 1
    j = 1
    while string[i-j:i+j+1] == string[i-j:i+j+1][::-1] and i-j >= 0 and i+j+1<=len(string):
        j += 1
        length += 2
    numbers.append(length)
print(" ".join(map(str, numbers)))