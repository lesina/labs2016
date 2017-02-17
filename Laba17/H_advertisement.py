N = int(input())
items = list(map(int, input().split()))
items = sorted(items)
print(sum(items)-sum(items[:N//2]))