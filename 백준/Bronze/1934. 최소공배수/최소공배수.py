t = int(input())

def LCM(a,b):
    gcd = 1
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            gcd = max(gcd, i)
    if gcd != 1:        
        lcm = gcd * (a // gcd) * (b // gcd)
    else:
        lcm = a * b

    print(lcm)

for _ in range(t):
    a,b = map(int, input().split())
    LCM(a,b)