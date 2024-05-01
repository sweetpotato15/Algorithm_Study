import sys
from bisect import bisect_left
input = sys.stdin.readline

n,m = map(int, input().split())
names = []
strong = []

for i in range(n):
    a, b = input().split()
    names.append(a)
    strong.append(int(b))

for i in range(m):
    a = int(input())
    index = bisect_left(strong, a)
    print(names[index])