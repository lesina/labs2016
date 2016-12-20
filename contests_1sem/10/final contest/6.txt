def routes(x, y):
    route = [[0]*(x+2)]
    route.append([0] + [1]*(x+1))
    for i in range(y):
        route.append( [0, 1] + [None]*(x))
    for j in range(2, x+2):
        for i in range(2, y+2):
            route[i][j] = route[i][j-1] + route[i-1][j]
    print(route[-1][-1])


n, m = list(map(int, input().split()))
routes(n,m)
