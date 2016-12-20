a, b = list(map(int, input().split()))
array = []
for i in range(a):
    array.append([])
    for j in range(b):
        if (i+j) % 2:
            array[i].append('*')
        else:
            array[i].append('.')
#for i in range(n):
#    for j in range(n):
#        if i == j  or i == n//2 or j == n//2 or i == n-j-1:
#            array[i][j] = "*"
for i in range(a):
    for j in range(b):
        print(array[i][j], end = " ")
    print()
