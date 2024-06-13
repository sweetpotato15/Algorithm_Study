import sys
input = sys.stdin.readline

def sticker(n, array):
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]
    dp[0][1] = array[0][1] + dp[1][0]
    dp[1][1] = array[1][1] + dp[0][0]
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2], dp[0][i-2]) + array[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + array[1][i]
    print(max(dp[0][-1], dp[1][-1]))

t = int(input())
for _ in range(t):
    n = int(input())
    array = [list(map(int, input().split())), list(map(int, input().split()))]
    if n == 1: print(*max(array))
    else: sticker(n, array)