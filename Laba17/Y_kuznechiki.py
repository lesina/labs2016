numberOfGrasshoppes = int(input())
grasshoppers = list(map(int, input().split()))
time = int(input())

for i in range(time):
    place = numberOfGrasshoppes - grasshoppers[-1] -1
    grasshoppers = grasshoppers[:place] + [grasshoppers[-1]] + grasshoppers[place:-1]
print(*grasshoppers)