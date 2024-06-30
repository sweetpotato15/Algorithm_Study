import sys
input = sys.stdin.readline
from copy import deepcopy

R, C, Q = map(int, input().split())
image = [[0]*(C+1)] + [[0] + list(map(int, input().split())) for _ in range(R)]

total_sum = deepcopy(image) # [i][j] : [i][0] ~ [i][j] 까지의 합

for i in range(1,R+1):
    for j in range(1, C+1):
        total_sum[i][j] = total_sum[i][j-1] + total_sum[i-1][j] - total_sum[i-1][j-1] + image[i][j]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    answer = total_sum[r2][c2] - total_sum[r2][c1-1] - total_sum[r1-1][c2] + total_sum[r1-1][c1-1]
    count = (r2-r1+1) * (c2-c1+1)
    print(answer // count)