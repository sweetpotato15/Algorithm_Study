import sys
input = sys.stdin.readline
from itertools import combinations
n,m = map(int, input().split()) # n 개수, m 나눌 숫자
number = list(map(int, input().split()))
number = [x % m for x in number] # 나머지 저장

s = [0] * n # 누적합
s[0] = number[0]
for i in range(1,n):
    s[i] = s[i-1] + number[i]
C = [0] * m
answer =0 
for i in range(n):
    remainder = s[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    answer += C[i] * (C[i]-1) // 2

print(answer)