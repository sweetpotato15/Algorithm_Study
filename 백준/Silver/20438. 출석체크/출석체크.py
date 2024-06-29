import sys
input = sys.stdin.readline
from math import floor
N,K,Q,M = map(int, input().split())
# 학생수, 졸고있는 학생수, 출석코드 보낼 학생수, 구간수
sleep = list(map(int, input().split()))
code_std = list(map(int, input().split()))

code = [False] * 3 + [False] * (N)
for s in code_std:
    if s in sleep:
        continue
    for j in range(1,floor((N+3)/s)+1):
        if s*j <= N+2:
            code[s*j] = True

for s in sleep:
    code[s] = False

for _ in range(M):
    S,E = map(int, input().split())
    print(E-S+1 - sum(code[S:E+1]))