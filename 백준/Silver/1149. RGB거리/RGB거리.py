n = int(input())
# dp 테이블에 (i,j) 까지 칠할 수 있는 최소비용 넣기 (index, 앞뒤 같은색 주의)

cost = [0] * n
for i in range(n):
    cost[i] = list(map(int, input().split()))

# dp 의 첫 행은 cost 의 첫 행과 동일 
dp = [0] * n
dp[0] = cost[0]
for i in range(1,n):
    dp[i] = [0]*3

# dp에 채우기 
for i in range(1,n):
    for j in range(3):
        if j == 0:
            left = 1
            right = 2
            
        elif j == 1:
            left = -1
            right = 1
            
        else:
            left = -2
            right = -1
            
        dp[i][j] = min(dp[i-1][j+left], dp[i-1][j+right]) + cost[i][j]


print(min(dp[n-1]))