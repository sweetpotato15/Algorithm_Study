import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n,m,start = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes.sort(reverse = True)

def dfs(graph, visited, v):
    visited[v] = True
    answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

visited = [False] * (n+1)
answer = []

dfs(graph, visited, start)

result = [0] * (n+1)

for i in range(len(answer)):
    result[answer[i]] = i+1

for i in result[1:]:
    print(i)