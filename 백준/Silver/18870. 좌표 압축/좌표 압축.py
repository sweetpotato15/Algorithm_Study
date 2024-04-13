import sys
input = sys.stdin.readline
from bisect import bisect_left

# 나보다 작은 서로 다른 좌표 개수
n = int(input())
number = list(map(int, input().split()))
number2 = list(set(number))
number2.sort()
for i in number:
    print(bisect_left(number2,i), end=" ")