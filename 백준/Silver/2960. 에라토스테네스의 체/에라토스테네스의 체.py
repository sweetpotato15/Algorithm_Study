N, K = map(int, input().split())

array = list(range(N+1))
answer = []
count = 0
for i in range(2, N+1):
    if array[i] == 0:
        continue
    for j in range(1, int(N//i)+1):
        if array[i*j] == 0:
            continue
        count += 1
        array[i*j] = 0
        if count == K:
            print(i*j)
            exit()
print(N)