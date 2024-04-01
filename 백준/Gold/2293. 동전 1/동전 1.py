n, k = map(int, input().split())
coins  = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp = [0] * (k+1)
dp[0] = 1 # 0원을 만드는 경우의 수 : 1가지

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])