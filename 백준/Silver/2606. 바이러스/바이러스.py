import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
start = 1

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(graph, visited, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)
dfs(graph, visited, start)

num = 0

for n in visited:
    if n == True:
        num += 1

print(num-1)