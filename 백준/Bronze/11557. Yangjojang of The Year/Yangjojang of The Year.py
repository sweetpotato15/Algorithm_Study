import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n=int(input())
    new = []
    for _ in range(n):
        a, b = input().split()
        b = int(b)
        new.append([a,b])
    new = sorted(new, key = lambda x: x[1])
    print(new[-1][0])