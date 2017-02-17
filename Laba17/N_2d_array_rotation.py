def Transpose(A):
    B = []
    for i in range(len(A[0])):
        B.append([0]*len(A))
    for row in range(len(A)):
        for number in range(len(B)):
            B[number][row] = A[row][number]
    return B


def SwapColumns(A, i, j):
    for x in range(len(A)):
        A[x][i], A[x][j] = A[x][j], A[x][i]
    return A

def Rotate(A):
    for i in range(len(A[0])//2):
        A = SwapColumns(A, i, -i-1)
    return A

N, M = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
if len(A) > 1:
    A = Rotate(Transpose(A))
else:
    A = Transpose(A)
for i in range(M):
    print(*A[i])
