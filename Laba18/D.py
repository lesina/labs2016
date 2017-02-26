def makeGraph(size, n):
    adjacency_list = []
    for i in range(size):
        adjacency_list.append([])
    for i in range(n):
        num, vertex = list(map(int, input().split()))
        adjacency_list[num].append(vertex)
        adjacency_list[vertex].append(num)
    return adjacency_list


def dfs(vertex):
    visitedEdges[vertex] = True
    for i in adjacency_list[vertex]:
        if not visitedEdges[i]:
#            if ((vertex + 1), i) not in DFS and (i, (vertex + 1)) not in DFS:
#                DFS.append((vertex + 1, i))
            dfs(i)


size = int(input())
n = int(input())
visitedEdges = [False]*size
adjacency_list = makeGraph(size, n)
for vertex in range(len(adjacency_list)):
    if len(adjacency_list[vertex]):
        dfs(vertex)
        break
if False in visitedEdges:
    print("NO")
else:
    print("YES")