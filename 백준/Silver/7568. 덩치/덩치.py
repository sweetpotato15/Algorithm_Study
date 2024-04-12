import sys
input = sys.stdin.readline

n = int(input())
total_list = [list(map(int, input().split())) for _ in range(n)]

answer = [1] * n
for i in range(n):
    for j in range(n):
        if total_list[i][0] < total_list[j][0] and total_list[i][1] < total_list[j][1]:
            answer[i] += 1
print(*answer)