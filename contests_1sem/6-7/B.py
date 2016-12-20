from math import sqrt

def distance(a, b, c, d):
    return sqrt((c-a)**2 + (d-b)**2)

A = []
while len(A) != 4:
    A += list(map(float, input().split()))
print(distance(A[0], A[1], A[2], A[3]))
