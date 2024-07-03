G = int(input())
array = []
# i : x+y, j : x-y
for i in range(G,0,-1):
    if G % i == 0: #나누어 떨어진다면 
        j = G / i # i > j
        x = (i+j) / 2 
        y = (i-j) / 2 
        if y > 0 and (x%1 == 0 or y%1 == 0):
            array.append(int(x))

if not array:
    print(-1)
else:
    print(*sorted(array), sep = '\n')