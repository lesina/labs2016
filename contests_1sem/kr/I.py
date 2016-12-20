def onLine(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    if ((x3 - x1) * (y2 - y1) == (y3 - y1) * (x2 - x1)) and ((z3 - z1) * (y2 - y1) == (y3 - y1) * (z2 - z1)) and ((x3 - x1) * (z2 - z1) == (z3 - z1) * (x2 - x1)):
        return True
    else:
        return False

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
if onLine(first[0], first[1], first[2], second[0], second[1], second[2], third[0], third[1], third[2]):
    ans = 1
else:
    ans = 0
for t in range(40):
    first[0] += first[3]
    second[0] += second[3]
    third[0] += third[3]
    first[1] += first[4]
    second[1] += second[4]
    third[1] += third[4]
    first[2] += first[5]
    second[2] += second[5]
    third[2] += third[5]
    if onLine(first[0], first[1], first[2], second[0], second[1], second[2], third[0], third[1], third[2]):
        ans += 1
if ans > 30:
    print(-1)
else:
    print(ans)
