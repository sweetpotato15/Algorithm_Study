import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수 
graph = [[0]*N for _ in range(N)] # 0:없음, 1:사과
for _ in range(K):
    row, col = map(int, input().split())
    graph[row-1][col-1] = 1

dir_dic = {'U' : (-1, 0), # 위
            'D' : (0, 1), # 오른 
            'S' : (1, 0), # 아래
            'L' : (0, -1)}  # 왼
dir_lst = ['U', 'D', 'S', 'L', 'U', 'D', 'S', 'L']

direction = {} # D:오른쪽, L:왼쪽
L = int(input())
for _ in range(L):
    a, b = input().split()
    direction[int(a)] = b

snake = deque([(0, 0, 'D')]) # (x, y, 방향) / 꼬리 ~ 머리 순
now_time = 0

while True:
    now_time += 1
    x, y, d = snake[-1]

    nx, ny = x + dir_dic[d][0] , y + dir_dic[d][1]

    # 1) 벽이나 자기자신의 몸과 부딪히는 경우
    if (not (0<=nx<N and 0<=ny<N)) or any(x==nx and y==ny for (x, y, _) in snake):
        print(now_time)
        break 
    
    # 2) 몸 길이 늘리기 (머리 길이)
    snake.append((nx, ny, d))

    # 3) 이동한 칸에 사과가 있는 경우 -> 그대로
    # 4) 이동한 칸에 사과가 없는 경우 -> 꼬리 제거 
    if graph[nx][ny] == 0:
        snake.popleft()
    else:
        graph[nx][ny] = 0

    # 5) n초 후, 방향 전환
    if now_time in direction.keys():
        x, y, d = snake.pop()
        nd = direction[now_time]

        d_index = dir_lst.index(d)
        if nd == 'D': # 시계 방향으로 90도 (머리만)
            snake.append((x, y, dir_lst[d_index+1]))
        else: # 반시계 방향으로 90도 (머리만)
            snake.append((x, y, dir_lst[d_index-1]))