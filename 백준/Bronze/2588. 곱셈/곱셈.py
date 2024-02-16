a = int(input())
b = int(input())

c = a * int(str(b)[-1])
d = a * int(str(b)[-2])
e = a * int(str(b)[0])
f = c + 10*d + 100*e

print(c)
print(d)
print(e)
print(f)