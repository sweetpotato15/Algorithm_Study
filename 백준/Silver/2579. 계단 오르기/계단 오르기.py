import sys
input = sys.stdin.readline

n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)
dp[1] = stair[1]

if n > 1:
    dp[2] = dp[1] + stair[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+stair[i-1], dp[i-2]) + stair[i]

print(dp[n])