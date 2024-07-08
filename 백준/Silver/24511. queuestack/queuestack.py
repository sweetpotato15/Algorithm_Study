import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
q = deque()
for i in range(N):
    if A[i] == 0:
        q.append(B[i])
# q = [1,4]
M = int(input())
C = list(map(int, input().split()))

for i in range(M):
    q.appendleft(C[i])
    print(q.pop(), end = ' ')