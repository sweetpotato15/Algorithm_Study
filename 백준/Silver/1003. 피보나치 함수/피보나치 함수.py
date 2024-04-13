import sys
input = sys.stdin.readline

dp = [[0,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]

for n in range(3,41):
    dp[n][0] += dp[n-1][0] + dp[n-2][0]
    dp[n][1] += dp[n-1][1] + dp[n-2][1]


t = int(input())
for _ in range(t):
    x = int(input())
    print(dp[x][0],dp[x][1]) 