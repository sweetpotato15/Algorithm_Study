import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N,H = map(int, input().split())
up, down = [], []
total = [-int(input()) for _ in range(N)]
down = sorted(total[0::2])
up = sorted(total[1::2])

answer = [0] * (H+1)
for h in range(1, H+1):
    answer[h] += bisect_right(down, -h)
    answer[-h] += bisect_right(up, -h)
count = min(answer[1:])
print(count, answer[1:].count(count))