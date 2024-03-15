money = int(input())
n = int(input())

value = 0
for _ in range(n):
    a,b = map(int, input().split())
    value += a*b

if value == money:
    print("Yes")
else:
    print("No")