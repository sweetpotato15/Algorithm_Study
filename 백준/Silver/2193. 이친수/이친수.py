N = int(input())

array = [0]*91
array[1] = 1
array[2] = 1
array[3] = 2
for i in range(4, 91):
    array[i] = sum(array[:i-1]) + 1
print(array[N])