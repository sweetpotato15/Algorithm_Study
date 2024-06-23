import sys
input = sys.stdin.readline

N,M = map(int, input().split())
miro = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

from collections import deque

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    
    while q:
        now = q.popleft()
        cx = now[0]
        cy = now[1]
        
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx=cx+dx
            ny=cy+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and miro[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = True
                miro[nx][ny] += miro[cx][cy]

bfs(0,0)
print(miro[-1][-1])