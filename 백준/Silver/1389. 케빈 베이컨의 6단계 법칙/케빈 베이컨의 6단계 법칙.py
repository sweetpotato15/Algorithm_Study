import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1000
graph = [[0]+[INF]*(N) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜 : i~j = i~k + k~j
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            value = min(graph[i][j], graph[i][k]+graph[k][j])
            graph[i][j] = value
            graph[j][i] = value

answer = [(i, sum(graph[i])) for i in range(N+1)]
answer = sorted(answer, key=lambda x:(x[1], x[0]))
print(answer[0][0])