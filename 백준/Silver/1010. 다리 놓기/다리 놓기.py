
# 다리 놓기 
t = int(input())

for _ in range(t):
    left, right = map(int, input().split())
    dp = [0] * (right+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,right+1):
        dp[i] = i * dp[i-1]
        
    print(dp[right] // (dp[left] * dp[right-left]))