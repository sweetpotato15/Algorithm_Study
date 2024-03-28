m = int(input())
n = int(input())

answer = []
for num in range(m, n+1):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        answer.append(num)

if len(answer) >= 1:
    print(sum(answer))
    print(min(answer))

else:
    print(-1)
