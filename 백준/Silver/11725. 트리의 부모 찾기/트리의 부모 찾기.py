import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(graph, v, visited):
    global answer
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            answer[i] = v
            dfs(graph, i, visited)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = list(range(N+1))
visited = [False] * (N+1)
dfs(graph, 1, visited)
print(*answer[2:], sep = '\n')