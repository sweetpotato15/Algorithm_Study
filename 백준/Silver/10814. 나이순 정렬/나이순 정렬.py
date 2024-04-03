import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(1,n+1):
    a,b = input().split()
    array.append((int(a),i,b))

array.sort()

for (a,b,c) in array:
    print(a,c)