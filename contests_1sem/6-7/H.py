def Transpose(A):
    return list(map(list, zip(*A)))

n, m = list(map(int, input().split()))
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
A = Transpose(A)
for i in range(m):
    print(*A[i])
