n, m = map(int, input().split())

A = [0] * n
B = [0] * n

for i in range(n):
    A[i] = list(map(int, input().split()))

for i in range(n):
    B[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(A[i][j] + B[i][j], end=" ")
    print()