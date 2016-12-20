n, m = list(map(int, input().split()))
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
MAX = A[0][0]
for i in range(n):
    if max(A[i]) > MAX:
        MAX = max(A[i])
x, y = 0, 0
for i in range(n):
    if MAX in A[i]:
        y = i
        x = A[i].index(MAX)
        break
print(y, x)
