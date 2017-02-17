def newTable():
    table = []
    for i in range(8):
        table.append([0]*8)

    for i in range(8):
        x, y = list(map(int, input().split()))
        table[x-1][y-1] = 1
    return table

def check(table):
    answer = "NO"
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                if not checkThisOne(table, i, j):
                    answer = "YES"
    return answer

def checkThisOne(table, x, y):
    #res = True
    if table[x].count(1) > 1:
        return False
    if list(map(list, zip(*table)))[y].count(1) > 1:
        return False
    i = 1
    while x - i >= 0 and y - i >= 0:
        if table[x-i][y-i] == 1:
            return False
        else:
            i += 1
    i = 1
    while x + i <= 7 and y + i <= 7:
        if table[x + i][y + i] == 1:
            return False
        else:
            i += 1
    i = 1
    while x - i >= 0 and y + i <= 7:
        if table[x - i][y + i] == 1:
            return False
        else:
            i += 1
    i = 1
    while x + i <= 7 and y - i >= 0:
        if table[x + i][y - i] == 1:
            return False
        else:
            i += 1
    return True

table = newTable()
print(check(table))
#for i in range(8):
#    print(*table[i])