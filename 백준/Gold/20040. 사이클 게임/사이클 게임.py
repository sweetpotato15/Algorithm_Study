import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # n개 점, m 선 - 홀수, 후 - 짝수
parent = list(range(n))

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

answer = 0

for i in range(1, m+1):
    a,b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b): # 사이클 발생 안함
        union_parent(parent, a, b)
    else: # 사이클 발생
        answer = i
        break

print(answer)