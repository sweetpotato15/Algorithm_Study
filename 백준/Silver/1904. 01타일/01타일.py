N = int(input())

dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2

if N == 1 or N == 2:
    print(dp[N])
else:
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    print(dp[N])