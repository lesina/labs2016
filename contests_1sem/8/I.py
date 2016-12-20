n = int(input())
students = []
for i in range(n):
    students.append(tuple(map(float, input().split())))
students.sort(key = lambda x: (x[1], -x[0]))
for student in students:
    print("%.2f %.3f" % student)
