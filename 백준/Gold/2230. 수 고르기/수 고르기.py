import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = [int(input()) for _ in range(N)]
number = sorted(number)

answer = 2 * 1e9
start, end = 0,0
while start <= end < N:
    value = number[end] - number[start]
    if value < M:
        end += 1
    else:
        answer = min(answer, value)
        start += 1

print(answer)