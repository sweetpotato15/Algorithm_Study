
n , m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr = arr[:a] + list(reversed(arr[a:b+1])) + arr[b+1:]

for ans in arr[1:]:
    print(ans, end= ' ')