import sys
input = sys.stdin.readline

N, M = map(int, input().split())
square = [[-1]*(M+2)] + [[-1]+list(input().strip())+[-1] for _ in range(N)] + [[-1]*(M+2)]

ans = 1
for i in range(1, N+1):
    for j in range(1, M+1):
        value = square[i][j]
        for k in range(min(M-j, N-i)+1):
            if square[i+k][j+k] == value and square[i][j+k] == value and square[i+k][j] == value:
                ans = max(ans, k+1)
print(ans*ans)
