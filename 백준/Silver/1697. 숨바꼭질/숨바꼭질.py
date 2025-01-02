from collections import deque

N, K = map(int, input().split())
INF = int(1e6)
array = [INF]*(int(1e6))
visited = [False]*(int(1e6))
q = deque([[0, N]]) # (시간, 위치)
array[N] = 0

while q:
    sec, pos = q.popleft()
    if pos == K:
        print(sec)
        break
    if not visited[pos]:
        visited[pos] = True
        for x in [pos-1, pos+1, pos*2]:
            if not visited[x] and 0<=x<=100000:
                q.append([sec+1, x])
                array[x] = min(array[x], sec+1)