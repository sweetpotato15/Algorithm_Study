n, k = map(int, input().split())

dp = [0] * (k+1) # dp[i] : i 만큼의 무게에 해당하는 최대 가치 저장 -> dp[-1] 출력 (무게가 k 이하일 경우포함)


for i in range(n):
    weight, value = map(int, input().split())
    for j in range(k, weight-1, -1):
        dp[j] = max(dp[j-weight] + value, dp[j])


print(dp[-1])