import sys
input = sys.stdin.readline

def dfs(x, y, count, total):
    global max_value
    if count == 4:
        max_value = max(max_value, total)
        return 
    for (i, j) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = x+i, y+j
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count+1, total+graph[nx][ny])
            visited[nx][ny] = False

def block(x, y):
    global max_value
    value = graph[x][y]
    block = 0
    for (i, j) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = x+i, y+j
        if 0<=nx<N and 0<=ny<M:
            block += 1
            value += graph[nx][ny]
    
    if block == 3:
        max_value = max(max_value, value)
    
    if block == 4:
        for (i, j) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x+i, y+j
            value -= graph[nx][ny]
            max_value = max(max_value, value)
            value += graph[nx][ny]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_value = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, 0)
        block(i, j)
        visited[i][j] = False

print(max_value)