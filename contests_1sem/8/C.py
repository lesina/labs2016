n = int(input())
answer = 0
array = list(map(int, input().split()))
check_array = [i for i in array]
for i in range(len(array)-1):
    if not check_array[i]:
        check_array[i+1] -= 1
        check_array[i+1] = abs(check_array[i+1])
if check_array[-1] == 1:
    answer = check_array
check_array = [i for i in array]
check_array[0] = abs(check_array[0]-1)
for i in range(len(array)-1):
    if not check_array[i]:
        check_array[i+1] -= 1
        check_array[i+1] = abs(check_array[i+1])
if check_array[-1] == 0 and answer == 0:
    answer = check_array
else:
    answer = min(answer.count(1), check_array.count(1))
print(answer)
