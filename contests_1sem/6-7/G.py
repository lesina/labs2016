def IsSymmetric(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i][j] != A[j][i]:
                return False
    return True

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
if IsSymmetric(A) and len(A[0]) == N:
    print("YES")
else:
    print("NO")
