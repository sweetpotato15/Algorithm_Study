import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
for _ in range(N):
    command = int(input())
    if command == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -command)