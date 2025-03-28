import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] 
original_move = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 방향 : 3, 2, 1, 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 벽 : 1, 청소 안됨 : 0, 청소 됨 : 2

def process():
    global d
    q = deque([(r, c, d)])
    cnt = 0

    while q:
        x, y, d = q.popleft()

        # 1. 현재 칸이 청소되지 않은 경우
        if graph[x][y] == 0:
            graph[x][y] = 2
            cnt += 1
        
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 (다 청소 됨 or 벽)
        if graph[x-1][y]!=0 and graph[x+1][y]!=0 and graph[x][y-1]!=0 and graph[x][y+1]!=0:
            if d == 0:
                if graph[x+1][y] == 2:
                    q.append((x+1, y, d))
                else:
                    return cnt
            elif d == 1:
                if graph[x][y-1] == 2:
                    q.append((x, y-1, d))
                else:
                    return cnt
            elif d == 2:
                if graph[x-1][y] == 2:
                    q.append((x-1, y, d))
                else:
                    return cnt
            else:
                if graph[x][y+1] == 2:
                    q.append((x, y+1, d))
                else:
                    return cnt
        
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        else:
            move_direction = original_move[:]
            for _ in range(d):
                move_direction.insert(0, move_direction.pop())
            for i in range(4):
                nx, ny = x+move_direction[i][0], y+move_direction[i][1]
                if graph[nx][ny] == 0:
                    if sum(move_direction[i]) == 1:
                        if move_direction[i][0] == 0: # (0, 1)
                            q.append((nx, ny, 1))
                        else: # (1, 0)
                            q.append((nx, ny, 2))
                    else:
                        if move_direction[i][0] == 0: # (0, -1)
                            q.append((nx, ny, 3))
                        else: # (-1, 0)
                            q.append((nx, ny, 0))
                    break

answer = process()
print(answer)