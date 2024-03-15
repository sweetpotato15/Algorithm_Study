n,m = map(int, input().split())
arr = [0] * (n+1)
for i in range(m):
    a,b,c = map(int, input().split())
    for j in range(a,b+1):
        arr[j] = c

for value in arr[1:]:
    print(value, end= ' ')