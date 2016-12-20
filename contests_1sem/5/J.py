N = int(input())
ans = 0
money = list(map(int, input().split()))
money = money[::-1]
i = 0
while money[i] == 5:
    i += 1
    if i == len(money):
        break
money = money[i:]
for monetka in money:
    ans += (monetka - 5) // 5
    if monetka == 5:
        ans -= 1
if ans < 0:
    ans = 0
print(ans)
