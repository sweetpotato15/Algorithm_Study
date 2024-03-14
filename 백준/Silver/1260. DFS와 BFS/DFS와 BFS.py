def dfs(graph, v, visited_dfs): # 재귀함수 FILO 
    visited_dfs[v] = True
    print(v , end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

from collections import deque

def bfs(graph, start, visited_bfs): # 큐 FIFO
    visited_bfs[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)] # index i 번째 정점에 연결되어있는 정점 번호 

for _ in range(m):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for nodes in graph: # 정점이 여러개인경우 작은 번호부터 
    nodes.sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(graph,v,visited_dfs )
print()
bfs(graph, v, visited_bfs)