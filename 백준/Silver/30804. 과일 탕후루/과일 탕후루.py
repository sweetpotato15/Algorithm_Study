N = int(input())
array = list(map(int, input().split()))
answer = 1

start, end = 0, 0
count = [0]*10
count[array[0]] += 1
temp = [0]*10
temp[array[0]] = 1
kind = sum(temp)

while True:
    kind = sum(temp)
    if kind <= 2:
        answer = max(answer, sum(count))
        end += 1
        if end == N:
            break
        count[array[end]] += 1
        temp[array[end]] = 1

    else:
        count[array[start]] -= 1
        if count[array[start]] == 0:
            temp[array[start]] = 0
        start += 1

print(answer)