
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
answer = [0] + [int(input()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T+1)] 
# dp[i][j] : i초동안 j번 움직였을 경우 자두 최대 개수
# 움직인 횟수 (j)가 짝수면 1번 나무에 있을 경우(answer[i] == 1) 획득 가능
#                  홀수면 2번 나무에 있을 경우(answer[i] == 2) 획득 가능 

for i in range(1, T+1):
    # j == 0일 경우 1번 나무일 경우만 획득 가능
    if answer[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    
    # j가 1부터 W이하일까지
    for j in range(1,W+1):
        # 먹을 수 있는 경우 -> 이번에 움직여서 먹을건지, 이전에 움직여서 이번에 먹을건지
        if (answer[i] == 1 and j % 2 == 0) or (answer[i] == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        # 먹을 수 없는 경우 -> 움직일건지, 안움직일건지
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
        
print(max(dp[T]))