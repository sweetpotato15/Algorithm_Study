n,k = map(int, input().split())

dp = [1] * (n+1)
for i in range(1,n+1):
    dp[i] = i * dp[i-1]
answer = dp[n] // (dp[n-k] * dp[k])
print(answer % 10007)
