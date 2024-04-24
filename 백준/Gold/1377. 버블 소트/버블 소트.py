import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append((int(input()),i))
result = 0
Asort = sorted(A)
for i in range(n):
    if result<Asort[i][1] - i:
        result = Asort[i][1]-i
print(result+1)