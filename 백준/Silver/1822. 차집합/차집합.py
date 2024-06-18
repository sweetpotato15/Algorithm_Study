import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = A.difference(B)
print(len(A_B))
if A_B:
    print(*sorted(A_B))