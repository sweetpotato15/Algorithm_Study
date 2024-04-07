import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
array = []
parent = list(range(v+1))

cost = 0 
for i in range(e):
    a,b,c = map(int, input().split())
    array.append((c, a, b))
array.sort()

for i in array:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c

print(cost)