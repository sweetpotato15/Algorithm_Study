import sys
input = sys.stdin.readline

array = [0,1,1,1,2,2] + [0]*95
# 1 1 1 2 2 3 4 5 7 9 12 16 21 
for i in range(6, 101):
    array[i] = array[i-1] + array[i-5]

T = int(input())
for _ in range(T):
    num = int(input())
    print(array[num])