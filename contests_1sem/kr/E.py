x, y =list(map(float, input().split()))
if y > (1 + x**2) or y < (-2 - x**2):
    print("YES")
else:
    print("NO")
