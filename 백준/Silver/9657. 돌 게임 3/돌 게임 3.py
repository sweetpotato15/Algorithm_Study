import sys
input = sys.stdin.readline
N = int(input())

dp = [False] * (max(5,N+1)) # 상근이 이기면 True, 상근이 지면 False
rock = [1,3,4]
for i in rock:
    dp[i] = True

if N <= 4:
    answer = dp[N]

else:
    for i in range(5, N+1):
        if not (dp[i-1] and dp[i-3] and dp[i-4]):
            dp[i] = True
    answer = dp[-1]

if answer :print('SK')
else: print('CY')