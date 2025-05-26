# 내리막길 1520
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

M, N = map(int, input().split()) # 세로:M, 가로:N
graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]
dp[0][0] = 1

def dfs(x, y):
    if dp[x][y] == -1: # 아직 계산 안 된 경우 (첫 방문)
        # 네 방향 (높은 곳에서 낮은 곳 방문시 경로수 누적) -> 마지막 좌표에서 거꾸로 올라가는 식 
        dp[x][y] = 0
        for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x+i, y+j
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] > graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(M-1, N-1))