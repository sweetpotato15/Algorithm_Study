from collections import deque

N, K = map(int, input().split())
INF = int(1e6)
visited = [False]*(int(1e6))
q = deque([(0, N)]) # (시간, 위치)
visited[N] = True

while q:
    sec, pos = q.popleft()
    if pos == K:
        print(sec)
        break
    for x in [pos-1, pos+1, pos*2]:
        if 0<=x<=100000 and not visited[x]:
            q.append([sec+1, x])
            visited[x] = True