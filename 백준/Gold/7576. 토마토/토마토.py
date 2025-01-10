import sys
input = sys.stdin.readline
import heapq

M, N = map(int, input().split())
tomato = []
q = []
for i in range(N):
    command = list(map(int, input().split()))
    for j in range(M):
        if command[j] == 1:
            heapq.heappush(q, (1, i, j))
    tomato.append(command)

while q:
    day, x, y = heapq.heappop(q)
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = day+1
                heapq.heappush(q, (day+1, nx, ny))

max_day = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] > max_day:
            max_day = tomato[i][j]
        elif tomato[i][j] == 0:
            print(-1)
            exit()
print(max_day-1)