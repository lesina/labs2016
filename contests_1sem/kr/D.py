array2D = list(map(int, input().split()))
array2D[:3], array2D[6:9] = array2D[6:9], array2D[:3]
print(*array2D)
