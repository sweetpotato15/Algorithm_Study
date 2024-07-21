import sys
input = sys.stdin.readline

while True:
    ans = 0
    a = input().strip().lower()
    if a == '#':
        break
    for i in ['a','e','i','o','u']:
        ans += a.count(i)
    print(ans)