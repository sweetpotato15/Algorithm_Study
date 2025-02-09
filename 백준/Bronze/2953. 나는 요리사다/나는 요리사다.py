answer = []
for i in range(5):
    answer.append([i+1, sum(list(map(int, input().split())))])
answer = sorted(answer, key=lambda x : x[1], reverse = True)
print(*answer[0])