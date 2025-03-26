import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global count
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if graph[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            for i in range(8):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<H and 0<=ny<W and not visited[nx][ny]:
                    q.append((nx, ny))
    count += 1

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    count = 0

    dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
    if map(min, graph) == 1:
        print(1)
    elif map(max, graph) == 0:
        print(0)
    else:
        for i in range(H):
            for j in range(W):
                if graph[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
        print(count)

    