N = int(input())
arr = list(map(int, input().split(" ")))
MIN = max(arr) - min(arr)
indexs = sorted([arr.index(max(arr)), arr.index(min(arr))])
for i in range(N):
    for j in range(i+1, N):
        if abs(arr[j]-arr[i]) < MIN:
            indexs[0] = i
            indexs[1] = j
            MIN = abs(arr[j]-arr[i])
print(indexs[0], indexs[1])
