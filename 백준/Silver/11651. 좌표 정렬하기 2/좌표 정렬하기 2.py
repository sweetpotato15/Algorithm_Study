import sys
input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    a,b = map(int, input().split())
    num.append((b,a))

num.sort()
for (a,b) in num:
    print(b,a)