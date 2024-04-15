import sys
input = sys.stdin.readline

a,b = map(int, input().split())
a,b = max(a,b), min(a,b) # a > b

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        a,b = b, a%b
        return gcd(a,b)

print(a*b // gcd(a,b))