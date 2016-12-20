N = int(input())
array = list(map(int, input().strip().split()))
oddArray = [x for x in array if x%2 == 1]
evenArray = [x for x in array if x%2 == 0]
if oddArray and evenArray:
    maxOdd = max(oddArray)
    minEven = min(evenArray)
    i1 = array.index(maxOdd)
    i2 = array.index(minEven)
    array[i1], array[i2] = array[i2], array[i1]
print(*array)
