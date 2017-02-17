N = int(input())
dictionary = dict()

for i in range(N):
    name, number = input().split()
    dictionary[name] = [number]
for i in range(N):
    name, number = input().split()
    dictionary[name].append(number)

for name in dictionary:
    print(*dictionary[name])