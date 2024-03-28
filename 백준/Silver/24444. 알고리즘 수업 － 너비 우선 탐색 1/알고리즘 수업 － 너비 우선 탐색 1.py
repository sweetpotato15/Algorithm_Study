import sys
input = sys.stdin.readline
from collections import deque
n,m,start = map(int, input().split())
graph =[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes.sort()

visited = [False] * (n+1)
answer = []

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    answer.append(start)

    while queue:
        v = queue.popleft()
        for node in graph[v] :
            if not visited[node]:
                visited[node] =True
                queue.append(node)
                answer.append(node)

result = [0]*(n+1)
bfs(graph, visited, start)

for i in range(len(answer)):
    result[answer[i]] = i+1

for ans in result[1:]:
    print(ans)
