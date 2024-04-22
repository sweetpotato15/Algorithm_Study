import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp = [graph[0]] + [[0] * 3 for _ in range(n-1)]


if n ==2:
    answer1 = min(graph[0][0], graph[0][1]) + graph[1][2]
    answer2 = min(graph[0][0], graph[0][2]) + graph[1][1]
    answer3 = min(graph[0][1], graph[0][2]) + graph[1][0]
    print(min(answer1, answer2, answer3))
            
else:
    answer = []
    for first in range(3):
        if first == 0 : l,r = 1,2
        elif first == 1: l,r = 0,2
        else: l,r = 0,1
        dp[1][l] = dp[0][first] + graph[1][l]
        dp[1][r] = dp[0][first] + graph[1][r]
        dp[2][first] = min(dp[1][l], dp[1][r]) + graph[2][first]
        dp[2][l] = dp[1][r] + graph[2][l]
        dp[2][r] = dp[1][l] + graph[2][r]

        for i in range(3,n):
            for j in range(3):
                if i == n-1 and j == first: continue
                if j == 0: left, right = 1,2
                elif j == 1: left, right = -1,1
                else: left, right = -2,-1
                dp[i][j] = min(dp[i-1][j+left], dp[i-1][j+right]) + graph[i][j]
        answer.append(min(dp[-1][l], dp[-1][r]))    
    print(min(answer))