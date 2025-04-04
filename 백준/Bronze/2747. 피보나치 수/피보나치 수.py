N = int(input())

def fibo(n):
    dp = [0]*(N+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

answer = fibo(N)
print(answer)