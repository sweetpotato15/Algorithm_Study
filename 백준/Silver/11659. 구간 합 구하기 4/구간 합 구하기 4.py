import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 전체 개수 n, 합 구해야하는 횟수 m
number = list(map(int, input().split())) # 전체 숫자

dp = [0] * n
dp[0] = number[0]
for i in range(1,n):
    dp[i] = dp[i-1] + number[i]

for _ in range(m):
    a,b = map(int, input().split())
    if a == 1:
        print(dp[b-1])
    else:
        print(dp[b-1] - dp[a-2])