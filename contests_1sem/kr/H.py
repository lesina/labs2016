def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return min([a, b])

N = int(input())
answer = []
for i in range(N):
    a, b = list(map(int, input().split()))
    if gcd(a,b) == 1:
        answer.append((a,b))
for pair in answer:
    print(pair[0], pair[1], sep = " ")
