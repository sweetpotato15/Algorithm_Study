import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

from collections import deque, defaultdict

q = deque([(S, 0)])
max_answer = 0
flag = False
dict = defaultdict(list)

while q:
    vol, ind = q.popleft()
    if vol in dict[ind]:
        continue
    dict[ind].append(vol)

    if ind == N:
        flag = True
        max_answer = max(max_answer, vol)
    else:
        if 0<=vol+V[ind]<=M:
            q.append((vol+V[ind], ind+1))
        if 0<=vol-V[ind]<=M:
            q.append((vol-V[ind], ind+1))

if flag:
    print(max_answer)
else:
    print(-1)
