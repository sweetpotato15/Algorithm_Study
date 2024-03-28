n = int(input())
number = list(map(int, input().split()))

answer = 0
for num in number:
    count = 0
    for i in range(1,num):
        if num % i == 0:
            count += 1
    if count == 1:
        answer += 1

print(answer)