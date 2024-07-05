import sys
input = sys.stdin.readline

n = int(input())
array = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]

for i in range(1,n):
    for j in range(1,i+2):
        array[i][j] += max(array[i-1][j] , array[i-1][j-1]) 
print(max(array[-1]))