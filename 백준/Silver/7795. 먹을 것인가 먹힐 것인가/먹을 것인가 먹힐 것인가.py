import sys
input = sys.stdin.readline
from bisect import bisect_left

T = int(input())
for _ in range(T):
    answer = 0
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    for a in A:
        answer += bisect_left(B, a)
    print(answer)