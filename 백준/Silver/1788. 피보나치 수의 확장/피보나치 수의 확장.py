import sys
input = sys.stdin.readline

dp=[0,1]
n = int(input())
if abs(n) != 0:
    for i in range(2, abs(n)+1):
        dp.append((dp[i-1] + dp[i-2]) % 1000000000)
    print(1 if n >0 or n % 2 == 1 else -1)
    print(dp[abs(n)])
else:
    print(0)
    print(0)
