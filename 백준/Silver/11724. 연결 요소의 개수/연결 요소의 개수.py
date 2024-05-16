## 백준 11724
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

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

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = list(range(n+1))

for i in range(1,n+1):
    for j in graph[i]:
        union_parent(parent, i, j)

print(len(set(parent[1:])))