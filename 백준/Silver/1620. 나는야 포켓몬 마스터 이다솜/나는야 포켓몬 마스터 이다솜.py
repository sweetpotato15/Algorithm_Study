import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mylist = {}

for i in range(n):
    a = input().strip()
    mylist[i] = a
    mylist[a] = i

for _ in range(m):
    i = input().strip()
    if i.isalpha():
        print(mylist[i] + 1)
    else:
        print(mylist[int(i)-1])