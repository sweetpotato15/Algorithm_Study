n = int(input())

for _ in range(n):
    a,b = input().split()
    for i in range(len(b)):
        print(b[i] * int(a), end='')
    print()