F = [0]*3
G = [0]*3

n = int(input())
for i in range(3, n+1):
    F.append(F[i-1] + 2*G[i-2] + 1)
    G.append(F[i-2] + 2*G[i-1] - 1)
print(F[n])