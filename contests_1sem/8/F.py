d, n = list(map(int, input().split()))
answer = 0
while n%10:
    if n%10 == d:
        answer += 1
    n //= 10
print(answer)
