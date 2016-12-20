def SwapColumns(A, i, j):
    for x in range(len(A)):
        A[x][i], A[x][j] = A[x][j], A[x][i]
    return A

n, m = list(map(int, input().split()))
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
a, b = list(map(int, input().split()))
A = SwapColumns(A, a, b)
for i in range(n):
    print(*A[i])
