import sys
input = sys.stdin.readline
from math import *

m,n = map(int, input().split())
answer = []
def isprime(x):
    if x == 1:
        return
    if x == 2 or x == 3:
        print(x)
    else:
        for i in range(2,ceil(sqrt(x))+1):
            if x % i == 0:
                break
        else:print(x)


for i in range(m,n+1):
    isprime(i)