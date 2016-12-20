n, m, k = list(map(int, input().split()))
A = []
for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(0)
for x in range(k):
    i, j = list(map(int, input().split()))
    A[i-1][j-1] = "*"
for i in range(n):
    for j in range(m):
        if A[i][j] == "*" and n != 1 and m != 1:
            if i == 0 and j == 0:
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
                if A[i+1][j+1] != "*":
                    A[i+1][j+1] += 1
            elif i == 0 and j != 0 and j != len(A[0])-1:
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
                if A[i+1][j+1] != "*":
                    A[i+1][j+1] += 1
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
                if A[i+1][j-1] != "*":
                    A[i+1][j-1] += 1
            elif i == 0 and j == len(A[0])-1:
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
                if A[i+1][j-1] != "*":
                    A[i+1][j-1] += 1
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
            elif i == len(A)-1 and j == len(A[0])-1:
                if A[i-1][j-1] != "*":
                    A[i-1][j-1] += 1
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
            elif i == len(A)-1 and j == 0:
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
                if A[i-1][j+1] != "*":
                    A[i-1][j+1] += 1
            elif i == len(A)-1:
                if A[i-1][j-1] != "*":
                    A[i-1][j-1] += 1
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
                if A[i-1][j+1] != "*":
                    A[i-1][j+1] += 1
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
            elif j == 0:
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
                if A[i-1][j+1] != "*":
                    A[i-1][j+1] += 1
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
                if A[i+1][j+1] != "*":
                    A[i+1][j+1] += 1
            elif j == len(A[0]) - 1:
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
                if A[i-1][j-1] != "*":
                    A[i-1][j-1] += 1
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
                if A[i+1][j-1] != "*":
                    A[i+1][j-1] += 1
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
            else:
                if A[i-1][j-1] != "*":
                    A[i-1][j-1] += 1
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
                if A[i+1][j-1] != "*":
                    A[i+1][j-1] += 1
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
                if A[i+1][j+1] != "*":
                    A[i+1][j+1] += 1
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
                if A[i-1][j+1] != "*":
                    A[i-1][j+1] += 1
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
        elif A[i][j] == "*" and n == 1 and m != 1:
            if j == 0:
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
            elif j == len(A[0])-1:
                if A[i][j-1] != "*":
                    A[i][j+1] += 1
            else:
                if A[i][j-1] != "*":
                    A[i][j-1] += 1
                if A[i][j+1] != "*":
                    A[i][j+1] += 1
        elif A[i][j] == "*" and n != 1 and m == 1:
            if i == 0:
                if A[i+1][j] != "*":
                    A[i+1][j] += 1
            elif i == len(A)-1:
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
            else:
                if A[i-1][j] != "*":
                    A[i-1][j] += 1
                if A[i+1][j] != "*":
                    A[i+1][j] += 1

for i in range(n):
    print(*A[i])
