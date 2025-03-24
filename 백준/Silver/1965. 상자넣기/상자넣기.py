import sys
input = sys.stdin.readline

N = int(input())
box_list = list(map(int, input().split()))

dp = [1] * N
for i in range(N):
    for j in range(i):
        if box_list[i] > box_list[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
