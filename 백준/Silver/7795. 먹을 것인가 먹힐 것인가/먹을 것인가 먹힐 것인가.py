import sys
input = sys.stdin.readline
from bisect import bisect_left

T = int(input())
for _ in range(T):
    answer = 0
    start = 0
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    for i in range(N):
        while start < M:
            if A[i] <= B[start]:
                answer += start
                break
            else:
                start += 1
        if start == M:
            answer += start
    print(answer)