a = int(input())
b = int(input())
if (a > b):
        max1 = a
        max2 = b
else:
        max2 = a
        max1 = b
a = int(input())
while (a != 0):
        if (a > max1):
                max2 = max1
                max1 = a
        elif (a > max2):
                max2 = a
        a = int(input())
print(max2)
