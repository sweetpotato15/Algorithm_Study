import sys
input = sys.stdin.readline

def dfs(x, y, count, total):
    global sum_value
    if sum_value >= total + (3-count)*max_value: # 나머지가 다 최대라도 이미 최댓값보다 작은경우 
        return 
    if count == 3:
        sum_value = max(sum_value, total)
        return 
    
    for (i, j) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx, ny = x+i, y+j
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            if count == 1: # 2개 연결됐을 때
                visited[nx][ny] = True
                dfs(x, y, count+1, total+graph[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, count+1, total+graph[nx][ny])
            visited[nx][ny] = False

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
sum_value = 0
max_value = max(map(max, graph))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = False

print(sum_value)