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
dfs(0)
fuck_yeah = False
for vertex in adjacency_list:
    if len(vertex)%2:
        fuck_yeah = True
        break
if False in visitedEdges or fuck_yeah:
    print("NO")
else:
    print("YES")