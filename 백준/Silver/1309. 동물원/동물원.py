N = int(input())

array = [0]*(N+1)
array[0] = 3
array[1] = 7

if N ==1 or N==2: 
    print(array[N-1])
else:
    for i in range(2, N):
        array[i] = (array[i-1]*2 + array[i-2]) % 9901

    print(array[N-1])