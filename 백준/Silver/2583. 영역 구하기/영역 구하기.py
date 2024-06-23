import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1,y2):
            graph[i][j] = 1
visited = [[False]*M for _ in range(N)]
answer = []

def bfs(x,y):
    count = 1
    q = deque([[x,y]])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx = cx + dx
            ny = cy + dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] == 0:
                count += 1
                q.append([nx,ny])
                visited[nx][ny] = True
    return count

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 0:
            c = bfs(i,j)
            answer.append(c)
print(len(answer))
print(*sorted(answer))