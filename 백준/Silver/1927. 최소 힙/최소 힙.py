import sys
input = sys.stdin.readline
import heapq

n = int(input())
numbers = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, x)