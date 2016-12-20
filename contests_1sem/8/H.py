n = int(input())
array = list(map(int, input().split()))
print(*sorted(array, key = lambda x: tuple(x%(10**(i+1)) for i in range(len(str(max(array)))))))
