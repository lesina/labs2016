def looksay(look):
    look = str(look)
    prev, count, say = look[0], 1, ''
    for char in look[1:]:
        if char == prev:
            count += 1
            continue
        say += str(count) + prev
        prev = char
        count = 1
    return say + str(count) + prev

arr = [1]
k = int(input())
for i in range(k-1):
    arr.append(looksay(arr[i]))
print(arr[-1])
