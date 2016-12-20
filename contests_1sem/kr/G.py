from math import sqrt

def isSimple(s):
    for i in range(2, int(sqrt(s))+1):
        if s % i == 0:
            return False
    return True

def sumNumbers(s):
    res = 0
    while s != 0:
        res += s % 10
        s //= 10
    return res

a, b, k = list(map(int, input().split()))
res = []
for x in range(a, b+1):
    if isSimple(x) and sumNumbers(x) == k:
        res.append(x)
print(*res)
