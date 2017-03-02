def makeAdjacencyMatrix():
    for i in range(size):
        adjacency_matrix.append([1000000] * size)
    for i in range(n):
        vertex1, vertex2 = list(map(int, input().split()))
        adjacency_matrix[vertex1][vertex2] = 1
        adjacency_matrix[vertex2][vertex1] = 1


def Dexter(size, adjacency_matrix, start=0):
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


adjacency_matrix = []
size = int(input())
n = int(input())
makeAdjacencyMatrix()
weight = Dexter(size, adjacency_matrix)
for i in range(len(weight)):
    print(weight[i])