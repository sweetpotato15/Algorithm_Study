a,b,c,d,e,f = map(int, input().split())
if a == 0 :
    print(f//d-(e*c)//(b*d),c//b)
elif b == 0:
    print(c//a, f//e - (c*d) // (a*e))
elif d == 0:
    print(c//a - (b*f)//(a*e),f//e)
elif e == 0:
    print(f//d, c//b - (a*f)//(b*d))
else:

    print((b*f-e*c)//(b*d-a*e), (c*d-a*f)//(b*d-a*e))