d = []
for i in range(101):
    d.append([0]*101)

def dec(n, k):
    if n >= 0 and k >= 0 and d[n][k] > 0:
        return d[n][k]
    if n < 0:
        return 0
    if n <= 1 or k == 1:
        return 1
    d[n][k] =  dec(n, k-1) + dec(n-k, k) 
    return d[n][k]


m = int(input())
for i in range(m):
    for j in range(m):
        d[i][j] = -1
print(dec(m, m))
