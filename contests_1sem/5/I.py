from math import sqrt

def dist(vec1, vec2):
    return sqrt( (vec1[0]-vec2[0])**2 + (vec1[1]-vec2[1])**2 )

N = int(input())
arr = []
for i in range(N):
    arr.append(tuple(map(int, input().split(" "))))
MAX = 0
for i in range(N):
    for j in range(i+1, N):
        if dist(arr[i], arr[j]) > MAX:
            MAX = dist(arr[i], arr[j])
print(MAX)
