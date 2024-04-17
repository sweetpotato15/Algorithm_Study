import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    q = list(map(int, input().split()))
    index = [i for i in range(n)]
    count = 0
    while m in index:
        while max(q) != q[0]:
            q.append(q.pop(0))
            index.append(index.pop(0))
        q.pop(0)
        index.pop(0)
        count += 1
    print(count)   