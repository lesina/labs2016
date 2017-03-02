def makeGraph(n, m, mapa):
    size = n*m
    adjacency_list = []
    for i in range(size):
        adjacency_list.append([])
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == ' ' and j != m-1:
                if mapa[i][j+1] == ' ':
                    adjacency_list[i*m+j].append(i*m+j+1)
                    adjacency_list[i * m + j+1].append(i * m + j)
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == ' ' and i != n-1:
                if mapa[i+1][j] == ' ':
                    adjacency_list[i*m+j].append((i+1)*m+j)
                    adjacency_list[(i+1) * m + j].append((i) * m + j)
    return adjacency_list


def bfs(vertex):
    visitedEdges[vertex] = True
    for i in adjacency_list[vertex]:
        if not visitedEdges[i] and i not in queue:
            weight[i] = weight[vertex] + 1
            queue.append(i)
    while queue:
        bfs(queue.pop(0))


BFS = []
queue = []
n, m = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
MAP = []
for i in range(n):
    MAP.append(list(input()))
adjacency_list = makeGraph(n, m, MAP)
visitedEdges = [False] * (n*m)
weight = [0] * (n*m)
bfs((x1*m)+y1)
if weight[(x2*m)+y2]:
    print(weight[(x2*m)+y2])
else:
    print('INF')