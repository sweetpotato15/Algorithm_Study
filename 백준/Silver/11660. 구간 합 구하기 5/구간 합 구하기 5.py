import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [0] * (n+1)
D = [[0] * (n+1) for _ in range(n+1)]

A[0] = [0] * (n+1)
for i in range(1,n+1):
    A[i] = [0] + list(map(int, input().split()))

# D(x,y) = (1,1) ~ (x,y) 까지 합 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

#(x1,y1) ~ (x2,y2) 까지 합 구하기
for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1])