import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp = [graph[0]] + [[0] * 3 for _ in range(n-1)]
for i in range(1, n):
    for j in range(3):
        if j == 0: left, right = 1,2
        elif j == 1: left, right = -1,1
        else: left, right = -2,-1
        dp[i][j] = min(dp[i-1][j+left], dp[i-1][j+right]) + graph[i][j]
print(min(dp[-1]))