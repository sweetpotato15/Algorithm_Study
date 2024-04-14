import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)
n = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 2
def fibo(x):
    if x == 1 or x == 2:
        return dp[x]
    elif dp[x] == 0:
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]
    return dp[x]
print(fibo(n)%10007)