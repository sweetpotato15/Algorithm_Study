import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int, input().split()) # n+1 집합 개수, m 연산개수

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a,b,c = map(int, input().split())
    if a == 0:
        union_parent(parent, b,c)
    else:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")