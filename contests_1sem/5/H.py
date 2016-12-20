N, A, B, C, D = list(map(int,input().split(" ")))
array = [i+1 for i in range(N)]
array[A-1:B] = array[B-1:A-2:-1]
array[C-1:D] = array[D-1:C-2:-1]
print(*array, sep = " ")
