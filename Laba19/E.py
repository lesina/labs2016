# def makeGraph(size, n):
#     adjacency_list = []
#     for i in range(size):
#         adjacency_list.append([])
#     for i in range(n):
#         num, vertex = list(map(int, input().split()))
#         adjacency_list[num].append(vertex)
#     return adjacency_list
#
#
# def bfs(vertex, start=0):
#     visitedEdges[vertex] = True
#     for i in adjacency_list[vertex]:
#         if not visitedEdges[i] and i not in queue:
#             queue.append(i)
#             if (vertex, i) not in BFS and (queue[0], i) not in BFS:
#                 BFS.append((vertex, i))
#         if visitedEdges[i]:
#             BFS.append((vertex, i))
#             cycles.append(BFS)
#             while queue:
#                 queue.pop()
#     while queue:
#         bfs(queue.pop(0), start)
#
#
# def makeCycle(index):
#     result = cycles[index]
#     end = result[-1]
#     for i in range(len(result)):
#
#
#
# size, n = list(map(int, input().split()))
# adjacency_list = makeGraph(size, n)
# cycles = []
# for i in range(size):
#     visitedEdges = [False] * size
#     cycle = False
#     BFS = []
#     queue = []
#     bfs(i, i)
# if not cycles:
#     print("NO CYCLES")
# else:
#     for i in range(len(cycles)):
#         makeCycle(i)
"""

Что может быть лучше кода, написанного в состоянии аффекта в 3 часа ночи?
Это убивает меня!!!
Пожалуйста, если вы читаете это сейчас, значит вы катаете этот код, или вы Лариса.
Тогда попрошу поставить звёздочку этому репозиторию: https://github.com/lesina/labs2016
Мне важно знать, что мой труд кому-то нужен. Так же буду рад помощи в улучшении этого кода.
P.S. Даже не пытайся понять, что тут написано, мой юный читатель...

"""


def bfs(Graph, start=0, Path=[], Paths=[]):
    D = [None] * size
    D[start] = 0
    Q = [start]
    Qstart = 0
    while Qstart < len(Q):
        u = Q[Qstart]
        Path.append(u)
        Qstart += 1
        for v in Graph[u]:
            if D[v] is None:
                D[v] = D[u] + 1
                Q.append(v)
            if v == start and len(Path) > 2:
                Paths.append(list(Path))
        Path.pop()
    return Paths
#
# def trololo(Graph, Begin, Current, Path = [], Paths = []):
#     Path.append(Current)
#     for ihavenoideahowtonamethisshit in Graph[Current]:
#         if ihavenoideahowtonamethisshit == Begin and len(Path) > 2:
#             Paths.append(list(Path))
#         if ihavenoideahowtonamethisshit not in Path:
#             Paths = trololo(Graph, Begin, ihavenoideahowtonamethisshit, Path, Paths)
#     Path.pop()
#     return Paths


def makeGraph(size, n):
    adjacency_list = dict()
    for i in range(size):
        adjacency_list[i] = []
    for i in range(n):
        num, vertex = list(map(int, input().split()))
        adjacency_list[num].append(vertex)
    return adjacency_list


size, n = list(map(int, input().split()))
lil = makeGraph(size, n)
cycles = []
for i in range(size):
    for j in bfs(lil, i):
        cycles.append(j)
print(cycles)
if cycles:
    min_len = min(list(map(len, cycles)))
    for cycle in cycles:
        if len(cycle) == min_len:
            answer = cycle
            break
    print(*answer)
else:
    print("NO CYCLES")