def queensproblem(rows, columns):
    solutions = [[]]
    for row in range(rows):
        solutions = add_one_queen(row, columns, solutions)
    return solutions

def add_one_queen(new_row, columns, prev_solutions):
    return [solution + [new_column]
            for solution in prev_solutions
            for new_column in range(columns)
            if no_conflict(new_row, new_column, solution)]

def no_conflict(new_row, new_column, solution):
    return all(solution[row]       != new_column           and
               solution[row] + row != new_column + new_row and
               solution[row] - row != new_column - new_row
               for row in range(new_row))

arr = []
for i in range(8):
    arr.append(tuple(map(int, input().split(" "))))
sol = [0]*8

for dot in arr:
    sol[dot[1]-1] = dot[0]-1

solutions = []
for solution in queensproblem(8, 8):
    solutions.append(solution)

if sol in solutions:
    print("NO")
else:
    print("YES")
