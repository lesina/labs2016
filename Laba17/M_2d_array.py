n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
array = []
for i in range(n):
    array.append(numbers[i*m:i*m+m])
    print(*array[i])