import sys
input = sys.stdin.readline
n = int(input())

Total = [ [0]*(100) for _ in range(100)]

for i in range(n):
    x,y = map(int, input().split())
    
    for i in range(10):
        for j in range(10):

            Total[x+i][y+j] += 1

count = 0
for i in range(100):
    for j in range(100):
        if Total[i][j] >= 1:
            count += 1

print(count)