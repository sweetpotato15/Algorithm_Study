import sys
input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split())
'''
총 F층 / G층 가야함 / 현재 S층 / 위로 U층씩 / 아래로 D층씩
'''

visited = [False]*(F+1)
flag = False

def bfs():
    q = deque([(S, 0)])
    visited[S] = True

    while q:
        floor, cnt = q.popleft()
        if floor == G:
            print(cnt)
            return 
        
        if floor+U <= F and not visited[floor+U]:
            q.append((floor+U, cnt+1))
            visited[floor+U] = True
        
        if floor-D >= 1 and not visited[floor-D]:
            q.append((floor-D, cnt+1))
            visited[floor-D] = True
        
    print('use the stairs')
    return 

bfs()