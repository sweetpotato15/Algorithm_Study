import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    s = list(input().split())
    for i in s:
        print(i[::-1], end=' ')
    print()