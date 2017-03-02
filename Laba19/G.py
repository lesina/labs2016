def makeAdjacencyMatrix():
    for i in range(size):
        adjacency_matrix.append([1000000] * size)
    for i in range(n):
        vertex1, vertex2, weight = list(map(int, input().split()))
        adjacency_matrix[vertex1][vertex2] = weight
        adjacency_matrix[vertex2][vertex1] = weight


def Dexter(size, adjacency_matrix, start = 0):
    valid = [True] * size
    weight = [1000000] * size
    weight[start] = 0
    for i in range(size):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(size):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(size):
            if weight[ID_min_weight] + adjacency_matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + adjacency_matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


def returnPath(retStart):
    Path.append(retStart)
    newWeight = weight[retStart]
    for j in range(size):
        for i in range(size):
            if (newWeight - adjacency_matrix[i][retStart] == weight[i]):
                newWeight -= adjacency_matrix[i][retStart]
                retStart = i
                Path.append(i)


Path = []
adjacency_matrix = []
size, n, start, end = list(map(int, input().split()))
makeAdjacencyMatrix()
weight = Dexter(size, adjacency_matrix, start)
print(weight[end])
# retStart = int(input())
# returnPath(retStart)
# print(*Path)