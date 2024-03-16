n = int(input())

A = []

for _ in range(n):
    a,b = map(int, input().split())
    A.append((a,b))

A = sorted(A)

for (a,b) in A:
    print(a, b)