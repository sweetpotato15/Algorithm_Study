import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int, input().split())
number = list(map(int, input().split()))

answer = 0
dp = [0] * (max(number) + 1)
stack = deque()

for i in range(n):
    answer = max(answer, len(stack))
    stack.append(number[i])
    dp[number[i]] += 1
    if dp[number[i]] > k : 
        while True:
            now = stack.popleft()
            dp[now] -= 1
            if now == number[i]:
                break
    answer = max(answer, len(stack))
print(answer)