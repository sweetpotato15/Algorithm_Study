import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque(list(range(1,n+1)))
while q :
    if len(q) == 1:
        print(*q)
        break
    q.popleft()
    now = q.popleft()
    q.append(now)
