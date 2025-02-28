import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)] # [i][j] 까지의 최대 사탕 개수

row = graph[0]
col = [x[0] for x in graph]
for i in range(1, M):
    row[i] += row[i-1]
for i in range(1, N):
    col[i] += col[i-1]

dp[0] = row
for i in range(N):
    dp[i][0] = col[i]
dp = [[0]*(M+2)] + [[0]+i+[0] for i in dp] + [[0]*(M+2)]
for i in range(2, N+1):
    for j in range(2, M+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + graph[i-1][j-1]
print(dp[-2][-2])