import sys
input = sys.stdin.readline

# graph, visited, q
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().strip()))
visited = [[False] * m for _ in range(n)]

from collections import deque
def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = True
                graph[nx][ny] += graph[x][y]
bfs(0,0)
print(graph[-1][-1])