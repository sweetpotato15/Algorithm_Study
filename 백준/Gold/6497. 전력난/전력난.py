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

while True:
    m, n = map(int, input().split()) # m 집의 수 n 길의 수
    if m == 0 and n == 0: 
        break
    parent = list(range(m))

    array = []
    total = 0 # 원래 길의 수 총 비용
    for _ in range(n):
        a,b,c = map(int, input().split()) # a,b 연결, c 거리
        array.append((c, a,b))
        total += c

    if n == m-1:
        print(0)
    else:
        cost = 0 # 최소 비용
        array.sort()

        for i in range(n):
            c,a,b = array[i]
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
                cost += c
        print(total - cost)