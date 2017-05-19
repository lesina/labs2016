def makeMatrix(size, bridges):
    matrix = []
    for i in range(size):
        matrix.append([1000000]*size)
    for i in range(bridges):
        vertex1, vertex2, distance = list(map(int, input().split()))
        matrix[vertex1][vertex2] = distance
        matrix[vertex2][vertex1] = distance
    return matrix


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


cities = list(map(int, input().split()))
n = cities[0]
m = cities[1]
cities = cities[2:]
matrix = makeMatrix(n, m)
for i in range(n):
    mid_answer = Dexter(n, matrix, i)
    min_distance = 10000000
    res = 10000000
    for j in range(n):
        if j in cities:
            if mid_answer[j] < min_distance:
                min_distance = mid_answer[j]
                res = j
    print(res)