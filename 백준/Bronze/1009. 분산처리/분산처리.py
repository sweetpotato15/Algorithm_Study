T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    if a == 1 or a == 5 or a == 6 :
        print(a)
    elif a == 0:
        print(10)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        if b%4 == 0:
            b = 4
        else:
            b = b%4
        print((a**b)%10)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            b = 2
        else:
            b = 1
        print((a**b)%10)
