def makeGraph(size, n):
    adjacency_list = []
    for i in range(size):
        adjacency_list.append([])
    for i in range(n):
        num, vertex = list(map(int, input().split()))
        adjacency_list[num].append(vertex)
        adjacency_list[vertex].append(num)
    return adjacency_list


def bfs(vertex):
    visitedEdges[vertex] = True
    for i in adjacency_list[vertex]:
        if not visitedEdges[i] and i not in queue:
            queue.append(i)
            if (vertex, i) not in BFS and (queue[0], i) not in BFS:
                BFS.append((vertex, i))
    while queue:
        bfs(queue.pop(0))

BFS = []
queue = []
size, n = list(map(int, input().split()))
adjacency_list = makeGraph(size, n)
visitedEdges = []
for i in range(size):
    visitedEdges.append(False)
for i in visitedEdges:
    if not i:
        index = visitedEdges.index(i)
        bfs(index)
        if BFS == []:
            print("(", index, ") - spanning tree")
        else:
            for adam in BFS:
                print(*adam)
        BFS = []