import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

stack = [] 
answer = [0] * n

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

print(*answer)


