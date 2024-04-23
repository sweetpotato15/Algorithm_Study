import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(num), num))