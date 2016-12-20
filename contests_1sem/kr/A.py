v = int(input())
t = int(input())
s = v*t
while (s < 0):
    s += 109
print(s%109)
