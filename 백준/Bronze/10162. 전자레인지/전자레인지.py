a = 300
b = 60
c = 10

T = int(input())
n1,n2,n3 = T // a, (T%a) // b, ((T%a) % b ) // c

if ((T%a) % b ) % c != 0:
    print(-1)
else:
    print(n1,n2,n3)