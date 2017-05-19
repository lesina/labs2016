def makeMatrix(size, bridges):
    matrix = []
    visited = [False] * size
    for i in range(size):
        matrix.append([0]*size)
    for i in range(bridges):
        vertex1, vertex2 = list(map(int, input().split()))
        matrix[vertex1][vertex2] = 1
        matrix[vertex2][vertex1] = 1
        if bfs(size, matrix):
            return i+1
    return bridges


def bfs(n, matrix, start = 0):
    #D = [0] * n
    #D[start] = 0
    visited = [False]*n
    #answer = 0
    Queue = [start]
    Qstart = 0
    while Qstart < len(Queue):
        current = Queue[Qstart]
        visited[Qstart] = True
        Qstart += 1
        for v in range(len(matrix)):
            if matrix[current][v]:
                #D[v] = D[u] + 1
                if v not in Queue:
                    Queue.append(v)
                    #answer += 1
    return False not in visited


n, m = list(map(int, input().split()))
matrix = makeMatrix(n, m)
print(matrix)