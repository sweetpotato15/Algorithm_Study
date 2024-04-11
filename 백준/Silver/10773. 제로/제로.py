import sys
input = sys.stdin.readline

k = int(input())
answer = []
for i in range(k):
    a = int(input())
    if a != 0:
        answer.append(a)
    else:
        answer.pop()

print(sum(answer))