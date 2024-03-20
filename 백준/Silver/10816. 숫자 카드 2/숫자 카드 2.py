# 주어진 숫자가 내 리스트에서 몇번 나오는지 출력하는 문제

n = int(input())
mynumber = list(map(int, input().split()))
mynumber.sort()

m = int(input())
number = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def CountNumber(array, number):
    right = bisect_right(array, number)
    left = bisect_left(array, number)
    return right - left

for i in number:
    print(CountNumber(mynumber, i), end = ' ')
