day = 1
week = 1
money = []
price, delta, m = list(map(int, input().split()))
while week <= m:
    money.append(price)
    price += delta
    day += 1
    if day is 8:
        day = 1
        week += 1
print(sum(money))
