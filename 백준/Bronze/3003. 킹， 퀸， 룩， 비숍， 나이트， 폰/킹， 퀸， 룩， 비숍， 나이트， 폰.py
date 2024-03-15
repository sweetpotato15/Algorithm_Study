x = list(map(int, input().split()))
answer = [1,1,2,2,2,8]

result = []
for i in range(6):
    result.append(answer[i]-x[i])

for ans in result:
    print(ans, end=' ')