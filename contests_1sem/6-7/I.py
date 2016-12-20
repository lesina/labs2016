def Transpose(A):
    return list(map(list, zip(*A)))

def SwapColumns(A, i, j):
    for x in range(len(A)):
        A[x][i], A[x][j] = A[x][j], A[x][i]
    return A

def Rotate(A):
    for i in range(len(A)//2):
        A = SwapColumns(A, i, -i-1)
    return A

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
A = Rotate(Transpose(A))
for i in range(N):
    print(*A[i])
