n = int(input())
array = input()
array = list(array)
if len(array)/2 < float(n):
    n = int(len(array)/2)
alph = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14, "c":15, "s":16, "h":17, "d":18}
for i in range(n):
    for j in range(n-1):
        if alph[array[2*j]] > alph[array[2*j+2]]:
            array[2*j], array[2*j+2] = array[2*j+2], array[2*j]
            array[2*j+1], array[2*j+3] = array[2*j+3], array[2*j+1]
        elif alph[array[2*j]] == alph[array[2*j+2]] and alph[array[2*j+1]] > alph[array[2*j+3]]:
            array[2*j+1], array[2*j+3] = array[2*j+3], array[2*j+1]
print("".join(array))
