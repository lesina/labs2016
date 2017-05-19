def makeMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix


def bfs(n, colors, start = 0):
    #D = [0] * n
    #D[start] = 0
    visitedPairs = []
    answer = 0
    Queue = [start]
    Qstart = 0
    while Qstart < len(Queue):
        current = Queue[Qstart]
        Qstart += 1
        for v in range(len(matrix)):
            if matrix[current][v]:
                #D[v] = D[u] + 1
                if colors[v] != colors[current] and (v, current) not in visitedPairs and (current, v) not in visitedPairs:
                    answer += 1
                    visitedPairs.append((v, current))
                if v not in Queue:
                    Queue.append(v)
    return answer


n = int(input())
matrix = makeMatrix(n)
sapce = input()
colors = list(map(int, input().split()))
print(bfs(n, colors))