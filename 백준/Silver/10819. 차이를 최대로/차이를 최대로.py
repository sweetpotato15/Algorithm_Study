from itertools import permutations

N = int(input())
array = list(map(int, input().split()))
answer = 0

for i in permutations(range(N), N):
    count = 0
    for j in range(N-1):
        count += abs(array[i[j]] - array[i[j+1]])
    if answer < count:
        answer = count

print(answer)