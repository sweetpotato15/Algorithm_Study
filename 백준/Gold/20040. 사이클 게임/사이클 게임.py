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

array = []
for i in range(m):
    array.append(list(map(int, input().split())))
cylce = False
answer = 0

for i in range(m):
    a = array[i][0]
    b = array[i][1]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        cycle = True
        answer = i+1
        break

print(answer)
