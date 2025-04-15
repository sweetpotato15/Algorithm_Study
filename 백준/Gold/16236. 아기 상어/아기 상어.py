import sys
input = sys.stdin.readline
from collections import deque

def next_shark(start, shark_size, pos_size):
    # 다음 상어의 도착지 
    visited = [[False]*N for _ in range(N)]
    q = deque([(start[0], start[1], 0)]) # (x, y, dist)
    answer = []
    first = True

    while q:
        x, y, d = q.popleft()
        visited[x][y] = True
        
        if graph[x][y] in pos_size: # 도착지가 가능한 경우 (나보다 작은 물고기)
            answer.append((d, x, y))
            
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] <= shark_size:
                q.append((nx, ny, d+1))
                visited[nx][ny] = True

    answer.sort()
    if answer:
        return answer[0]     
    else:
        return 0



N = int(input())
graph = []
for i in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)
    if 9 in lst:
        x = i
        y = lst.index(9)
        graph[x][y] = 0

# x, y : 아기 상어 위치 / nx, ny : 다음 물고기 위치 

answer_time = 0
now_eat = 0
pos_size = [1]
shark_size = 2

while True:
    command = next_shark((x, y), shark_size, pos_size)
    if command == 0:
        print(answer_time)
        break


    # 물고기 먹는 과정
    dist, x, y = command
    now_eat += 1
    answer_time += dist
    graph[x][y] = 0

    if now_eat == shark_size: # 크기가 커질 경우
        now_eat = 0
        pos_size.append(shark_size)
        shark_size += 1