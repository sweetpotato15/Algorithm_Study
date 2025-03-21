N = int(input())

INF = int(1e6)
dp = [INF] * (int(1e5)+1)
dp[2] = 1
dp[5] = 1

for i in range(2, N+1):
    if i >= 5:
        dp[i] = min(dp[i-2]+1, dp[i-5]+1, dp[i])
    else:
        dp[i] = min(dp[i-2]+1, dp[i])

if dp[N] == INF:
    print(-1)
else:
    print(dp[N])