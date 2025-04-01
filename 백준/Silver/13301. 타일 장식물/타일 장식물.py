N = int(input())
array = [1, 1] + [0]*N

for i in range(2, N+2):
    array[i] = array[i-1] + array[i-2]

if N == 1:
    print(4)
else:
    answer = array[N-1]*4 + array[N-2]*2
    print(answer)