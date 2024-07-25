import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    global graph
    while q:
        cx, cy = q.popleft()
        for dx, dy in [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,2),(1,-2),(2,-1),(2,1)]:
            nx = cx + dx
            ny = cy + dy
            if nx == end_x and ny == end_y:
                graph[nx][ny] = graph[cx][cy] + 1
                return 
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[cx][cy] + 1
                q.append((nx,ny))
            

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    q = deque()
    q.append((start_x, start_y))

    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        bfs()
        print(graph[end_x][end_y])
