n = int(input())
array = []
for i in range(n):
    array.append([])
    for j in range(n):
        array[i].append('.')
for i in range(n):
    for j in range(n):
        if i == j  or i == n//2 or j == n//2 or i == n-j-1:
            array[i][j] = "*"
for i in range(n):
    for j in range(n):
        print(array[i][j], end = " ")
    print()
