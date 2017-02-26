def makeGraph(size, n):
    adjacency_list = []
    GOVNOKOD = []
    for i in range(size):
        adjacency_list.append([])
        GOVNOKOD.append([])
    for i in range(n):
        num, vertex = list(map(int, input().split()))
        adjacency_list[num].append(vertex)
        GOVNOKOD[num].append(vertex)
        GOVNOKOD[vertex].append(num)
    return adjacency_list, GOVNOKOD


def makeGraph2(size, n, pairs):
    adjacency_list = []
    for i in range(size):
        adjacency_list.append([])
    for i in pairs:
        num, vertex = i[0], i[1]
        adjacency_list[num].append(vertex)
    return adjacency_list


def dfs(vertex):
    visitedEdges[vertex] = True
    for i in adjacency_list[vertex]:
        if not visitedEdges[i]:
#            if ((vertex + 1), i) not in DFS and (i, (vertex + 1)) not in DFS:
#                DFS.append((vertex + 1, i))
            dfs(i)


def dfs2(vertex):
    visitedEdges[vertex] = True
    for i in NOG_adjacency_list[vertex]:
        if not visitedEdges[i]:
#            if ((vertex + 1), i) not in DFS and (i, (vertex + 1)) not in DFS:
#                DFS.append((vertex + 1, i))
            dfs2(i)


def dfs3(vertex):
    visitedEdges[vertex] = True
    for i in GOVNOKOD[vertex]:
        if not visitedEdges[i]:
#            if ((vertex + 1), i) not in DFS and (i, (vertex + 1)) not in DFS:
#                DFS.append((vertex + 1, i))
            dfs3(i)


def bfs2(vertex):
	visitedEdges[vertex] = True
	for i in NOG_adjacency_list[vertex]:
		if not visitedEdges[i] and i not in queue:
			queue.append(i)
	while queue:
		bfs2(queue.pop(0))


def bfs3(vertex):
	visitedEdges[vertex] = True
	for i in GOVNOKOD[vertex]:
		if not visitedEdges[i] and i not in queue:
			queue.append(i)
	while queue:
		bfs3(queue.pop(0))


def bfs(vertex):
	visitedEdges[vertex] = True
	for i in adjacency_list[vertex]:
		if not visitedEdges[i] and i not in queue:
			queue.append(i)
	while queue:
		bfs(queue.pop(0))


size = int(input())
n = int(input())
adjacency_list, GOVNOKOD = makeGraph(size, n)
pairs = []
for vertex in range(len(adjacency_list)):
    visitedEdges = [False] * size
    queue = []
    bfs(vertex)
    midVisitedEdges = visitedEdges
    for vert in range(len(midVisitedEdges)):
        visitedEdges = [False] * size
        queue = []
        if midVisitedEdges[vert]:
            dfs(vert)
        if visitedEdges[vertex] and vertex!=vert:
            pairs.append((vertex, vert))

span_count1 = 0
visitedEdges = [False] * size
queue = []
while False in visitedEdges:
    span_count1 += 1
    bfs3(visitedEdges.index(False))

NOG_adjacency_list = makeGraph2(size, n, pairs)
span_count2 = 0
visitedEdges = [False] * size
queue = []
while False in visitedEdges:
    span_count2 += 1
    bfs2(visitedEdges.index(False))

print(span_count1, span_count2)