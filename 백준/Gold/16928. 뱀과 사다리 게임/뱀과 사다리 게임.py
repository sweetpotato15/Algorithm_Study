import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
stairs, snakes = {}, {}
for _ in range(N):
    a, b = map(int, input().split())
    stairs[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

visited = [False]*101
cnt = [0]*101

q = deque([1]) #위치

while q:
    x = q.popleft()
    if x == 100: # 100번에 도착
        print(cnt[x])
        break

    for dice in range(1, 7):
        nx = x+dice
        if nx <= 100 and not visited[nx]: # 갈 수 있고, 아직 방문하지 않았다면면
            # 사다리가 있다면
            if nx in stairs.keys():
                nx = stairs[nx]
            # 뱀이 있다면 
            elif nx in snakes.keys():
                nx = snakes[nx]
            # 최종 변화된 nx가(사다리 올라가거나 뱀 내려온) 아무것도 없다면 
            if not visited[nx]:
                visited[nx] = True
                cnt[nx] = cnt[x] + 1
                q.append(nx)