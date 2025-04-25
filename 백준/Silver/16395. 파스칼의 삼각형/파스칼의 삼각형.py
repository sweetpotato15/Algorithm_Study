n, k = map(int, input().split())

dp = [1]*(n+2)

def fact(n):
    if n == 1 or n == 0:
        return 1
    if dp[n] == 1:
        dp[n] = n*fact(n-1)
    return dp[n]

fact(n)
print(dp[n-1]//(dp[k-1]*dp[n-k]))
    
    