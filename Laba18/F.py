size = int(input())
adjacency_matrix = []
list_of_edges = []
for i in range(size):
    adjacency_matrix.append(list(map(int, input().split())))
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j]:
            list_of_edges.append(tuple([i, j, adjacency_matrix[i][j]]))
for edge in list_of_edges:
    print(*edge)