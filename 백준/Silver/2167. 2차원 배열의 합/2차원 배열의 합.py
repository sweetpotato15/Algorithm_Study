# 2차원 배열의 합 2167

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

graph_sum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        graph_sum[i][j] = graph_sum[i-1][j] + graph_sum[i][j-1] - graph_sum[i-1][j-1] + graph[i][j]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split()) # (i,j) ~ (x,y) 합 / i행 j열
    answer = graph_sum[x][y] - graph_sum[x][j-1] - graph_sum[i-1][y] + graph_sum[i-1][j-1]
    print(answer)
