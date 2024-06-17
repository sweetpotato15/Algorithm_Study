n = int(input())
s = input().strip()

a = s.count('A')
b = n-a

if a == b:
    print('Tie')
elif a > b:
    print('A')
else:
    print('B')