import sys

input = sys.stdin.readline
n,m = map(int, input().split())
A = list(map(int, input().split()))

answer = 0 # 정답 count 수
S = [0] *n # 구간합 초기화
C = [0] * m # 나머지 같은 값 count 수
remainder = [0] * n

# 구간합 구하기
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 나머지 배열로 초기화
for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1
    
# 나머지 같은 값 (조합)

for i in range(m):
    if C[i] > 1:
        answer += C[i] * (C[i] -1) //2

print(answer)