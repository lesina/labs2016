a, b = input().split()
a = '0x' + a
b = '0x' + b
res = int(a, 16) ^ int(b, 16)
print(hex(res)[2:])
