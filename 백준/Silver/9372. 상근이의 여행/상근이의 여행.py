# 루트 노드의 개수
import sys
input = sys.stdin.readline


t = int(input())
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

def topology():
    n, m = map(int, input().split())
    parent = list(range(n+1))
    answer = 0
    for i in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += 1
    print(answer)

for i in range(t):
    topology()