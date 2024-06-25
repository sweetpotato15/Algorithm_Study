import sys
input = sys.stdin.readline

N=int(input())
# 양쪽에 패딩 1씩
dp = [[0,0,1,1,1,1,1,1,1,1,1,0]] + [[0]*12 for _ in range(N-1)]
for i in range(1, N):
    for j in range(1,11):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[-1]) % 1000000000)