import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
water = deque(sorted(list(map(int, input().split()))))

ans = 0
while water:
    x = water.popleft()
    ans += 1
    while water and x+L-1 >= water[0]:
        
        water.popleft(),'popleft'

print(ans)