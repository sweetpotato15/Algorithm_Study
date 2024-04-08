# dp문제

import sys
input = sys.stdin.readline

def sum123():
    n = int(input())
    coins = [1,2,3]
    dp = [0] * (n+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]

    print(dp[n])

t = int(input())
for _ in range(t):
    sum123()