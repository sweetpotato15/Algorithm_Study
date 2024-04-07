# 최소신장트리
# x,y,z 거리를 따로 담아서 합치고 sort 한 다음에 최소 하나씩 꺼내서
import sys
input = sys.stdin.readline

n = int(input())
parent = list(range(n+1))

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

x,y,z = [], [], []
for i in range(1, n+1):
    a,b,c = map(int, input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

total = []
for i in range(n-1):
    total.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    total.append((abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    total.append((abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))

cost = 0
total.sort()
for i in total:
    c, a, b = i

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        cost += c
print(cost)