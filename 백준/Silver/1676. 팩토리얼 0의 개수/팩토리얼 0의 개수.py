n = int(input())

n2 = 0
n5 = 0
for i in range(1, n+1):
    for j in range(1,n//2 +1):
        if i % (2**j) == 0:
            n2 += 1
        else:
            continue

for i in range(1, n+1):
    for j in range(1,n//5 +1):
        if i % (5**j) == 0:
            n5 += 1
        else:
            continue

print(min(n2, n5))