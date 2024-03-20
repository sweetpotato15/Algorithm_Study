n = int(input()) # 가지고 있는 카드 수
mynumber = list(map(int, input().split()))
mynumber.sort()

m = int(input())
number = list(map(int, input().split()))

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in number:
    if binary_search(mynumber, 0, n-1, i) == None:
        print(0)
    else:
        print(1)