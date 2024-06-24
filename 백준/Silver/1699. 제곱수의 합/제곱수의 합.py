import sys
input = sys.stdin.readline

N = int(input())
dp = list(range(N+1))
# dp[i] : i를 만드는데 최소의 횟수
# dp[i] = dp[제곱수] + dp[i-제곱수] 중 작은 값으로 저장

for i in range(1, N+1):
    for j in range(1, int(i**(1/2))+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[-1])