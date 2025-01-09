import sys
input = sys.stdin.readline
import heapq
sys.setrecursionlimit(int(1e9))

INF = int(1e6)
N, M = map(int, input().split())

answer = [[INF]*(M) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
graph = []
sx, sy = 0, 0

for i in range(N):
    command = list(map(int, input().split()))
    for j in range(M):
        if command[j] == 0:
            answer[i][j] = 0
        elif command[j] == 2:
            sx, sy = i, j
    graph.append(command)

q = [(0, sx, sy)] # (dist, x, y)
answer[sx][sy] = 0
while q:
    dist, x, y = heapq.heappop(q)

    if not visited[x][y]:
        visited[x][y] = True
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] == 1:
                answer[nx][ny] = min(answer[nx][ny], dist+1)
                q.append((dist+1, nx, ny))

for i in range(N):
    for j in range(M):
        if answer[i][j] == INF:
            print(-1, end=" ")
        else:
            print(answer[i][j], end=" ")
    print()