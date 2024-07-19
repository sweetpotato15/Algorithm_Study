import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited, n):
    global answer
    if n == 5:
        answer = 1
        return 
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited, n+1)
            visited[i] = False

answer = 0
for i in range(N):
    visited = [False] * N
    dfs(i, visited,1)
    if answer == 1:
        print(1)
        exit()
print(0)