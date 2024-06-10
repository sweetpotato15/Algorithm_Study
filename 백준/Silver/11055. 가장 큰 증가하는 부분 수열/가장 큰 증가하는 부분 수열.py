import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))
dp = [0] * (n+1) # 자기 자신자체로 초기화
maximum = 0
# 나 이전에 있는 최댓값의 dp값을 나에게 더해야함

for i in range(1, n+1): # 현재
    for j in range(i): # 나보다 이전 값
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j])
    dp[i] += array[i]

    
print(max(dp))