n = int(input())
a = 'long '
b = 'int'

if n % 4 == 0 :
    print(a * (n // 4) + b)
else:
    print(a * (n // 4+1) +b)