import sys
input = sys.stdin.readline
from collections import deque

def move_people(graph, x, y, visited):
    global flag
    q = deque([(x, y)])
    move_lst = deque([(x, y)])
    sum_value = graph[x][y]
    num = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and L<=abs(graph[x][y]-graph[nx][ny])<=R and not visited[nx][ny]:
                move_lst.append((nx, ny))
                sum_value += graph[nx][ny]
                q.append((nx, ny))
                visited[nx][ny] = True
                num += 1

    if num > 1:
        flag = True

    # 인구 이동
    new_value = sum_value // num
    while move_lst:
        x, y = move_lst.pop()
        graph[x][y] = new_value
    
    return graph, visited, flag

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    visited = [[False]*N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                A, visited, flag = move_people(A, i, j, visited)
                
    if not flag:
        print(ans)
        break
    ans += 1
