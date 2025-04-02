import sys
input = sys.stdin.readline

N = int(input())
ans = 0
dict = {}
for _ in range(N):
    name = input().strip()
    if name in dict.keys():
        continue
    if name == 'ENTER':
        dict = {}
        continue
    dict[name] = 1
    ans += 1
print(ans)