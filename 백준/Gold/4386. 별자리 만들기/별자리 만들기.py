import sys
input = sys.stdin.readline

# 모든 두 점의 거리를 cost로 해서 정렬 후 2개씩 합치기
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


n = int(input())
parent = list(range(0,n+1))
star = [0] * (n+1) # 별 정보 (index, x, y)
for i in range(1, n+1):
    star[i] = [i] + list(map(float, input().split()))

cost = []
for i in range(1,n+1):
    for j in range(i, n+1):
        cost.append((((star[i][1]-star[j][1])**2+(star[i][2]-star[j][2])**2)**(1/2), i,j))

cost.sort()
answer = 0

for c in cost:
    value, i1, i2 = c
    if find_parent(parent, i1) != find_parent(parent, i2):
        union_parent(parent, i1, i2)
        answer += value

print(round(answer,2))
