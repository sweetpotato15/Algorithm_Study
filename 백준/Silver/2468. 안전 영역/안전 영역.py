import sys
input = sys.stdin.readline
from collections import deque

def rain_height(graph, h):
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= h:
                graph[i][j] = 0
    return graph

def bfs(x, y):
    global visited
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N and new_graph[nx][ny]!= 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_count = 1
max_height = 0
for i in graph:
    max_height = max(max_height, max(i))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for height in range(1, max_height):
    new_graph = rain_height(graph, height)
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if new_graph[i][j] != 0 and not visited[i][j]:
                
                bfs(i, j)
                count += 1
    max_count = max(max_count, count)
print(max_count)