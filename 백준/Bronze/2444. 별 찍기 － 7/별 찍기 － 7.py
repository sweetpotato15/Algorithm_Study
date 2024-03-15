n = int(input())

for i in range(n):
    print(" "*(n-1-i)+"*"*(2*i+1))
for i in range(n-1):
    print(" "*(i+1)+"*"*(2*(n-i) - 3))    