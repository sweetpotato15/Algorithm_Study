import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

parent = list(range(n+1))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(1,n+1):
    array = list(map(int, input().split()))
    for j in range(1, n+1):
        if array[j-1] == 1:
            if find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)

city = list(map(int, input().split()))

answer = find_parent(parent, city[0])

for c in city:
    if answer != find_parent(parent, c):
        w = "NO"
        break
    else:
        w = "YES"

print(w)