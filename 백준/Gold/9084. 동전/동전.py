import sys
input = sys.stdin.readline

def money(N, coins, M):
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
                dp[i] += dp[i-coin]
    return dp[-1]

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    answer = money(N,coins,M)
    print(answer)