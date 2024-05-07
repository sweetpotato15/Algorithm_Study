import sys
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n):
    new = list(map(int, input().split()))
    answer = sorted(new + answer, reverse = True)[:n]
print(answer[-1])