import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # n : 표 크기, m : 구하는 횟수
A = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    A[i] = [0] + list(map(int, input().split()))
S = [[0]*(n+1) for _ in range(n+1)] # S  -> (1,1)부터 (i,j)까지 합
for i in range(1,n+1):
    for j in range(1,n+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + A[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    answer = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(answer)
