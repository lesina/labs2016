pages = int(input())
if pages == 1:
    answer = 1
elif pages == 2:
    answer = 2
else:
    days = [1, 1]
    index = 2
    while sum(days) < pages:
        days.append(days[index-1] + days[index-2])
        index += 1
    answer = index
print(answer)
