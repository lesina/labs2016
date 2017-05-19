def makeMatrix(start_x, start_y, finish_x, finish_y):
    matrix = []
    visited = []
    for i in range(8):
        matrix.append([0]*8)
        visited.append([False]*8)



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


chess_dict_tudim = {"a": 0, "b": 1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
chess_dict_sudim = {0: "a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7"h"}
start = int(input())
finish = int(input())
matrix = makeMatrix(chess_dict_tudim[start[0]], int(start[1])-1, chess_dict_tudim[finish[0]], int(finish[1])-1)
print(matrix)