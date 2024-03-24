n,m = map(int, input().split())
S = []
M = []
for i in range(n):
    S.append(input())

for i in range(m):
    M.append(input())
count = 0
for i in M:
    if i in S:
        count += 1
print(count)